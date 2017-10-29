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
        
    
numLayer=3

sizeLayer=[12,12,12,12,12,12,12,12]    #  Hidden

bpm=tf.placeholder(tf.float32,shape=(None,10))
cHV=tf.placeholder(tf.float32,shape=(None,14))



wFC0_1= GenWeight([10,sizeLayer[0]])
bFC0_1=GenBias([sizeLayer[0]])
wFC1_1= GenWeight([sizeLayer[0],sizeLayer[1]])
bFC1_1=GenBias([sizeLayer[1]])
wFC2_1= GenWeight([sizeLayer[1],sizeLayer[2]])
bFC2_1=GenBias([sizeLayer[2]])
wFC3_1= GenWeight([sizeLayer[2],sizeLayer[3]])
bFC3_1=GenBias([sizeLayer[3]])   
wFC4_1= GenWeight([sizeLayer[3],sizeLayer[4]])
bFC4_1=GenBias([sizeLayer[4]])   
wFC5_1= GenWeight([sizeLayer[4],sizeLayer[5]])
bFC5_1=GenBias([sizeLayer[5]])   
wFC6_1= GenWeight([sizeLayer[5],sizeLayer[6]])
bFC6_1=GenBias([sizeLayer[6]])   
wFC7_1= GenWeight([sizeLayer[6],sizeLayer[7]])
bFC7_1=GenBias([sizeLayer[7]])   
wFCEnd_1= GenWeight([sizeLayer[numLayer-1],14])
bFCEnd_1=GenBias([14])   

##

wFC0_2= GenWeight([10,sizeLayer[0]])
bFC0_2=GenBias([sizeLayer[0]])
wFC1_2= GenWeight([sizeLayer[0],sizeLayer[1]])
bFC1_2=GenBias([sizeLayer[1]])
wFC2_2= GenWeight([sizeLayer[1],sizeLayer[2]])
bFC2_2=GenBias([sizeLayer[2]])
wFC3_2= GenWeight([sizeLayer[2],sizeLayer[3]])
bFC3_2=GenBias([sizeLayer[3]])   
wFC4_2= GenWeight([sizeLayer[3],sizeLayer[4]])
bFC4_2=GenBias([sizeLayer[4]])   
wFC5_2= GenWeight([sizeLayer[4],sizeLayer[5]])
bFC5_2=GenBias([sizeLayer[5]])   
wFC6_2= GenWeight([sizeLayer[5],sizeLayer[6]])
bFC6_2=GenBias([sizeLayer[6]])   
wFC7_2= GenWeight([sizeLayer[6],sizeLayer[7]])
bFC7_2=GenBias([sizeLayer[7]])   
wFCEnd_2= GenWeight([sizeLayer[numLayer-1],14])
bFCEnd_2=GenBias([14])   

##


xInput=bpm
yInput=cHV

xFC0_1=tf.matmul(xInput,wFC0_1)+bFC0_1
xAct0_1=tf.nn.relu(xFC0_1)
xFC1_1=tf.matmul(xAct0_1,wFC1_1)+bFC1_1
xAct1_1=tf.nn.relu(xFC1_1)
xFC2_1=tf.matmul(xAct1_1,wFC2_1)+bFC2_1
xAct2_1=tf.nn.relu(xFC2_1)
xFC3_1=tf.matmul(xAct2_1,wFC3_1)+bFC3_1
xAct3_1=tf.nn.relu(xFC3_1)
xFC4_1=tf.matmul(xAct3_1,wFC4_1)+bFC4_1
xAct4_1=tf.nn.relu(xFC4_1)
xFC5_1=tf.matmul(xAct4_1,wFC5_1)+bFC5_1
xAct5_1=tf.nn.relu(xFC5_1)
xFC6_1=tf.matmul(xAct5_1,wFC6_1)+bFC6_1
xAct6_1=tf.nn.relu(xFC6_1)
xFC7_1=tf.matmul(xAct6_1,wFC7_1)+bFC7_1

xActEnd_1=tf.nn.relu(eval('xFC'+str(numLayer-1)+'_1'))
xFCEnd_1=tf.matmul(xActEnd_1,wFCEnd_1)+bFCEnd_1

##
xFC0_2=tf.matmul(xInput,wFC0_2)+bFC0_2
xAct0_2=tf.nn.relu(xFC0_2)
xFC1_2=tf.matmul(xAct0_2,wFC1_2)+bFC1_2
xAct1_2=tf.nn.relu(xFC1_2)
xFC2_2=tf.matmul(xAct1_2,wFC2_2)+bFC2_2
xAct2_2=tf.nn.relu(xFC2_2)
xFC3_2=tf.matmul(xAct2_2,wFC3_2)+bFC3_2
xAct3_2=tf.nn.relu(xFC3_2)
xFC4_2=tf.matmul(xAct3_2,wFC4_2)+bFC4_2
xAct4_2=tf.nn.relu(xFC4_2)
xFC5_2=tf.matmul(xAct4_2,wFC5_2)+bFC5_2
xAct5_2=tf.nn.relu(xFC5_2)
xFC6_2=tf.matmul(xAct5_2,wFC6_2)+bFC6_2
xAct6_2=tf.nn.relu(xFC6_2)
xFC7_2=tf.matmul(xAct6_2,wFC7_2)+bFC7_2

xActEnd_2=tf.nn.relu(eval('xFC'+str(numLayer-1)+'_2'))
xFCEnd_2=tf.matmul(xActEnd_2,wFCEnd_2)+bFCEnd_2

##

xFinal=xFCEnd_1+xFCEnd_2


#xOutput=tf.nn.softmax(xFinal)
#yOutput=tf.nn.softmax(yInput)
xOutput=xFinal
yOutput=yInput
#xOutput=xFinal+50.
#yOutput=yInput+50.

#lossFn=-tf.reduce_mean(yOutput*tf.log(xOutput))
lossFn=tf.reduce_mean(tf.square(xOutput-yOutput))
#lossFn=tf.reduce_mean(tf.abs(xOutput-yOutput))
#lossFn=tf.reduce_max(tf.abs(xOutput-yOutput))
#lossFn=tf.reduce_sum(tf.abs(xOutput*yOutput))


trainBPM=tf.train.AdamOptimizer(0.001)
#trainBPM=tf.train.GradientDescentOptimizer(0.01)
optBPM=trainBPM.minimize(lossFn)

iniBPM=tf.global_variables_initializer()

nIt=1e5
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





