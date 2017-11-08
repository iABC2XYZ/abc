#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：


"""

import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt

plt.close('all')

def GenWeight(shape):
    initial = tf.truncated_normal(shape, stddev=1.)
    return tf.Variable(initial)
def GenBias(shape):
    initial = tf.constant(1., shape=shape)
    return tf.Variable(initial)

def MatMul(X):
    numX=len(X)
    Y=X[0]
    for i in xrange(1,numX):
        Y=np.matmul(Y,X[i])
    return Y


def MatResponse(wResponse,numInput,numOutput):
    U, s, V=np.linalg.svd(wResponse)
    S=np.vstack((np.diag(s),np.zeros((numInput-numOutput,numOutput))))
    S_1=np.hstack((np.diag(1/s),np.zeros((numOutput,numInput-numOutput))))
    
    wResponseSolve=MatMul((V.T,S_1,U.T))
    return wResponseSolve


def getDataRow(exData,sizeRow,):
    numEx=np.shape(exData)[0]
    idChoose1=np.random.randint(0,high=numEx,size=(sizeRow))
    idChoose2=np.random.randint(0,high=numEx,size=(sizeRow))
    xCHV1=np.reshape(exData[idChoose1,0:14],(sizeRow,14))
    yBPM1=np.reshape(exData[idChoose1,14:24],(sizeRow,10))
    xCHV2=np.reshape(exData[idChoose2,0:14],(sizeRow,14))
    yBPM2=np.reshape(exData[idChoose2,14:24],(sizeRow,10))
    X=yBPM1-yBPM2
    Y=xCHV1-xCHV2
    return X,Y


nameFolder='/home/node1/Templates/ABC/abc/BPM/Paper/'
try:

    nameData=nameFolder+'Rec_1106_2046.dat'
    nameDataBK=nameFolder+'Rec_1106_2046.dat.bk'
    exData=np.loadtxt(nameData)
except:

    nameData=nameFolder+'Rec_1106_2046.dat'
    nameDataBK=nameFolder+'Rec_1106_2046.dat.bk'
    if not os.path.exists(nameDataBK):
        os.system('cp '+nameData+' '+nameDataBK)
    
    fidWrite=open(nameData,'w+')
    with open(nameDataBK) as fid:
        for line in fid:
            line=line.strip("\n")
            line=line.expandtabs()
            line=line.strip()
            
            lineWrite=''
            idSpace=line.find(' ')

            for iRec in xrange(24):
                lineChoose=line[0:idSpace].strip()
                
                line=line[idSpace::]
                line=line.strip()
                idSpace=line.find(' ')
                
                lineWrite+=lineChoose+' '
              
            lineWrite+='\n'
            fidWrite.writelines(lineWrite)
     
    fidWrite.close()
    exData=np.loadtxt(nameData)



numInput=14
numOutput=10

numEpoch=2e7
numBatch=100
numPlot=80
numPlotStep=100
learningRate=5e-5


#
xInput=tf.placeholder(tf.float32,shape=(None,numInput))
yInput=tf.placeholder(tf.float32,shape=(None,numOutput))

#

w1= GenWeight([numInput,numOutput])
x1=tf.matmul(xInput,w1)


#
xFinal=x1

#
xOutput=tf.reshape(xFinal,(-1,numOutput))
yOutput=tf.reshape(yInput,(-1,numOutput))


lossFn=tf.sqrt(tf.losses.mean_squared_error(xOutput,yOutput))     


trainBPM=tf.train.AdamOptimizer(learningRate)
optBPM=trainBPM.minimize(lossFn)

iniBPM=tf.global_variables_initializer()


try:
    if vars().has_key('se'):
        se.close()
except:
    pass
se= tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
se.run(iniBPM)

lossRec=[]
lossRecMean=[]

for iEpoch in range(np.int32(numEpoch)):
    yBPM,xCHV=getDataRow(exData,numBatch)
    se.run(optBPM,feed_dict={xInput:xCHV,yInput:yBPM})
    
    if iEpoch % numPlotStep==0:
        lossRecTmp=se.run(lossFn,feed_dict={xInput:xCHV,yInput:yBPM})
        lossRec.append(lossRecTmp)
        lossRecMean.append(np.mean(lossRec))
        if len(lossRec)>numPlot:
            lossRec.pop(0)
            lossRecMean.pop(0)

        
        plt.figure('loss')
        plt.clf()
        plt.plot(lossRec,'b')
        plt.plot(lossRecMean,'r')
        plt.title(iEpoch)
        plt.grid('on')
        plt.pause(0.01)
    
        
        
        xCHV=np.ones((1,numInput))

        #yBPMEx=np.array([0,0,0,0,0,0,0,0,0,0])[:,np.newaxis].T
        xCHVEx=se.run(xOutput,feed_dict={xInput:xCHV})
        rxCHVEx=np.sqrt(np.sum(xCHVEx**2))
        if not vars().has_key('rxCHVExRec'):
            rxCHVExRec=[]
        else:
            rxCHVExRec.append(rxCHVEx)
        if len(rxCHVExRec)>numPlot:
            rxCHVExRec.pop(0)
        
        plt.figure('rxCHVExRec')
        plt.clf()
        plt.plot(rxCHVExRec,'b')
        plt.title(iEpoch)
        plt.grid('on')
        plt.pause(0.01)
        
        plt.figure('Ex')
        if iEpoch % numPlotStep*5==0:
            plt.clf()
        plt.hold('on')
        plt.plot(xCHVEx.T,'b*')
        plt.title(iEpoch)
        plt.grid('on')
        plt.pause(0.01)
        
        
        wSum=np.sum(se.run(w1))
        if not vars().has_key('wRec'):
            wRec=[]
        else:
            wRec.append(wSum)
        if len(wRec)>numPlot:
            wRec.pop(0)
        plt.figure('w')
        plt.clf()
        plt.plot(wRec,'b')
        plt.title(iEpoch)
        plt.grid('on')
        plt.pause(0.01)

        xBPMEx=np.array([0,1.56824205393,3.11142945232,3.86897583945,4.66700936151,0,2.09661528113,1.15367116991,1.12618083973,2.16402881327])[:,np.newaxis].T
        wResponse=se.run(w1)        
        wResponseSolve=MatResponse(wResponse,numInput,numOutput)
        yCHV=MatMul((xBPMEx,wResponseSolve))

        plt.figure('Ex - Inv')
        if iEpoch % numPlotStep*5==0:
            plt.clf()
        plt.hold('on')
        plt.plot(yCHV.T,'b*')
        plt.title(iEpoch)
        plt.grid('on')
        plt.pause(0.01)







