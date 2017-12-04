#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 23:43:20 2017

@author: p
"""

import numpy as np

import tensorflow as tf
import matplotlib.pyplot as plt
import os
import subprocess

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


    def SetDataInit(self):
        self.numItem=np.shape(self.xTrain)[0]
        
        with tf.name_scope('Input'):
            self.xIn=tf.placeholder(tf.float32,shape=(None,self.sizeInput),name='xInput')
            self.yIn=tf.placeholder(tf.float32,shape=(None,self.sizeOutput),name='xInput')
        
        self.numOutputLayer4FC=self.sizeInput       #会记录上次的sizeOutput,它可以由D1_in_channels生成。
        
        self.D1_in_channels=0       #会记录上次的D1_ｏｕｔ_channels

        
    def GetTrainData(self,fName):    
        X=np.loadtxt(fName+'.train')
        Y=np.loadtxt(fName+'.label')    
        return X,Y
    
    def GetPreData(self,fName):
        X=np.loadtxt(fName+'.pre')
        return X


    def SetDataConfig(self,numChangeData=None):
        self.xTrain,self.yTrain=self.GetTrainData(self.listTrain[0])
        self.xTest,self.yTest=self.GetTrainData(self.listTest[0])
        self.xPre=self.GetPreData(self.listPre[0])
        
        self.sizeInput=np.shape(self.xTrain)[1]
        self.sizeOutput=np.shape(self.yTrain)[1]
        
        if numChangeData==None:
            self.numChangeData=4000
        else:
            self.numChangeData=numChangeData
            
        if self.numChangeData<0:
            self.listTrain.pop(0)
            self.listTest.pop(0)
            self.listPre.pop(0)
        
        self.SetDataInit()


    def ChangeData_X(self,listX,flagType):
        numX=len(listX)
        if flagType.lower()=='train':
            if numX>1:
                iList=np.random.choice(numX)
                x,y=self.GetTrainData(listX[iList])
                if self.numChangeData<0:
                    listX.pop(iList)
                    x=np.vstack((self.xTrain,x))
                    y=np.vstack((self.yTrain,y))
                return x,y
            else:
                return self.xTrain,self.yTrain
        
        if flagType.lower()=='test':
            if numX>1:
                iList=np.random.choice(numX)
    
                x,y=self.GetTrainData(listX[iList])
                if self.numChangeData<0:
                    listX.pop(iList)
                    x=np.vstack((self.xTest,x))
                    y=np.vstack((self.yTest,y))
                return x,y
            else:
                return self.xTest,self.yTest
        
        if flagType.lower()=='pre':
            if numX>1:
                iList=np.random.choice(numX)
                x=self.GetPreData(listX[iList])
                if self.numChangeData<0:
                    listX.pop(iList)
                    x=np.vstack((self.xPre,x))
                return x
            else:
                return self.xPre
    
    def ChangeData(self):

        self.xTrain,self.yTrain=self.ChangeData_X(self.listTrain,flagType='train')
        self.numItem=np.shape(self.xTrain)[0]
        self.xTest,self.yTest=self.ChangeData_X(self.listTest,flagType='test')
        self.xPre=self.ChangeData_X(self.listPre,flagType='pre')

    


    
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

  
    def Build(self):
        self.GetOutX()
        self.GetOutY()
        self.PostProcess()
        self.GetLoss()
        self.GetTrain()
        self.GetOpt()        



    def GetOutX(self):
        with tf.name_scope('xOut'):
            self.xOut=self.X
    def GetOutY(self):
        with tf.name_scope('yOut'):
            self.yOut=self.yIn

    def GetLoss(self):
        with tf.name_scope('loss'):
            if self.typeLoss=='mse':
                self.loss=tf.losses.mean_squared_error(self.xOut,self.yOut)
            if self.typeLoss=='cross_entropy':
                xSoft=tf.nn.softmax(self.xOut)
                ySoft=tf.nn.softmax(self.yOut)
                self.loss=-tf.reduce_mean(xSoft*tf.log(ySoft))
            if self.typeLoss=='mseratio':
                diffXY=self.xOut-self.yOut
                ratioXY=tf.div(diffXY,self.yOut)
                self.loss=tf.reduce_sum(tf.square(ratioXY))/self.batchSize
                

                
    def Deal4Predict(self):
        xOutMax=tf.reduce_max(self.xOut,axis=1)
        self.xOutRatio=tf.div((xOutMax-self.xOut[-1,0]),self.xOut[-1,0])
        
        
        
        
    def PostProcess(self):
        with tf.name_scope('postProcess'):
            self.Deal4Predict()
    
    
    
    def GetTrain(self):
        with tf.name_scope('train'):
            if self.typeTrain=='adamoptimizer':
                self.train=tf.train.AdamOptimizer(self.learningRate)

    
    def GetOpt(self):
        with tf.name_scope('optimizer'):
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


    def GenWeight(self,shape):
        with tf.name_scope("weight"):
            initial = tf.truncated_normal(shape, stddev=1.)
            return tf.Variable(initial)
    def GenBias(self,size):
        with tf.name_scope("bias"):
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
        if typeAct=='dropout_cnn':
            xAct=tf.nn.dropout(X,0.5)
        
        return xAct


    
    def ReadyData(self,xData,yData):
        

        idChoose=np.random.randint(0,high=np.shape(xData)[0],size=(self.batchSize))
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
        
    def SetRunPredict(self,numRunPreStep=5000):
        self.numRunPreStep=numRunPreStep
    
    def Run(self):

        if self.configSession=='+':
            sess=tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
        else:
            sess=tf.InteractiveSession(self.configSession)
          

        writer=tf.summary.FileWriter("logs/",sess.graph)
            
        sess.run(tf.global_variables_initializer())
        
        recLossTrain=[]
        recLossTest=[]

        recLossTrainMean=[]
        recLossTestMean=[]
        
        recRYPre=[]
        recRYPreMean=[]


        for iEpoch in range(self.numEpoch):
            if iEpoch==10:
                print "*"*8
                subprocess.call('tensorboard --logdir="logs/"')
                print "="*8
            

            if iEpoch % np.abs(self.numChangeData)==np.abs(self.numChangeData)-1:
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
                plt.pause(0.01)
                
                plt.figure('loss:Test')
                plt.clf()
                plt.hold
                plt.plot(recLossTest,'r-o')
                plt.plot(recLossTestMean,'m-o')                
                plt.grid('on')
                plt.title(iEpoch)
                plt.pause(0.01) 
                
            if iEpoch % self.numRunPreStep==self.numRunPreStep-1:
                
                yPre=sess.run(self.xOut,feed_dict={self.xIn:self.xPre})
                yPre0=np.matmul(self.xPre[:,-3].reshape(-1,1),np.ones((1,np.shape(yPre)[1])))  # -3: high
                
                yPreRatio=(yPre-yPre0)/yPre0
                
                fid=open('Ratio.pre','w+')
                for iYPreRatio in yPreRatio:
                    for jYPreRatio in iYPreRatio:
                        fid.writelines('%.5f '%jYPreRatio)
                    fid.writelines('\n')
                fid.close()
                
                yFit=yPreRatio.T
                xFit=np.linspace(0,1,np.shape(yFit)[0])
                pFit=np.polyfit(xFit,yFit,1)
                kFit=pFit[0,:]
                
                numFitChoose=50
                kFitChoose=[]
                kFit_=np.copy(kFit)
                for iFit in range(numFitChoose):
                    argMax=np.argmax(kFit_)
                    kFit_[argMax]=0.
                    kFitChoose.append(argMax)
                
                xPreChoose=self.xPre[kFitChoose,2::5]
                yPreChoose=yPre[kFitChoose,:]
                allPreChoose=np.hstack((xPreChoose,yPreChoose))
                plt.figure('allPreChoose')
                plt.clf()
                plt.plot(allPreChoose.T)
                plt.pause(0.01)
                
                fidRead=open('ml.code','r')
                fid=open('ml.code.Choose','w+')
                iFitChoose=0
                for iRead in fidRead:
                    if iFitChoose in kFitChoose:
                        fid.writelines(iRead)
                    iFitChoose+=1
                
                fidRead.close()
                fid.close()
    
       
                rYPreRatio=np.std(yPreRatio)
                               
                recRYPre.append(rYPreRatio)
                recRYPreMean.append(np.mean(recRYPre))
                
                if len(recRYPre)>self.numRec:
                    recRYPre.pop(0)
                    recRYPreMean.pop(0)                
                
                plt.figure('PRE Y')
                plt.clf()
                plt.plot(yPre.T)
                plt.title(iEpoch)
                plt.pause(0.01)
                
                plt.figure('PRE Ratio')
                plt.clf()
                plt.plot(yPreRatio.T)
                plt.title(iEpoch)
                plt.pause(0.01)
                
                plt.figure('PRE R')
                plt.clf()
                plt.hold
                plt.plot(recRYPre)
                plt.plot(recRYPreMean)
                plt.title(iEpoch)
                plt.pause(0.01)                
                                
                
                ##
                xyPre=np.hstack((self.xPre[:,2::5],yPre))
                plt.figure('PRE ALL')
                plt.clf()
                plt.hold
                plt.plot(xyPre[0:3,:].T)
                plt.title(iEpoch)
                plt.pause(0.01)                
                
                xyPreMean=np.mean(xyPre,0)
                plt.figure('PRE ALL Mean')
                plt.clf()
                plt.hold
                plt.plot(xyPreMean)
                plt.title(iEpoch)
                plt.pause(0.01)                                                  

        
    def AddFC(self,numOutputLayer,typeAct=''):
        with tf.name_scope('FC'):
            if numOutputLayer==0:
                numOutputLayer=self.sizeOutput
            
            w=self.GenWeight((self.numOutputLayer4FC,numOutputLayer))
            b=self.GenBias(numOutputLayer)
            X=tf.nn.xw_plus_b(self.X,w,b)
            self.X=self.Act(X,typeAct)
            
            self.numOutputLayer4FC=numOutputLayer
            
    def AddMatrix(self):
        with tf.name_scope('Matrix'):
            w=self.GenWeight((self.sizeInput,self.sizeOutput))
            self.X=tf.matmul(self.X,w)
            
          

    def conv1d(self,x, W,stride, padding):
        return tf.nn.conv1d(x,W,stride, padding)
    
    def AddCNN1D(self,D1_filter_width, D1_out_channels, D1_in_channels=0,typeAct='',stride=1, padding="SAME",reshape=0):
        with tf.name_scope('CNN1D'):
        
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
            
        
    def AddCNN1D_MultiChannel(self,D1_filter_width, D1_out_channels, D1_in_channels=0,typeAct='',stride=1, padding="SAME",reshape=0):
        with tf.name_scope('CNN1D__MultiChannel'):
            if D1_in_channels==0 and self.D1_in_channels==0:
                self.X=tf.expand_dims(self.X, -1)
                self.D1_in_channels=1
            
            if D1_in_channels!=0:
                self.D1_in_channels=D1_in_channels
                
            if len(D1_filter_width)==1:
                D1_out_channelsNow=D1_out_channels[0]
                w=self.GenWeight((D1_filter_width[0], self.D1_in_channels, D1_out_channelsNow))
                b=self.GenBias((D1_out_channelsNow))
                X=self.conv1d(self.X,w,stride, padding)+b
                XAct=self.Act(X,typeAct) 
                
                D1_out_channels_=D1_out_channelsNow
                
            if len(D1_filter_width)>1:
                    
                XActList=[]
                D1_out_channelsList=[]
                D1_out_channels_=0
                
                for iNow in range(len(D1_filter_width)):
                    
                    D1_filter_widthNow=D1_filter_width[iNow]

                    if len(D1_out_channels)==1:
                        D1_out_channelsNow=D1_out_channels[0]
                    if len(D1_out_channels)>1:
                        D1_out_channelsNow=D1_out_channels[iNow]
                        
                    D1_out_channels_+=D1_out_channelsNow
                        
                    D1_out_channelsList.append(D1_out_channelsNow)
                    
                    wNow=self.GenWeight((D1_filter_widthNow,self.D1_in_channels, D1_out_channelsNow))
                    bNow=self.GenBias((D1_out_channelsNow))
                    XNow=self.conv1d(self.X,wNow,stride, padding)+bNow
                    XActNow=self.Act(XNow,typeAct)

                    XActList.append(XActNow)
                    
                    
                for iNow in range(len(D1_filter_width)):
                    if iNow==0:
                        XAct=XActList[iNow]
                    else:
                        XActTmp=XActList[iNow]
                        
                        XAct=tf.concat((XAct,XActTmp),axis=2)
                    
  
            
            if reshape==1:
                self.numOutputLayer4FC=self.numOutputLayer4FC*D1_out_channels_
                XAct=tf.reshape(XAct,(-1,self.numOutputLayer4FC))
            
            self.X=XAct
                
            
            self.D1_in_channels=D1_out_channels_


    def SetDataList(self,mlTrainList,mlTestList,mlPreList,numChangeData=-2000):
        self.SetTrainList(mlTrainList)
        self.SetTestList(mlTestList)
        self.SetPreList(mlPreList)
        self.SetDataConfig(numChangeData)
        
    
        

        
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
        
os.system('rm -fr ./logs')
        

mlTrainList=['ml_0','ml_1','ml_2','ml_3','ml_4','ml_5','ml_6','ml_7','ml_8','ml_9','ml_10',\
       'ml_11','ml_12','ml_13','ml_14','ml_15','ml_16','ml_17','ml_18','ml_19','ml_20',\
       'ml_21','ml_22','ml_23','ml_24','ml_25','ml_26','ml_27','ml_28','ml_29','ml_30',\
       'ml_31','ml_32','ml_33','ml_34',\
       ]

mlTestList=['ml_35']

mlPreList=['ml']


x=DL()

x.SetDataList(mlTrainList,mlTestList,mlPreList,numChangeData=-2000)



x.SetNN(numEpoch=1e8,learningRate=0.005,batchSize=80,typeLoss='mseRatio',configSession='+')
x.AddCNN1D_MultiChannel(D1_filter_width=[8,5], D1_out_channels=[10], D1_in_channels=0,typeAct='tanh',stride=1, padding="SAME",reshape=0)
x.AddCNN1D(D1_filter_width=8, D1_out_channels=10, D1_in_channels=0,typeAct='tanh',stride=1, padding="SAME",reshape=0)
x.AddCNN1D(D1_filter_width=8, D1_out_channels=10, D1_in_channels=0,typeAct='tanh',stride=1, padding="SAME",reshape=0)
x.AddCNN1D(D1_filter_width=8, D1_out_channels=10, D1_in_channels=0,typeAct='tanh',stride=1, padding="SAME",reshape=1)
x.AddFC(40,'dropout_cnn')
x.AddFC(0,'')
#x.AddMatrix()

x.Build()
x.SetRec(numRec=100,numRecStep=100)
x.SetRunPredict(numRunPreStep=5000)


x.Run()






















        
        
        
        









