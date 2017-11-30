#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 23:43:20 2017

@author: p
"""

import numpy as np

import tensorflow as tf
import matplotlib.pyplot as plt

plt.close('all')

import time



class DL:
    def __init__(self):
        self.sizeHidden=[]
        
    def tic(self):
        self.timeStart= time.clock()
    def toc(self):
        self.timeEnd= time.clock()
        self.timeElapsed=self.timeEnd-self.timeStart
        print('Time Elapsed %.5f s'%self.timeElapsed)
        
        
    def SetTrainList(self,mlTrainList):
        self.listTrain=mlTrainList
    def SetTestList(self,mlTestList):
        self.listTest=mlTestList
    
    def SetPreList(self,mlPreList):
        self.listPre=mlPreList


    def SetDataInit(self,configXData,configYData,numDiffData):
        self.configXData=configXData.lower()
        self.configYData=configYData.lower()
        self.GetZnum()
        self.sizeInput=self.GetSizeInput()
        self.sizeOutput=self.GetSizeOutput()
        self.numDiffData= numDiffData
        self.numItem=np.shape(self.xTrain)[0]
        
        self.xIn=tf.placeholder(tf.float32,shape=(None,self.sizeInput))
        self.yIn=tf.placeholder(tf.float32,shape=(None,self.sizeOutput))
        
        self.numOutputLayer4FC=self.sizeInput       #会记录上次的sizeOutput,它可以由D1_in_channels生成。
        
        self.D1_in_channels=0       #会记录上次的D1_ｏｕｔ_channels

        
    def GetTrainData(self,fName):    
        X=np.loadtxt(fName+'.train')
        Y=np.loadtxt(fName+'.label')    
        return X,Y
    
    def GetPreData(self,fName):
        X=np.loadtxt(fName+'.pre')
        return X


    def SetDataConfig(self,configXData='dx',configYData='dy',numDiffData=None,numChangeData=None):
        self.xTrain,self.yTrain=self.GetTrainData(self.listTrain[0])
        self.xTest,self.yTest=self.GetTrainData(self.listTest[0])
        self.xPre=self.GetPreData(self.listPre[0])
        if numChangeData==None:
            self.numChangeData=4000
        else:
            self.numChangeData=numChangeData
        
        self.SetDataInit(configXData,configYData,numDiffData)

    def ChangeData(self):
        numListTrain=len(self.listTrain)
        if numListTrain>0:
            iList=np.random.choice(numListTrain)
            self.xTrain,self.yTrain=self.GetTrainData(self.listTrain[iList])

        numListTest=len(self.listTest)
        if numListTest>0:
            iList=np.random.choice(numListTest)
            self.xTest,self.yTest=self.GetTrainData(self.listTest[iList])   
            
        numListPre=len(self.listPre)
        if numListPre>0:
            iList=np.random.choice(numListPre)
            self.xPre=self.GetPreData(self.listPre[iList]) 
        

    def SetData(self,xTrain,yTrain,configXData='dx',configYData='dy',numDiffData=None):     # 原来的那个
        self.xTrain=xTrain
        self.yTrain=yTrain
        
        self.SetDataInit(configXData,configYData,numDiffData)

    
    def SetNN(self,numEpoch=10000,learningRate=0.001,batchSize=100,typeLoss='mse',typeTrain='adamoptimizer',configSession='config=tf.ConfigProto(log_device_placement=True)'):
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

    def SetPre(self,xPre=-1):
        if type(xPre)==int:      #　作为开关使用的
            if xPre==-1:         #  此时表示内部测试，即用数据内部特征测试
                if 'x+dx' in self.configXData:    #  综合前两个，意思是在当前ｍｅａｎ位置上，调到０，调幅－ｍｅａｎ
                    xMean=np.mean(self.xTrain,axis=0)[np.newaxis,:]
                    xPreTmp=np.hstack((xMean,-xMean))
                elif 'dx' in self.configXData:      # 由于ｍｅａｎ上ｘ并不是０，因此为了将ｘ－>0，需要将ｄｘ变化量为　－ｍｅａｎ
                    xMean=np.mean(self.xTrain,axis=0)[np.newaxis,:]
                    xPreTmp=-xMean
                elif 'x' in self.configXData:       #此时需要将ｘ全部校正到０，即ｘ＝０
                    xPreTmp=np.zeros((1,self.sizeInput))
                
                
                
                if self.zXPlusLen>0:
                    yMean=np.mean(self.yTrain,axis=0)
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
        self.PostProcess()
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

    def Deal4Predict(self):
        xOutMax=tf.reduce_max(self.xOut,axis=1)
        self.xOutRatio=tf.div((xOutMax-self.xOut[-1,0]),self.xOut[-1,0])
        
        
        
        
    def PostProcess(self):
        self.Deal4Predict()
    
    
    
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
            sizeInput=np.shape(xTrain)[1]*2+self.zXPlusLen-self.zXMinusLen
        elif 'dx' in self.configXData:
            sizeInput=np.shape(xTrain)[1]+self.zXPlusLen-self.zXMinusLen
        elif 'x' in self.configXData:
            sizeInput=np.shape(xTrain)[1]+self.zXPlusLen-self.zXMinusLen
        return sizeInput

    def GetSizeOutput(self):
        if 'y+dy' in  self.configYData:
            sizeOutput=np.shape(yTrain)[1]*2+self.zYPlusLen-self.zYMinusLen
        elif 'dy' in self.configYData:
            sizeOutput=np.shape(yTrain)[1]+self.zYPlusLen-self.zYMinusLen
        elif 'y' in self.configYData:
            sizeOutput=np.shape(yTrain)[1]+self.zYPlusLen-self.zYMinusLen
            
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
        x1=self.xTrain[idChoose1,:]
        x2=self.xTrain[idChoose2,:]
        y1=self.yTrain[idChoose1,:]
        y2=self.yTrain[idChoose2,:]
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
            
        return X,Y
    
    
    def ReadyData(self,xData,yData):
        idChoose=np.random.randint(0,high=self.numItem,size=(self.batchSize))
        x=xData[idChoose,:]
        y=yData[idChoose,:]
        return x,y
        

    
    
        
    def RunTrain(self):
        if self.configSession=='+':
            sess=tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
        else:
            sess=tf.InteractiveSession(self.configSession)
        sess.run(tf.global_variables_initializer())
        
        lossRec=[]
        rYAimRec=[]
        lossMeanRec=[]
        rYAimMeanRec=[] 

        
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
        
        
    def Run(self):

        if self.configSession=='+':
            sess=tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
        else:
            sess=tf.InteractiveSession(self.configSession)
        sess.run(tf.global_variables_initializer())
        
        recLossTrain=[]
        recLossTest=[]

        recLossTrainMean=[]
        recLossTestMean=[]
        
        recRYPre=[]
        recRYPreMean=[]

        
        for iEpoch in range(self.numEpoch):

            if iEpoch % self.numChangeData==self.numChangeData-1:
                self.ChangeData()


            xTrain,yTrain=self.ReadyData(self.xTrain,self.yTrain)

            sess.run(self.opt,feed_dict={self.xIn:xTrain,self.yIn:yTrain})
            
            
            

            if iEpoch % self.numRecStep==0:
                xTest,yTest=self.ReadyData(self.xTest,self.yTest)
                
                lossTrain=sess.run(self.loss,feed_dict={self.xIn:xTrain,self.yIn:yTrain})
                lossTest=sess.run(self.loss,feed_dict={self.xIn:xTest,self.yIn:yTest})
                
                
                recLossTrain.append(lossTrain)
                recLossTrainMean.append(np.mean(recLossTrain))
                
                recLossTest.append(lossTest)
                recLossTestMean.append(np.mean(recLossTest))    
                
                if len(recLossTrain)>self.numRec:
                    recLossTrain.pop(0)
                    recLossTrainMean.pop(0)
                    recLossTest.pop(0)
                    recLossTestMean.pop(0)
                
                plt.figure('loss:Train')
                plt.clf()
                plt.hold
                plt.plot(recLossTrain,'b-o')
                plt.plot(recLossTrainMean,'g-o')            
                plt.grid('on')
                plt.title(iEpoch)
                plt.pause(0.1)
                
                plt.figure('loss:Test')
                plt.clf()
                plt.hold
                plt.plot(recLossTest,'r-o')
                plt.plot(recLossTestMean,'m-o')                
                plt.grid('on')
                plt.title(iEpoch)
                plt.pause(0.1) 
                
                
                
                
                xTmp=sess.run(self.xOutRatio,feed_dict={self.xIn:xTrain,self.yIn:yTrain})
                print np.shape(xTmp)
                plt.figure('tmp')
                plt.clf()
                plt.plot(xTmp,'.')
                plt.pause(0.1) 

        
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
        

        
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

mlTrainList=['ml_0','ml_1','ml_2','ml_3','ml_4','ml_5','ml_6','ml_7','ml_8','ml_9','ml_10',\
       'ml_11','ml_12','ml_13','ml_14','ml_15','ml_16','ml_17','ml_18','ml_19','ml_20',\
       'ml_21','ml_22','ml_23','ml_24','ml_25','ml_26','ml_27','ml_28','ml_29','ml_30',\
       'ml_31','ml_32','ml_33','ml_34',\
       ]

mlTestList=['ml_35']

mlPreList=['ml']


def GetTrainData(fName):    
    X=np.loadtxt(fName+'.train')
    Y=np.loadtxt(fName+'.label')    
    return X,Y



def GetPreData(fName):
    X=np.loadtxt(fName+'.pre')
    return X

    
xTrain,yTrain=GetTrainData('ml_0')

xPre=GetPreData(mlPreList[0])



x=DL()
x.SetTrainList(mlTrainList)
x.SetTestList(mlTestList)
x.SetPreList(mlPreList)
x.SetDataConfig(configXData='dx',configYData='dy',numDiffData=None,numChangeData=2e5)

x.SetNN(numEpoch=1e6,learningRate=0.002,configSession='+')
x.AddFC(0,'relu')
x.AddFC(0,'')

x.Build()
x.SetRec()

x.Run()






















        
        
        
        









