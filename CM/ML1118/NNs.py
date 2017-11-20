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
    def __init__(self,xData,yData,xAim,numHidden,batchSize,learningRate,numEpoch,numRec,numRecStep,numPreData,configX,configY,tpyeNN,typeLoss,typeTrain,configSession):
        self.numHidden=numHidden
        self.batchSize=batchSize
        self.learningRate=learningRate
        self.numEpoch=numEpoch
        self.numRec=numRec
        self.numRecStep=numRecStep
        self.numPreData= numPreData     
        
        self.typeNN=tpyeNN.lower()
        self.typeLoss=typeLoss.lower()
        self.typeTrain=typeTrain.lower()
        
        self.configX=configX.lower()
        self.configY=configY.lower()
        self.configSession=configSession

        self.numInput=self.GetNumInput()
        self.numOutput=self.GetNumOutput()

        self.xData=xData
        self.yData=yData
        self.xAim=xAim
        
        self.xIn=tf.placeholder(tf.float32,shape=(None,self.numInput))
        self.yIn=tf.placeholder(tf.float32,shape=(None,self.numOutput))
        self.xOut=self.GetOutX()
        self.yOut=self.GetOutY()
        self.loss=self.GetLoss()
        self.train=self.GetTrain()
        self.opt=self.GetOpt()
        
        self.numItem=np.shape(self.xData)[0]
        self.xAim=self.GetAim()
        
    def GetNumInput(self):
        if self.configX=='x':
            numInput=np.shape(xData)[1]
        elif self.configX=='dx':
            numInput=np.shape(xData)[1]
        elif self.configX=='x+dx':
            numInput=np.shape(xData)[1]*2

        return numInput

    def GetNumOutput(self):
        if self.configY=='y':
            numOutput=np.shape(yData)[1]
        elif self.configY=='dy':
            numOutput=np.shape(yData)[1]
        elif self.configY=='y+dy':
            numOutput=np.shape(yData)[1]*2        
        return numOutput        
    
    def GenWeight(self,shape):
        initial = tf.truncated_normal(shape, stddev=1.)
        return tf.Variable(initial)
    def GenBias(self,shape):
        initial=self.GenWeight((1,shape(0)))
        return initial[0,:]
            
    def GetOutX(self):
        if self.typeNN=='matrix':
            xOut= self.Matrix()
        if self.typeNN=='fc':
            pass
        if self.typeNN=='cnn1D':
            pass
        if self.typeNN=='cnn2D':
            pass    
        if self.typeNN=='rnn':
            pass    
        return xOut
    def GetOutY(self):
        yOut=self.yIn
        return yOut

    def Matrix(self):
        shapeM=(self.numInput,self.numOutput)
        M=self.GenWeight(shapeM)
        xOut=tf.matmul(self.xIn,M)
        return xOut
        
    def GetLoss(self):
        if self.typeLoss=='mse':
            loss=tf.losses.mean_squared_error(self.xOut,self.yOut)
        return loss
            
    def GetTrain(self):
        if self.typeTrain=='adamoptimizer':
            train=tf.train.AdamOptimizer(self.learningRate)
        return train
    
    def GetOpt(self):
        opt=self.train.minimize(self.loss)
        return opt

    def GetAim(self):
        if xAim==-1:     # rms -> Correct
            if self.configX=='x':
                xAim4Pre=np.zeros((1,self.numInput))
            if self.configX=='dx':
                xMean=np.mean(self.xData,axis=0)[np.newaxis,:]
                xAim4Pre=-xMean
            if self.configX=='x+dx':
                xMean=np.mean(self.xData,axis=0)[np.newaxis,:]
                xAim4Pre_x=xMean
                xAim4Pre_dx=-xMean
                xAim4Pre=np.hstack((xAim4Pre_x,xAim4Pre_dx))
                
        return xAim4Pre
                    

    def PreData(self):
        idChoose2=np.random.randint(0,high=self.numItem,size=(self.batchSize))
        if self.numPreData==None:
            idChoose1=np.random.randint(0,high=self.numItem,size=(self.batchSize))
        else:
            idChoose1=idChoose2-self.numPreData
        x1=self.xData[idChoose1,:]
        x2=self.xData[idChoose2,:]
        y1=self.yData[idChoose1,:]
        y2=self.yData[idChoose2,:]
        dx=x2-x1
        dy=y2-y1
        if self.configX=='x':
            X=x1
        elif self.configX=='dx':
            X=dx
        elif self.configX=='x+dx':
            X=np.hstack((x1,dx))
            
        if self.configY=='y':
            Y=y1
        elif self.configY=='dy':
            Y=dy
        elif self.configY=='y+dy':
            Y=np.hstack((y1,dy))
        return X,Y
        

    def Train(self):
        if self.configSession=='':
            sess=tf.Session()
        else:
            sess=tf.Session(self.configSession)
        sess.run(tf.global_variables_initializer())
        
        lossRec=[]
        rYAimRec=[]
        for iEpoch in range(self.numEpoch):
            X,Y=self.PreData()
            sess.run(self.opt,feed_dict={self.xIn:X,self.yIn:Y})
            
            if iEpoch % self.numRecStep==0:
                lossNow=sess.run(self.loss,feed_dict={self.xIn:X,self.yIn:Y})
                lossRec.append(lossNow)

                yAim=sess.run(self.xOut,feed_dict={self.xIn:self.xAim})[0]
                rYAim=np.sum(np.square(yAim))
                rYAimRec.append(rYAim)
                
                if len(lossRec)>self.numRec:
                    lossRec.pop(0)
                    rYAimRec.pop(0)
                
                
                plt.figure('loss')
                plt.clf()
                plt.plot(lossRec,'-o')
                plt.grid('on')
                plt.title(iEpoch)
                plt.pause(0.01)
                
                plt.figure('rYAim')
                plt.clf()
                plt.plot(rYAimRec,'-o')
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
xAim=-1
numHidden=0
batchSize=100
learningRate=0.001
numEpoch=50000
numRec=50
numRecStep=50
numPreData=1
configX='x+dx'
configY='y'
tpyeNN='Matrix'
typeLoss='mse'
typeTrain='AdamOptimizer'
configSession=''




x=DL(xData,yData,xAim,numHidden,batchSize,learningRate,numEpoch,numRec,numRecStep,numPreData,configX,configY,tpyeNN,typeLoss,typeTrain,configSession)

x.Train()

















