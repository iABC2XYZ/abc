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
        self.sizeInput=self.GetSizeInput()
        self.sizeOutput=self.GetSizeOutput()
        self.numDiffData= numDiffData
        self.numItem=np.shape(self.xData)[0]
    
    def SetNN(self,NN='FC',numEpoch=10000,learningRate=0.001,batchSize=100,typeLoss='mse',typeTrain='adamoptimizer',configSession=''):
        self.NN=NN.lower()
        self.numEpoch=np.int32(numEpoch)
        self.learningRate=learningRate
        self.batchSize=np.int32(batchSize)
        
        self.typeLoss=typeLoss.lower()
        self.typeTrain=typeTrain.lower()
        
        self.configSession=configSession
            
        
    
    def SetRec(self,numRec=100,numRecStep=100):
        self.numRec=numRec
        self.numRecStep=numRecStep
    
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

    
    def Build(self):
        self.xIn=tf.placeholder(tf.float32,shape=(None,self.sizeInput))
        self.yIn=tf.placeholder(tf.float32,shape=(None,self.sizeOutput))
        self.xOut=self.GetOutX()
        self.yOut=self.GetOutY()
        self.loss=self.GetLoss()
        self.train=self.GetTrain()
        self.opt=self.GetOpt()
        
    def GetSizeInput(self):
        if self.configXData=='x':
            sizeInput=np.shape(xData)[1]
        elif self.configXData=='dx':
            sizeInput=np.shape(xData)[1]
        elif self.configXData=='x+dx':
            sizeInput=np.shape(xData)[1]*2

        return sizeInput

    def GetSizeOutput(self):
        if self.configYData=='y':
            sizeOutput=np.shape(yData)[1]
        elif self.configYData=='dy':
            sizeOutput=np.shape(yData)[1]
        elif self.configYData=='y+dy':
            sizeOutput=np.shape(yData)[1]*2        
        return sizeOutput          
    
    
    def GetOutX(self):
        if self.NN=='matrix':
            xOut= self.Matrix()
        if self.NN=='fc':
            xOut=self.FC()
        if self.NN=='complex':
            self.X=self.xIn
            print self.X
        if self.NN=='cnn1D':
            pass
        if self.NN=='cnn2D':
            pass    
        if self.NN=='rnn':
            pass    
        return xOut
    def GetOutY(self):
        yOut=self.yIn
        return yOut

   
    
    def AddFC(self,sizeInput,sizeOutput,typeAct='relu'):
        if sizeInput==0:
            sizeInput = self.sizeInput
        if  sizeOutput==0:
            sizeOutput=self.sizeOutput
        w=self.GenWeight((sizeInput,sizeOutput))
        b=self.GenBias(sizeOutput)
        X=tf.nn.xw_plus_b(self.X,w,b)
        xAtc=self.Act(X,typeAct)
        
        self.X=xAtc
        self.xOut=xAtc
        


    
        
    
    

    def GenWeight(self,shape):
        initial = tf.truncated_normal(shape, stddev=1.)
        return tf.Variable(initial)
    def GenBias(self,size):
        initial=self.GenWeight((1,size))
        return initial[0,:]
    
    def GetLoss(self):
        if self.typeLoss=='mse':
            loss=tf.losses.mean_squared_error(self.xOut,self.yOut)
        if self.typeLoss=='cross_entropy':
            #loss=tf.nn.softmax_cross_entropy_with_logits(self.xOut,self.yOut)
            xSoft=tf.nn.softmax(self.xOut)
            ySoft=tf.nn.softmax(self.yOut)
            loss=-tf.reduce_mean(xSoft*tf.log(ySoft))
            
        return loss
    
    def GetTrain(self):
        if self.typeTrain=='adamoptimizer':
            train=tf.train.AdamOptimizer(self.learningRate)
        return train
    
    def GetOpt(self):
        opt=self.train.minimize(self.loss)
        return opt
    
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
    
    
    def conv1d(x, W,stride=1,padding="SAME"):
        return tf.nn.conv1d(x, W, stride, padding)
    
    def conv2d(x, W,strides=[1,1,1,1], padding="SAME"):
        return tf.nn.conv2d(x, W, strides, padding)


    def Matrix(self):
        shapeM=(self.sizeInput,self.sizeOutput)
        M=self.GenWeight(shapeM)
        xOut=tf.matmul(self.xIn,M)
        return xOut
    
    def FC(self):
        sizeLayer=self.sizeHidden
        sizeLayer.insert(0,self.sizeInput)
        sizeLayer.append(self.sizeOutput)
        
        numCalculation4NN=self.numCalculation4NN
        
        wRec=[]
        bRec=[]
        for iLayer in range(numCalculation4NN):
            if iLayer==0:
                X=self.xIn
            numIn=np.int32(sizeLayer[iLayer])
            numOut=np.int32(sizeLayer[iLayer+1])
            w=self.GenWeight((numIn,numOut))
            b=self.GenBias(numOut)
            wRec.append(w)
            bRec.append(b)
            X=tf.nn.xw_plus_b(X,w,b)
            
            try:
                typeAct=self.typeAct[iLayer]
            except:
                typeAct=''
            
            X=self.Act(X,typeAct)
                
        xOut=X

        return xOut
    
    def SetFC(self,sizeHidden,typeAct=['relu*n']):
        self.sizeHidden=self.GetSizeHidden(sizeHidden)
        self.numCalculation4NN=len(self.sizeHidden)+1
        self.typeAct=self.GetTypeAct(typeAct)
    
    def GetSizeHidden(self,sizeHidden):
        try:
            if 0 in sizeHidden:
                sizeHidden.pop(sizeHidden.index(0))
        except:
            if sizeHidden==0:
                sizeHidden=[]
            else:
                sizeHidden=[sizeHidden]
        return sizeHidden 
    
    def GetTypeAct(self,typeAct):
        if len(typeAct)==1:
            # 先判断是不是　‘?*n’,如果是，那么除了最有一层不用激活函数之外，其余的都用相同的激活函数。
            typeAct_0=typeAct[0]
            if '*n' in typeAct_0:
                idTypeActWord=typeAct_0.index('*')
                typeActWord=typeAct_0[0:idTypeActWord]
                self.typeAct=[typeActWord]*(self.numCalculation4NN-1)
            
            # 再考虑是不是‘?*ｍ’其中ｍ是具体的数值。如果是集体的数值，那么就是前ｍ个使用某一个激活函数
            elif "*" in typeAct_0:
                idTypeActWord=typeAct_0.index('*')
                typeActWord=typeAct_0[0:idTypeActWord]
                typeActNum=typeAct_0[idTypeActWord+1::]
                self.typeAct=[typeActWord]*(np.int32(typeActNum))             
            
            # 再考虑:就只有一层
            elif '*' not in typeAct_0:
               self.typeAct=typeAct 
            

        else:
            # 再是一般情况
            self.typeAct=[]
            for iTypeAct in typeAct:
                if '*' not in iTypeAct:
                    self.typeAct.append(iTypeAct)
                else:
                    idTypeActWord=iTypeAct.index('*')
                    typeActWord=iTypeAct[0:idTypeActWord]
                    typeActNum=iTypeAct[idTypeActWord+1::]
                    typeActTmp=[typeActWord]*(np.int32(typeActNum))
                    for i in range(np.int32(typeActNum)):
                        self.typeAct.append(typeActTmp[i])


            
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
        if self.configXData=='x':
            X=x1
        elif self.configXData=='dx':
            X=dx
        elif self.configXData=='x+dx':
            X=np.hstack((x1,dx))
            
        if self.configYData=='y':
            Y=y1
        elif self.configYData=='dy':
            Y=dy
        elif self.configYData=='y+dy':
            Y=np.hstack((y1,dy))
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
        rYAimRelaRec=[]
        rYAimRelaMeanRec=[]
        
        for iEpoch in range(self.numEpoch):
            X,Y=self.PreData()
            sess.run(self.opt,feed_dict={self.xIn:X,self.yIn:Y})
            
            if iEpoch % self.numRecStep==0:
                lossNow=sess.run(self.loss,feed_dict={self.xIn:X,self.yIn:Y})
                lossRec.append(lossNow)

                yAim=sess.run(self.xOut,feed_dict={self.xIn:self.xPre})[0]
                rYAim=np.sqrt(np.mean(np.square(yAim)))
                rYAimRec.append(rYAim)
                
                lossMeanRec.append(np.mean(lossRec))
                rYAimMeanRec.append(np.mean(rYAimRec))
                
                rYAimRelaRec.append(np.sqrt(np.mean(np.square(np.log(np.abs(yAim))))))
                rYAimRelaMeanRec.append(np.mean(rYAimRelaRec))
                if len(lossRec)>self.numRec:
                    lossRec.pop(0)
                    rYAimRec.pop(0)
                    lossMeanRec.pop(0)
                    rYAimMeanRec.pop(0)
                    rYAimRelaRec.pop(0)
                    rYAimRelaMeanRec.pop(0)
                
                
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

                plt.figure('yAim : Relative')
                plt.clf()
                yAimRela=np.sign(yAim)*np.log(np.abs(yAim))
                plt.plot(yAimRela,'-o')
                plt.grid('on')
                plt.title(iEpoch)
                plt.pause(0.01)    
                
                plt.figure('rYAim  : Relative')
                plt.clf()
                plt.hold
                plt.plot(rYAimRelaRec,'b-o')
                plt.plot(rYAimRelaMeanRec,'g-o')
                plt.grid('on')
                plt.title(iEpoch)
                plt.pause(0.01)  
                
                
        sess.close()    

      
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

'''
x=DL()
x.SetData(xData,yData,'x+dx','y')
x.SetNN(NN='fc',numEpoch=1e5,learningRate=0.005)
x.SetFC(sizeHidden=[20],typeAct=['','relu','relu*5','sigmod'])
x.Build()

x.SetRec()
x.SetPre(xPre=-1)


x.RunTrain()
'''
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-


'''
x1=DL()
x1.SetData(xData,yData,'x+dx','y')
x1.SetNN(NN='matrix',numEpoch=1e5,learningRate=0.005)
x1.Build()

x1.SetRec()
x1.SetPre(xPre=-1)


x1.RunTrain()
'''


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-


x2=DL()
x2.SetData(xData,yData,'x+dx','y')
x2.SetNN(NN='Complex',numEpoch=1e5,learningRate=0.005)
#AddFC(self,sizeInput,sizeOutput,typeAct='relu')

x2.AddFC(0,0,typeAct='relu')

x2.Build()


            


                
                

    
    


