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
    yCHV=exData[idChoose,0:14]
    xBPM=exData[idChoose,14:24]
    return xBPM,yCHV


exDataTmp=np.loadtxt('Rec.dat')
exDataSize=np.size(exDataTmp)/25*25
exData=exDataTmp[0:exDataSize:].reshape(exDataSize/25,25)

flagWrite=0
if flagWrite==1:
    with open('Rec.BK','w+') as f:
        for i in range(exDataSize/25):
            strLine=str(exData[i,:]).replace('\n',' ')[1:-1:]+'\n'
            f.writelines(strLine)
        
    
numLayer=6

sizeLayer=[12,12,12,12,12,12]    #  Hidden

bpm=tf.placeholder(tf.float32,shape=(None,10))
cHV=tf.placeholder(tf.float32,shape=(None,14))



wFC0= GenWeight([10,sizeLayer[0]])
bFC0=GenBias([sizeLayer[0]])

wFC1= GenWeight([sizeLayer[0],sizeLayer[1]])
bFC1=GenBias([sizeLayer[1]])
    
wFC2= GenWeight([sizeLayer[1],sizeLayer[2]])
bFC2=GenBias([sizeLayer[2]])
    

wFC3= GenWeight([sizeLayer[2],sizeLayer[3]])
bFC3=GenBias([sizeLayer[3]])   

wFC4= GenWeight([sizeLayer[3],sizeLayer[4]])
bFC4=GenBias([sizeLayer[4]])   

wFC5= GenWeight([sizeLayer[4],sizeLayer[5]])
bFC5=GenBias([sizeLayer[5]])   

wFCEnd= GenWeight([sizeLayer[numLayer-1],14])
bFCEnd=GenBias([14])   


xInput=bpm
yInput=cHV

xFC0=tf.matmul(xInput,wFC0)+bFC0
xAct0=tf.atan(xFC0)
xFC1=tf.matmul(xAct0,wFC1)+bFC1
xAct1=tf.atan(xFC1)
xFC2=tf.matmul(xAct1,wFC2)+bFC2
xAct2=tf.atan(xFC2)
xFC3=tf.matmul(xAct2,wFC3)+bFC3
xAct3=tf.atan(xFC3)
xFC4=tf.matmul(xAct3,wFC4)+bFC4
xAct4=tf.atan(xFC4)
xFC5=tf.matmul(xAct4,wFC5)+bFC5

xActEnd=tf.atan(eval('xFC'+str(numLayer-1)))
xFCEnd=tf.matmul(xActEnd,wFCEnd)+bFCEnd




xFinal=xFCEnd


#xOutput=tf.nn.softmax(xFinal)
#yOutput=tf.nn.softmax(yInput)
xOutput=xFinal
yOutput=yInput
#xOutput=xFinal+50.
#yOutput=yInput+50.

#lossFn=-tf.reduce_mean(yOutput*tf.log(xOutput))
#lossFn=tf.reduce_mean(tf.square(xOutput-yOutput))
lossFn=tf.reduce_mean(tf.abs(xOutput-yOutput))

trainBPM=tf.train.AdamOptimizer(0.001)
optBPM=trainBPM.minimize(lossFn)

iniBPM=tf.global_variables_initializer()

nIt=5e4
sizeRow=100
stepLossRec=200
nLossRec=np.int32(nIt/stepLossRec+1)

lossRec=np.zeros((nLossRec))


se= tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
se.run(iniBPM)
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
        plt.plot(yCHV[4,:],'bd')
        plt.plot(yCHV_Cal[4,:],'rd')        
        plt.title(i)
        plt.pause(0.05)
    
    
se.close()





