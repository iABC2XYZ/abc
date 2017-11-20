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

def GenWeight(shape):
    initial = tf.truncated_normal(shape, stddev=1.)
    return tf.Variable(initial)
def GenBias(shape):
    initial = tf.constant(1., shape=shape)
    return tf.Variable(initial)



def getDataRow(exData,sizeRow,):
    numEx=np.shape(exData)[0]
    idChoose1=np.random.randint(0,high=numEx,size=(sizeRow))
    idChoose2=np.random.randint(0,high=numEx,size=(sizeRow))
    yCHV1=np.reshape(exData[idChoose1,0:14],(sizeRow,14))
    xBPM1=np.reshape(exData[idChoose1,14:24],(sizeRow,10))
    yCHV2=np.reshape(exData[idChoose2,0:14],(sizeRow,14))
    xBPM2=np.reshape(exData[idChoose2,14:24],(sizeRow,10))
    X=xBPM1-xBPM2
    Y=yCHV1-yCHV2
    return X,Y


nameFolder='/home/e/ABC/abc/BPM/Paper/'
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



numInput=10
numOutput=14

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
    xBPM,yCHV=getDataRow(exData,numBatch)
    se.run(optBPM,feed_dict={xInput:xBPM,yInput:yCHV})
    
    if iEpoch % numPlotStep==0:
        lossRecTmp=se.run(lossFn,feed_dict={xInput:xBPM,yInput:yCHV})
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
    
        
        #xBPMEx=np.array([0,-2,-2,-2,-2,0,1,1,1,1])[:,np.newaxis].T
        xBPMEx=np.array([0,1.56824205393,3.11142945232,3.86897583945,4.66700936151,0,2.09661528113,1.15367116991,1.12618083973,2.16402881327])[:,np.newaxis].T

        #xBPMEx=np.array([0,0,0,0,0,0,0,0,0,0])[:,np.newaxis].T
        yCHVEx=se.run(xOutput,feed_dict={xInput:xBPMEx})
        rYCHVEx=np.sqrt(np.sum(yCHVEx**2))
        if not vars().has_key('rYCHVExRec'):
            rYCHVExRec=[]
        else:
            rYCHVExRec.append(rYCHVEx)
        if len(rYCHVExRec)>numPlot:
            rYCHVExRec.pop(0)
        
        plt.figure('rYCHVExRec')
        plt.clf()
        plt.plot(rYCHVExRec,'b')
        plt.title(iEpoch)
        plt.grid('on')
        plt.pause(0.01)
        
        plt.figure('Ex')
        if iEpoch % numPlotStep*5==0:
            plt.clf()
        plt.hold('on')
        plt.plot(yCHVEx.T,'b*')
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


np.savetxt('w.dat',se.run(w1))


