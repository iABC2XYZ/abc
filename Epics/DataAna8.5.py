#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:44:34 2017

@author: p
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

plt.close('all')

def GenWeight(shape):
    initial = tf.truncated_normal(shape, stddev=1.)
    return tf.Variable(initial)
def GenBias(shape):
    initial = tf.constant(1., shape=shape)
    return tf.Variable(initial)



def getDataRow(exData,sizeRow):
    numEx=np.shape(exData)[0]
    idChoose1=np.random.randint(1,high=numEx,size=(sizeRow))
    idChoose2=idChoose1-1
    yCHV1=np.reshape(exData[idChoose1,0:14],(sizeRow,7,2))
    xBPM1=np.reshape(exData[idChoose1,14:24],(sizeRow,5,2))
    yCHV2=np.reshape(exData[idChoose2,0:14],(sizeRow,7,2))
    xBPM2=np.reshape(exData[idChoose2,14:24],(sizeRow,5,2))
    yCHV=yCHV1-yCHV2
    xBPM=xBPM1-xBPM2
    return xBPM,yCHV



def conv1d(x, W):
    return tf.nn.conv1d(x, W, stride=1, padding="SAME")

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding="SAME")



exData=np.loadtxt('/home/e/ABC/abc/Epics/Rec.dat')


bpm=tf.placeholder(tf.float32,shape=(None,5,2))
cHV=tf.placeholder(tf.float32,shape=(None,7,2))


xInput=bpm
yInput=cHV

#
nChan1=200

w1= GenWeight([1,2,nChan1])
b1=GenBias([nChan1])
x1=tf.nn.relu(conv1d(xInput, w1)+b1)

#
nChan2=1

n2=nChan1/nChan2
x2=tf.reshape(x1,(-1,5,n2,nChan2))

#
nChan3=13
w3= GenWeight([1,1,nChan2,nChan3])
b3=GenBias([nChan3])
x3=tf.nn.relu(conv2d(x2, w3)+b3)

#
nChan4=13
w4= GenWeight([2,2,nChan2,nChan4])
b4=GenBias([nChan4])
x4=tf.nn.relu(conv2d(x2, w4)+b4)

#
nChan5=13
w5= GenWeight([3,3,nChan2,nChan5])
b5=GenBias([nChan5])
x5=tf.nn.relu(conv2d(x2, w5)+b5)

#
x6=tf.concat((tf.concat((x3,x4),axis=3),x5),axis=3)

#
nChan7=5
w7= GenWeight([3,3,nChan3+nChan4+nChan5,nChan7])
b7=GenBias([nChan7])
x7=tf.nn.relu(conv2d(x6, w7)+b7)


#
x8=tf.reshape(x7,(-1,5*n2*nChan7))

#
w9=GenWeight([5*n2*nChan7,14])
b9=GenBias([14])
x9=tf.matmul(x8,w9)+b9


#
n9_2=250
w9_2=GenWeight([5*n2*nChan7,n9_2])
b9_2=GenBias([n9_2])
x9_2=tf.nn.relu(tf.matmul(x8,w9_2)+b9_2)

#
w10_2=GenWeight([n9_2,14])
b10_2=GenBias([14])
x10_2=tf.matmul(x9_2,w10_2)+b10_2




##

xFinal=x10_2

xOutput=tf.reshape(xFinal,(-1,14))
yOutput=tf.reshape(yInput,(-1,14))


lossFn=tf.reduce_mean(tf.square(xOutput-yOutput))


trainBPM_1=tf.train.AdamOptimizer(0.05)
optBPM_1=trainBPM_1.minimize(lossFn)

trainBPM_2=tf.train.AdamOptimizer(0.01)
optBPM_2=trainBPM_2.minimize(lossFn)

trainBPM_3=tf.train.AdamOptimizer(0.005)
optBPM_3=trainBPM_3.minimize(lossFn)

trainBPM_4=tf.train.AdamOptimizer(0.001)
optBPM_4=trainBPM_4.minimize(lossFn)

iniBPM=tf.global_variables_initializer()


try:
    if vars().has_key('se'):
        se.close()
except:
    pass
se= tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
se.run(iniBPM)


nIt=2e7
sizeRow=100
stepLossRec=50
nLossRec=np.int32(nIt/stepLossRec+1)

lossRec=np.zeros((nLossRec))

iRec=0
for i in range(np.int32(nIt)):
    xBPM,yCHV=getDataRow(exData,sizeRow)
    se.run(optBPM_4,feed_dict={bpm:xBPM,cHV:yCHV})
    
    if i % stepLossRec==0:
        lossRecTmp=se.run(lossFn,feed_dict={bpm:xBPM,cHV:yCHV})
        lossRec[iRec]=lossRecTmp
        iRec+=1

        print lossRecTmp
        
        plt.figure('lossRec')
        numPlot=30
        plt.clf()
        if iRec<=numPlot:
            xPlot=np.linspace(0,iRec-1,iRec)
            yPlot=lossRec[0:iRec:]
            yPlotMean=np.cumsum(yPlot)/(xPlot+1)
            

        else:
            xPlot=np.linspace(iRec-numPlot,iRec-1,numPlot)
            yPlot=lossRec[iRec-numPlot:iRec:]
            yPlotMean[0:-1:]=yPlotMean[1::]
            yPlotMean[-1]=np.mean(yPlot)

        plt.hold
        plt.plot(xPlot,yPlot,'*b')
        plt.plot(xPlot,yPlotMean,'go')
            
        plt.grid('on')
        plt.title(i)
        plt.pause(0.05)
        
        
        xBPM,yCHV=getDataRow(exData,1)
        yCHV_Cal=se.run(xFinal,feed_dict={bpm:xBPM})
        plt.figure(2)
        plt.clf()
        plt.hold
        plt.plot(np.reshape(yCHV[0,:],(14)),'bd')
        plt.plot(yCHV_Cal[0,:],'rd')        
        plt.title(i)
        plt.pause(0.05)
    
    
#se.close()


xBPMReal_1=np.ones((5,2))*0.
xBPMReal_1[0,:]=[2.2,-1.6]

xBPMReal_2=np.ones((5,2))*3.
xBPMReal_3=np.ones((5,2))*(-3.)
xBPMReal_4=np.ones((5,2))
xBPMReal_4[:,0]=xBPMReal_4[:,0]*3.
xBPMReal_4[:,1]=xBPMReal_4[:,1]*(-3.)

xBPMReal=np.zeros((4,5,2))
xBPMReal[0,:,:]=xBPMReal_1
xBPMReal[1,:,:]=xBPMReal_2
xBPMReal[2,:,:]=xBPMReal_3
xBPMReal[3,:,:]=xBPMReal_4

yCHV_Cal4Real=se.run(xFinal,feed_dict={bpm:xBPMReal})

yCHV_Cal4Real_1=np.reshape(yCHV_Cal4Real[0,::],(7,2))
yCHV_Cal4Real_2=np.reshape(yCHV_Cal4Real[1,::],(7,2))
yCHV_Cal4Real_3=np.reshape(yCHV_Cal4Real[2,::],(7,2))
yCHV_Cal4Real_4=np.reshape(yCHV_Cal4Real[3,::],(7,2))

print '----------------- yCHV_Cal4Real_1 --------------------------'
print yCHV_Cal4Real_1
print '----------------- yCHV_Cal4Real_2 --------------------------'
print yCHV_Cal4Real_2
print '----------------- yCHV_Cal4Real_3 --------------------------'
print yCHV_Cal4Real_3
print '----------------- yCHV_Cal4Real_4 --------------------------'
print yCHV_Cal4Real_4

















