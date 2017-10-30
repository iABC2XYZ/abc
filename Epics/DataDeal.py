#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 23:22:09 2017

@author: p
"""

import numpy as np
import matplotlib.pyplot as plt

rec=np.loadtxt('/home/p/ABC/abc/Epics/Rec.dat')


mapRes = np.zeros((10, 14))
biasRes=np.zeros((1,14))
for i in range(14):
    for j in range(10):
        res_fit = np.polyfit(rec[:, i], rec[:, 14 + j], 1)
        mapRes[j, i] = res_fit[0]
        biasRes[0,i]+=res_fit[1]
    biasRes[0,i]/=14.
#print(mapRes)


bpms=np.array([np.mean(rec[:,14]),np.mean(rec[:,15]),np.mean(rec[:,16]),np.mean(rec[:,17]),np.mean(rec[:,18]),np.mean(rec[:,19]),np.mean(rec[:,20]),np.mean(rec[:,21]),np.mean(rec[:,22]),np.mean(rec[:,23])])[:,np.newaxis].T
vCorrector=np.matmul(bpms,mapRes)+biasRes
print vCorrector


'''
for i in range(14):
    for j in range(10):
        plt.figure(str(i)+' '+str(j))
        plt.plot(rec[:, i], rec[:, 14 + j],'.')
        
'''

import tensorflow as tf
exData=rec

def GenWeight(shape):
    initial = tf.truncated_normal(shape, stddev=1.)
    return tf.Variable(initial)
def GenBias(shape):
    initial = tf.constant(1., shape=shape)
    return tf.Variable(initial)


def getDataRow(exData,sizeRow):
    numEx=np.shape(exData)[0]
    idChoose=np.random.randint(0,high=numEx,size=(sizeRow))
    yCHV=np.reshape(exData[idChoose,0:14],(sizeRow,7*2))
    xBPM=np.reshape(exData[idChoose,14:24],(sizeRow,5*2))
    return xBPM,yCHV


w=GenWeight((10,14))
b=GenBias([14])

bpm=tf.placeholder(tf.float32,shape=(None,10))
cHV=tf.placeholder(tf.float32,shape=(None,14))


xInput=bpm
yInput=cHV

x1=tf.matmul(bpm,w)+b


xFinal=x1

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


nIt=2e4
sizeRow=30
stepLossRec=50
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
    




yCHV_Cal4Real=se.run(xFinal,feed_dict={bpm:bpms})

print vCorrector
print yCHV_Cal4Real




