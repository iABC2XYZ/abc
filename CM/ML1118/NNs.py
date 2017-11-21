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
    def __init__(self,xData,yData,xAim,numHidden,batchSize,learningRate,numEpoch,numRec,numRecStep,numPreData,configX,configY,tpyeNN,typeAct,typeLoss,typeTrain,configSession):
        self.numHidden=self.GetNumHidden(numHidden)
        self.batchSize=batchSize
        self.learningRate=learningRate
        self.numEpoch=numEpoch
        self.numRec=numRec
        self.numRecStep=numRecStep
        self.numPreData= numPreData     
        
        self.typeNN=tpyeNN.lower()
        self.typeAct=typeAct.lower()
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
    
    def GetNumHidden(self,numHidden):
        try:
            if 0 in numHidden:
                numHidden.pop(numHidden.index(0))
            
        except:
            if numHidden==0:
                numHidden=[]
            else:
                numHidden=[numHidden]
        return numHidden
            
        

    
    def GenWeight(self,shape):
        initial = tf.truncated_normal(shape, stddev=1.)
        return tf.Variable(initial)
    def GenBias(self,size):
        initial=self.GenWeight((1,size))
        return initial[0,:]
            
    def GetOutX(self):
        if self.typeNN=='matrix':
            xOut= self.Matrix()
        if self.typeNN=='fc':
            xOut=self.FC()
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

    def FC(self):
        sizeLayer=self.numHidden
        sizeLayer.insert(0,self.numInput)
        sizeLayer.append(self.numOutput)
        
        numLayer=len(sizeLayer)
        
        wRec=[]
        bRec=[]
        for iLayer in range(numLayer-1):
            if iLayer==0:
                X=self.xIn
            numIn=np.int32(sizeLayer[iLayer])
            numOut=np.int32(sizeLayer[iLayer+1])
            w=self.GenWeight((numIn,numOut))
            b=self.GenBias(numOut)
            wRec.append(w)
            bRec.append(b)
            X=tf.nn.xw_plus_b(X,w,b)
            
            if iLayer < numLayer-2:
                X=self.Act(X)
                
        xOut=X

        return xOut
                
                
    def Act(self,X):
        if self.typeAct=='relu':
            xAct=tf.nn.relu(X)
        if self.typeAct=='relu6':
            xAct=tf.nn.relu6(X)
        if self.typeAct=='sigmoid':
            xAct=tf.nn.sigmoid(X)
        if self.typeAct=='tanh':
            xAct=tf.nn.tanh(X)
        if self.typeAct=='elu':
            xAct=tf.nn.elu(X)
        if self.typeAct=='softplus':
            xAct=tf.nn.softplus(X)
        if self.typeAct=='softsign':
            xAct=tf.nn.softsign(X)
        return xAct
    
    

    def Matrix(self):
        shapeM=(self.numInput,self.numOutput)
        M=self.GenWeight(shapeM)
        xOut=tf.matmul(self.xIn,M)
        return xOut
        
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

                yAim=sess.run(self.xOut,feed_dict={self.xIn:self.xAim})[0]
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
numHidden=10
batchSize=100
learningRate=0.001
numEpoch=50000
numRec=50
numRecStep=50
numPreData=1
configX='x+dx'
configY='y'
tpyeNN='fc'
typeAct='relu'
typeLoss='mse'
typeTrain='AdamOptimizer'
configSession=''




x=DL(xData,yData,xAim,numHidden,batchSize,learningRate,numEpoch,numRec,numRecStep,numPreData,configX,configY,tpyeNN,typeAct,typeLoss,typeTrain,configSession)

x.FC()

x.Train()




















