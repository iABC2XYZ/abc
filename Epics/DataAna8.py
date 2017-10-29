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
    idChoose=np.random.randint(0,high=numEx,size=(sizeRow))
    yCHV=np.reshape(exData[idChoose,0:14],(sizeRow,7,2))
    xBPM=np.reshape(exData[idChoose,14:24],(sizeRow,5,2))
    return xBPM,yCHV



def conv1d(x, W):
    return tf.nn.conv1d(x, W, stride=1, padding="SAME")

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding="SAME")



exData=np.loadtxt('/home/p/ABC/abc/Epics/Rec.dat')


bpm=tf.placeholder(tf.float32,shape=(None,5,2))
cHV=tf.placeholder(tf.float32,shape=(None,7,2))


xInput=bpm
yInput=cHV

#
nChan1=100

w1= GenWeight([1,2,nChan1])
b1=GenBias([nChan1])
x1=tf.nn.relu(conv1d(xInput, w1)+b1)

#
nChan2=1

n2=nChan1/nChan2
x2=tf.reshape(x1,(-1,5,n2,nChan2))

#
nChan3=5
w3= GenWeight([1,1,nChan2,nChan3])
b3=GenBias([nChan3])
x3=tf.nn.relu(conv2d(x2, w3)+b3)

#
nChan4=5
w4= GenWeight([2,2,nChan2,nChan4])
b4=GenBias([nChan4])
x4=tf.nn.relu(conv2d(x2, w4)+b4)

#
nChan5=5
w5= GenWeight([3,3,nChan2,nChan5])
b5=GenBias([nChan5])
x5=tf.nn.relu(conv2d(x2, w5)+b5)

#
x6=tf.concat((tf.concat((x3,x4),axis=3),x5),axis=3)

#
nChan7=1
w7= GenWeight([3,3,nChan3+nChan4+nChan5,nChan7])
b7=GenBias([nChan7])
x7=tf.nn.relu(conv2d(x6, w7)+b7)


#
x8=tf.reshape(x7,(-1,5*n2))

#
w9=GenWeight([5*n2,14])
b9=GenBias([14])
x9=tf.matmul(x8,w9)+b9



##

xFinal=x9

xOutput=tf.reshape(xFinal,(-1,14))
yOutput=tf.reshape(yInput,(-1,14))


lossFn=tf.reduce_mean(tf.square(xOutput-yOutput))


trainBPM=tf.train.AdamOptimizer(0.01)
optBPM=trainBPM.minimize(lossFn)

iniBPM=tf.global_variables_initializer()


try:
    if vars().has_key('se'):
        se.close()
except:
    pass
se= tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
se.run(iniBPM)


nIt=1e5
sizeRow=20
stepLossRec=600
nLossRec=np.int32(nIt/stepLossRec+1)

lossRec=np.zeros((nLossRec))

iRec=0
for i in range(np.int32(nIt)):
    xBPM,yCHV=getDataRow(exData,sizeRow)
    se.run(optBPM,feed_dict={bpm:xBPM,cHV:yCHV})
    
    if i % stepLossRec==0:
        lossRecTmp=se.run(lossFn,feed_dict={bpm:xBPM,cHV:yCHV})
        lossRec[iRec]=lossRecTmp
        iRec+=1

        print lossRecTmp
                
        plt.figure(1)
        plt.hold
        plt.plot(iRec,lossRecTmp,'*b')
        plt.grid('on')
        plt.title(i)
        plt.pause(0.05)
        
        
        xBPM,yCHV=getDataRow(exData,5)
        yCHV_Cal=se.run(xFinal,feed_dict={bpm:xBPM})
        plt.figure(2)
        plt.clf()
        plt.hold
        #plt.plot(yCHV[0,:],'b*')
        #plt.plot(yCHV_Cal[0,:],'r*')
        #plt.plot(yCHV[1,:],'bo')
        #plt.plot(yCHV_Cal[1,:],'ro')
        #plt.plot(yCHV[2,:],'b^')
        #plt.plot(yCHV_Cal[2,:],'r^')
        #plt.plot(yCHV[3,:],'bs')
        #plt.plot(yCHV_Cal[3,:],'rs')
        plt.plot(np.reshape(yCHV[4,:],(14)),'bd')
        plt.plot(yCHV_Cal[4,:],'rd')        
        plt.title(i)
        plt.pause(0.05)
    
    
#se.close()


xBPMReal_1=np.ones((5,2))*0.
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

















