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



def getDataRow(exData,sizeRow,):
    numEx=np.shape(exData)[0]
    idChoose1=np.random.randint(0,high=numEx,size=(sizeRow))
    idChoose2=np.random.randint(0,high=numEx,size=(sizeRow))
    idChoose2[0]=idChoose1[0]
    yCHV1=np.reshape(exData[idChoose1,0:14],(sizeRow,14))
    xBPM1=np.reshape(exData[idChoose1,14:24],(sizeRow,10))
    yCHV2=np.reshape(exData[idChoose2,0:14],(sizeRow,14))
    xBPM2=np.reshape(exData[idChoose2,14:24],(sizeRow,10))

    X=np.hstack((xBPM1,yCHV1,xBPM2))
    Y=yCHV2
    
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

#numExUse=100
#exData=exData[np.random.randint(0,high=np.shape(exData)[0],size=(numExUse)),:]

numInput=34
numOutput=14

numEpoch=2e7
numBatch=100
numPlot=80
numPlotStep=100
learningRate=1e-4


#
xInput=tf.placeholder(tf.float32,shape=(None,numInput))
yInput=tf.placeholder(tf.float32,shape=(None,numOutput))

#
numX1=100
w1= GenWeight([numInput,numX1])
b1=GenBias([numX1])
x1=tf.nn.relu6(tf.nn.xw_plus_b(xInput,w1,b1))

#
numX2=40
w2= GenWeight([numX1,numX2])
b2=GenBias([numX2])
x2=tf.nn.relu6(tf.nn.xw_plus_b(x1,w2,b2))

#
numX3=40
w3= GenWeight([numX2,numX3])
b3=GenBias([numX3])
x3=tf.nn.relu6(tf.nn.xw_plus_b(x2,w3,b3))

#
w4= GenWeight([numX3,numOutput])
b4=GenBias([numOutput])
x4=tf.nn.xw_plus_b(x3,w4,b4)


##
wNN= GenWeight([numInput,numOutput])
bNN=GenBias([numOutput])
xNN=tf.matmul(xInput,wNN)+bNN



#
xFinal=xNN

#
xOutput=tf.reshape(xFinal,(-1,numOutput))
yOutput=tf.reshape(yInput,(-1,numOutput))


lossFnMSE=tf.sqrt(tf.losses.mean_squared_error(xOutput,yOutput))     
lossFn0=tf.reduce_sum(tf.square((xOutput[0,:])))  
lossFn=lossFnMSE+lossFn0


trainBPM=tf.train.AdamOptimizer(learningRate)
optBPM=trainBPM.minimize(lossFn)

iniBPM=tf.global_variables_initializer()


try:
    if vars().has_key('se'):
        se.close()
except:
    pass
se= tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
#se= tf.InteractiveSession()
se.run(iniBPM)

lossRec=[]
lossRecMean=[]

for iEpoch in range(np.int32(numEpoch)):
    xBPM,yCHV=getDataRow(exData,numBatch)
    se.run(optBPM,feed_dict={xInput:xBPM,yInput:yCHV})
   
    if iEpoch % numPlotStep==0:
        lossRecTmp=se.run(lossFn,feed_dict={xInput:xBPM,yInput:yCHV})
        print lossRecTmp
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
    
        
        
        xBPM1Ex_1=[[1.86,-1.57,-3.11,-3.87,-4.67,-1.38,-2.1,-1.15,-1.13,-2.16]]
        yCHV1Ex_1=np.zeros((1,numOutput))
        xBPM2Ex_1=[[1.86,0,0,0,0,-1.38,0,0,0,0]]

        xBPM1Ex_2=[[1.86,-1.57,-3.11,-3.87,-4.67,-1.38,-2.1,-1.15,-1.13,-2.16]]
        yCHV1Ex_2=np.zeros((1,numOutput))
        xBPM2Ex_2=[[1.86,-1.57,-3.11,-3.87,-4.67,-1.38,-2.1,-1.15,-1.13,-2.16]]      

        
        xBPM1Ex_3=[[1.86,-1.57,-3.11,-3.87,-4.67,-1.38,-2.1,-1.15,-1.13,-2.16]]
        yCHV1Ex_3=np.zeros((1,numOutput))
        xBPM2Ex_3=[[1.86,0,0,0,0,-1.38,0,0,0,0]]   

        x_Ex_1=np.hstack((xBPM1Ex_1,yCHV1Ex_1,xBPM2Ex_1))
        x_Ex_2=np.hstack((xBPM1Ex_2,yCHV1Ex_2,xBPM2Ex_2))
        x_Ex=np.vstack((x_Ex_1,x_Ex_2))

        y_Ex=se.run(xOutput,feed_dict={xInput:x_Ex})
        y_Ex_1=y_Ex[0,:]-yCHV1Ex_1
        y_Ex_2=y_Ex[1,:]-yCHV1Ex_2
        
  
        plt.figure('Ex')
        if iEpoch % numPlotStep*5==0:
            plt.clf()
        plt.hold('on')
        plt.plot(y_Ex_1.T,'b-*')
        plt.plot(y_Ex_2.T,'r-*')
        plt.title(iEpoch)
        plt.grid('on')
        plt.pause(0.01)
        
        wSum=np.sum(np.square(se.run(wNN)))
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





