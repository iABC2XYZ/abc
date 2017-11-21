#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 19:43:06 2017

@author: p
"""
import numpy as np

import tensorflow as tf
import matplotlib.pyplot as plt
plt.close('all')

class DL:
    def __init__(self):
        self.sizeHidden=[]

    def SetData(self,xData,yData,configXData='dx',configYData='dy',numDiffData=None):
        self.xData=xData
        self.yData=yData
        self.configXData=configXData.lower()
        self.configYData=configYData.lower()
        self.GetZnum()
        self.sizeInput=self.GetSizeInput()
        self.sizeOutput=self.GetSizeOutput()
        self.numDiffData= numDiffData
        self.numItem=np.shape(self.xData)[0]
        
        self.xIn=tf.placeholder(tf.float32,shape=(None,self.sizeInput))
        self.yIn=tf.placeholder(tf.float32,shape=(None,self.sizeOutput))
        
        self.numOutputLayer4FC=self.sizeInput       #会记录上次的sizeOutput,它可以由D1_in_channels生成。
        
        self.D1_in_channels=0       #会记录上次的D1_ｏｕｔ_channels


    
    def SetNN(self,numEpoch=10000,learningRate=0.001,batchSize=100,typeLoss='mse',typeTrain='adamoptimizer',configSession=''):
        self.numEpoch=np.int32(numEpoch)
        self.learningRate=learningRate
        self.batchSize=np.int32(batchSize)
        
        self.typeLoss=typeLoss.lower()
        self.typeTrain=typeTrain.lower()
        
        self.configSession=configSession
        
        self.X=self.xIn


    def SetRec(self,numRec=100,numRecStep=100):
        self.numRec=numRec
        self.numRecStep=numRecStep
    '''
    def SetPre(self,xPre=-1):
        if type(xPre)==int:      #　作为开关使用的
            if xPre==-1:         #  此时表示内部测试，即用数据内部特征测试
                if self.configXData=='x':       #此时需要将ｘ全部校正到０，即ｘ＝０
                    xPreTmp=np.zeros((1,self.sizeInput))
                if self.configXData=='dx':      # 由于ｍｅａｎ上ｘ并不是０，因此为了将ｘ－>0，需要将ｄｘ变化量为　－ｍｅａｎ
                    xMean=np.mean(self.xData,axis=0)[np.newaxis,:]
                    xPreTmp=-xMean
                if self.configXData=='x+dx':    #  综合前两个，意思是在当前ｍｅａｎ位置上，调到０，调幅－ｍｅａｎ
                    xMean=np.mean(self.xData,axis=0)[np.newaxis,:]
                    xPreTmp=np.hstack((xMean,-xMean))
                self.xPre=xPreTmp


        if type(xPre)==list:     #如果是个list，将这个list转化成numpy.ndarray，之后直接作为xPre
            xPreTmp=np.array(xPre)
            self.xPre=xPreTmp
            
        if type(xPre)==np.ndarray:  #如果这是一个数组，那么直接就是将数组作为xPre
            xPreTmp=xPre
            self.xPre=xPreTmp

    '''
    def SetPre(self,xPre=-1):
        if type(xPre)==int:      #　作为开关使用的
            if xPre==-1:         #  此时表示内部测试，即用数据内部特征测试
                if 'x+dx' in self.configXData:    #  综合前两个，意思是在当前ｍｅａｎ位置上，调到０，调幅－ｍｅａｎ
                    xMean=np.mean(self.xData,axis=0)[np.newaxis,:]
                    xPreTmp=np.hstack((xMean,-xMean))
                elif 'dx' in self.configXData:      # 由于ｍｅａｎ上ｘ并不是０，因此为了将ｘ－>0，需要将ｄｘ变化量为　－ｍｅａｎ
                    xMean=np.mean(self.xData,axis=0)[np.newaxis,:]
                    xPreTmp=-xMean
                elif 'x' in self.configXData:       #此时需要将ｘ全部校正到０，即ｘ＝０
                    xPreTmp=np.zeros((1,self.sizeInput))
                
                
                
                if self.zXPlusLen>0:
                    yMean=np.mean(self.yData,axis=0)
                    idChoose=range(self.zXPlusStart,self.zXPlusEnd)
                    yMeanChoose=(yMean[idChoose])[np.newaxis,:]

                    
                    xPreTmp=np.hstack((xPreTmp,yMeanChoose))
                if self.zXMinusLen>0:
                    idDelete=range(self.zXMinusStart,self.zXMinusEnd)
                    np.delete(xPreTmp,idDelete)

                self.xPre=xPreTmp


        if type(xPre)==list:     #如果是个list，将这个list转化成numpy.ndarray，之后直接作为xPre
            xPreTmp=np.array(xPre)
            self.xPre=xPreTmp
            
        if type(xPre)==np.ndarray:  #如果这是一个数组，那么直接就是将数组作为xPre
            xPreTmp=xPre
            self.xPre=xPreTmp    
    
    
    
    def Build(self):
        self.GetOutX()
        self.GetOutY()
        self.GetLoss()
        self.GetTrain()
        self.GetOpt()        



    def GetOutX(self):
        self.xOut=self.X
    def GetOutY(self):
        self.yOut=self.yIn

    def GetLoss(self):
        if self.typeLoss=='mse':
            self.loss=tf.losses.mean_squared_error(self.xOut,self.yOut)
        if self.typeLoss=='cross_entropy':
            xSoft=tf.nn.softmax(self.xOut)
            ySoft=tf.nn.softmax(self.yOut)
            self.loss=-tf.reduce_mean(xSoft*tf.log(ySoft))

    
    def GetTrain(self):
        if self.typeTrain=='adamoptimizer':
            self.train=tf.train.AdamOptimizer(self.learningRate)

    
    def GetOpt(self):
        self.opt=self.train.minimize(self.loss)


    def GetZnum(self):
        self.zXPlusLen=0
        self.zXMinusLen=0
        self.zYPlusLen=0
        self.zYMinusLen=0        

        if '+z:' in self.configXData:
            strStart=self.configXData.index('[')
            strMid=self.configXData.index(',')
            strEnd=self.configXData.index(']')
            
            self.zXPlusStart=np.int32(self.configXData[strStart+1:strMid])-1
            self.zXPlusEnd=np.int32(self.configXData[strMid+1:strEnd])
            self.zXPlusLen=self.zXPlusEnd-self.zXPlusStart
        if '-z:' in self.configXData:
            strStart=self.configXData.index('[')
            strMid=self.configXData.index(',')
            strEnd=self.configXData.index(']')
            
            self.zXMinusStart=np.int32(self.configXData[strStart+1:strMid])-1
            self.zXMinusEnd=np.int32(self.configXData[strMid+1:strEnd])
            self.zXMinusLen=self.zXMinusEnd-self.zXMinusStart
            
        if '+z:' in self.configYData:
            strStart=self.configYData.index('[')
            strMid=self.configYData.index(',')
            strEnd=self.configYData.index(']')
            
            self.zYPlusStart=np.int32(self.configYData[strStart+1:strMid])-1
            self.zYPlusEnd=np.int32(self.configYData[strMid+1:strEnd])
            self.zYPlusLen=self.zYPlusEnd-self.zYPlusStart
            
        if '-z:' in self.configYData:
            strStart=self.configYData.index('[')
            strMid=self.configYData.index(',')
            strEnd=self.configYData.index(']')

            self.zYMinusStart=np.int32(self.configYData[strStart+1:strMid])-1
            self.zYMinusEnd=np.int32(self.configYData[strMid+1:strEnd])
            self.zYMinusLen=self.zYMinusEnd-self.zYMinusStart


    def GetSizeInput(self):
        if 'x+dx' in self.configXData:
            sizeInput=np.shape(xData)[1]*2+self.zXPlusLen-self.zXMinusLen
        elif 'dx' in self.configXData:
            sizeInput=np.shape(xData)[1]+self.zXPlusLen-self.zXMinusLen
        elif 'x' in self.configXData:
            sizeInput=np.shape(xData)[1]+self.zXPlusLen-self.zXMinusLen
        return sizeInput

    def GetSizeOutput(self):
        if 'y+dy' in  self.configYData:
            sizeOutput=np.shape(yData)[1]*2+self.zYPlusLen-self.zYMinusLen
        elif 'dy' in self.configYData:
            sizeOutput=np.shape(yData)[1]+self.zYPlusLen-self.zYMinusLen
        elif 'y' in self.configYData:
            sizeOutput=np.shape(yData)[1]+self.zYPlusLen-self.zYMinusLen
            
        return sizeOutput      

    def GenWeight(self,shape):
        initial = tf.truncated_normal(shape, stddev=1.)
        return tf.Variable(initial)
    def GenBias(self,size):
        initial=self.GenWeight((1,size))
        return initial[0,:]
    
    def Act(self,X,typeAct):
        if typeAct=='relu':
            xAct=tf.nn.relu(X)
        if typeAct=='relu6':
            xAct=tf.nn.relu6(X)
        if typeAct=='sigmoid':
            xAct=tf.nn.sigmoid(X)
        if typeAct=='tanh':
            xAct=tf.nn.tanh(X)
        if typeAct=='elu':
            xAct=tf.nn.elu(X)
        if typeAct=='softplus':
            xAct=tf.nn.softplus(X)
        if typeAct=='softsign':
            xAct=tf.nn.softsign(X)
        if typeAct=='':
            xAct=X
        return xAct

        
    def PreData(self):
        idChoose2=np.random.randint(0,high=self.numItem,size=(self.batchSize))
        if self.numDiffData==None:
            idChoose1=np.random.randint(0,high=self.numItem,size=(self.batchSize))
        else:
            idChoose1=idChoose2-self.numDiffData
        x1=self.xData[idChoose1,:]
        x2=self.xData[idChoose2,:]
        y1=self.yData[idChoose1,:]
        y2=self.yData[idChoose2,:]
        dx=x2-x1
        dy=y2-y1

        if 'x+dx' in self.configXData:
            X=np.hstack((x1,dx))
        elif 'dx' in self.configXData:
            X=dx
        elif 'x' in self.configXData:
            X=x1
        
        if 'y+dy' in self.configYData:
            Y=np.hstack((y1,dy))  
        elif  'dy' in self.configYData:
            Y=dy
        elif 'y' in self.configYData:
            Y=y1
        

        if self.zXPlusLen>0:
            X=np.hstack((X,Y[:,self.zXPlusStart:self.zXPlusEnd]))
        if self.zYPlusLen>0:
            Y=np.hstack((Y,X[:,self.zYPlusStart:self.zYPlusEnd]))
        if self.zXMinusLen>0:
            xLen=np.shape(X)[1]
            idStay=range(0,self.zXMinusStart)
            idStay_2=range(self.zXMinusEnd,xLen)
            
            for i in idStay_2:
                idStay.append(i)
            X=X[:,idStay]
            
        if self.zYMinusLen>0:

            yLen=np.shape(Y)[1]
            idStay=range(0,self.zYMinusStart)
            idStay_2=range(self.zYMinusEnd,yLen)
            
            for i in idStay_2:
                idStay.append(i)
            Y=Y[:,idStay]
            
            
            
            

            
        
        '''
        if '+z:' in self.configXData:
            strStart=self.configXData.index(':')
            steEnd=self.configXData.index('-')
            nStart=np.int32(self.configXData[strStart:steEnd])
            print nStart
 
            X=x1
        ''' 
        
        
            

        return X,Y
    
    
        
    def RunTrain(self):
        if self.configSession=='':
            sess=tf.Session()
        else:
            sess=tf.Session(self.configSession)
        sess.run(tf.global_variables_initializer())
        
        lossRec=[]
        rYAimRec=[]
        lossMeanRec=[]
        rYAimMeanRec=[] 

        
        for iEpoch in range(self.numEpoch):
            X,Y=self.PreData()
            
            #print np.shape(X)
            #print np.shape(Y)
            #print tf.shape(self.xIn)
            #print tf.shape(self.yIn)
            
            sess.run(self.opt,feed_dict={self.xIn:X,self.yIn:Y})
            
            if iEpoch % self.numRecStep==0:
                lossNow=sess.run(self.loss,feed_dict={self.xIn:X,self.yIn:Y})
                lossRec.append(lossNow)

                yAim=sess.run(self.xOut,feed_dict={self.xIn:self.xPre})[0]
                rYAim=np.sqrt(np.mean(np.square(yAim)))
                rYAimRec.append(rYAim)
                
                lossMeanRec.append(np.mean(lossRec))
                rYAimMeanRec.append(np.mean(rYAimRec))
                

                if len(lossRec)>self.numRec:
                    lossRec.pop(0)
                    rYAimRec.pop(0)
                    lossMeanRec.pop(0)
                    rYAimMeanRec.pop(0)

                
                
                plt.figure('loss')
                plt.clf()
                plt.hold
                plt.plot(lossRec,'b-o')
                plt.plot(lossMeanRec,'g-o')
                plt.grid('on')
                plt.title(iEpoch)
                plt.pause(0.01)
                
                plt.figure('rYAim')
                plt.clf()
                plt.hold
                plt.plot(rYAimRec,'b-o')
                plt.plot(rYAimMeanRec,'g-o')
                plt.grid('on')
                plt.title(iEpoch)
                plt.pause(0.01)                

                plt.figure('yAim')
                plt.clf()
                plt.plot(yAim,'-o')
                plt.grid('on')
                plt.title(iEpoch)
                plt.pause(0.01)                


                
                
        sess.close()           
        
    def AddFC(self,numOutputLayer,typeAct=''):
        if numOutputLayer==0:
            numOutputLayer=self.sizeOutput
        
        w=self.GenWeight((self.numOutputLayer4FC,numOutputLayer))
        b=self.GenBias(numOutputLayer)
        X=tf.nn.xw_plus_b(self.X,w,b)
        self.X=self.Act(X,typeAct)
        
        self.numOutputLayer4FC=numOutputLayer

    def conv1d(self,x, W,stride, padding):
        return tf.nn.conv1d(x,W,stride, padding)
    
    def AddCNN1D(self,D1_filter_width, D1_out_channels, D1_in_channels=0,typeAct='',stride=1, padding="SAME",reshape=0):
        if D1_in_channels==0 and self.D1_in_channels==0:
            self.X=tf.expand_dims(self.X, -1)
            self.D1_in_channels=1
        
        if D1_in_channels!=0:
            self.D1_in_channels=D1_in_channels
        
        w=self.GenWeight((D1_filter_width, self.D1_in_channels, D1_out_channels))
        b=self.GenBias((D1_out_channels))
        X=self.conv1d(self.X,w,stride, padding)+b
        self.X=self.Act(X,typeAct)

        
        if reshape==1:
            self.numOutputLayer4FC=self.numOutputLayer4FC*D1_out_channels
            self.X=tf.reshape(self.X,(-1,self.numOutputLayer4FC))
            
        
        self.D1_in_channels=D1_out_channels
        
        

        
        '''
        X=self.X
        X=tf.reshape()
        
        w=self.GenWeight((filter_width, in_channels, out_channels))
        b=self.GenBias((out_channels))
        X=self.conv1d(self.X,w,stride, padding)+b
        self.X=self.Act(X,typeAct)
        '''

        

    
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
'''
fName='data1~2000'
def GetData(fName):    
    data=np.loadtxt(fName)
    bpmData=data[:,0:12]
    dcData=data[:,80:94]
    q1Data=data[:,140:143]
    q2Data=data[:,144:147]
    psData=np.hstack((dcData,q1Data,q2Data))
    return bpmData,psData
    
xData,yData=GetData(fName)


x=DL()
x.SetData(xData,yData,'x+dx','y')
x.SetNN(numEpoch=1e5,learningRate=0.005)
x.AddFC(10,'relu')
x.AddFC(0,'')
x.Build()

x.SetRec()
x.SetPre(xPre=-1)


x.RunTrain()
'''

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

fName='data1~2000'
def GetData(fName):    
    data=np.loadtxt(fName)
    bpmData=data[:,0:12]
    dcData=data[:,80:94]
    q1Data=data[:,140:143]
    q2Data=data[:,144:147]
    psData=np.hstack((dcData,q1Data,q2Data))
    return bpmData,psData
    
xData,yData=GetData(fName)


#print np.shape(xData)
#print np.shape(yData)

x=DL()
x.SetData(xData,yData,'x+dx+z:[15,20]','y-z:[15,20]')


x.SetNN(numEpoch=1e9,learningRate=0.002)
x.AddFC(0,'relu')
x.AddFC(0,'')
#x.AddCNN1D(D1_filter_width=3, D1_out_channels=5, D1_in_channels=0,typeAct='',stride=1, padding="SAME",reshape=0)
#x.AddCNN1D(D1_filter_width=1, D1_out_channels=8, D1_in_channels=0,typeAct='',stride=1, padding="SAME",reshape=1)
#x.AddFC(0,'')



x.Build()
x.SetRec()

x.SetPre(xPre=-1)

x.RunTrain()






print "END"
     
                

    
    


