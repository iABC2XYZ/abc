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
exData=np.loadtxt(nameFolder+'Rec_1106_2046.dat')


#
'''
numInput=10
numOutput=14

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


lossFn=tf.losses.mean_squared_error(xOutput,yOutput)     


trainBPM=tf.train.AdamOptimizer(0.005)
optBPM=trainBPM.minimize(lossFn)

iniBPM=tf.global_variables_initializer()


try:
    if vars().has_key('se'):
        se.close()
except:
    pass
se= tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
se.run(iniBPM)
'''
'''
nIt=2e7
sizeRow=100
stepLossRec=50
nLossRec=np.int32(nIt/stepLossRec+1)

lossRec=np.zeros((nLossRec))
lossTestRec=np.zeros((nLossRec))

iRec=0
for i in range(np.int32(nIt)):
    xBPM,yCHV=getDataRow(exData,sizeRow)
    se.run(optBPM_4,feed_dict={bpm:xBPM,cHV:yCHV})
    
    if i % stepLossRec==0:
        lossRecTmp=se.run(lossFn,feed_dict={bpm:xBPM,cHV:yCHV})
        lossRec[iRec]=lossRecTmp
        

        #testBPM,testCHV=getDataRow(testData,np.shape(testData)[0])
        testBPM,testCHV=getDataRow(testData,sizeRow)
        lossTestRecTmp=se.run(lossFn,feed_dict={bpm:testBPM,cHV:testCHV})
        lossTestRec[iRec]=lossTestRecTmp
        
        iRec+=1
        
        print lossRecTmp,lossTestRecTmp
        
        plt.figure('lossRec')
        numPlot=30
        plt.clf()
        plt.subplot(1,2,1)
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
        plt.title('Train  '+str(i))
        
        #
        plt.subplot(1,2,2)
        
        if iRec<=numPlot:
            xPlotT=np.linspace(0,iRec-1,iRec)
            yPlotT=lossTestRec[0:iRec:]
            yPlotMeanT=np.cumsum(yPlotT)/(xPlotT+1)
            

        else:
            xPlotT=np.linspace(iRec-numPlot,iRec-1,numPlot)
            yPlotT=lossTestRec[iRec-numPlot:iRec:]
            yPlotMeanT[0:-1:]=yPlotMeanT[1::]
            yPlotMeanT[-1]=np.mean(yPlotT)

        plt.hold
        plt.plot(xPlotT,yPlotT,'*b')
        plt.plot(xPlotT,yPlotMeanT,'go')
            
        plt.grid('on')
        plt.title('Test  '+str(i))
        
        plt.pause(0.05)
        
        
        
        
        xBPM,yCHV=getDataRow(exData,1)
        yCHV_Cal=se.run(xFinal,feed_dict={bpm:xBPM})
        testBPM,testCHV=getDataRow(testData,1)
        testCHV_Cal=se.run(xFinal,feed_dict={bpm:testBPM})
        plt.figure('EX')
        plt.clf()
        plt.subplot(121)
        plt.hold
        plt.plot(np.reshape(yCHV[0,:],(14)),'bd')
        plt.plot(yCHV_Cal[0,:],'rd')        
        plt.title(i)
        plt.subplot(122)
        plt.hold
        plt.plot(np.reshape(testCHV[0,:],(14)),'bd')
        plt.plot(testCHV_Cal[0,:],'rd')        
        plt.title(i)
        plt.pause(0.05)   
    
    
    
######################   FINAL PLOT -------------
plotFolder='./11.3/'       
import os
if not os.path.exists(plotFolder):
    os.makedirs(plotFolder)
else:
     plotFolder=plotFolder[0:-1]+'Temp/' 
     os.makedirs(plotFolder)


plt.close('all')
# Train Plot
xBPM,yCHV=getDataRow(exData,sizeRow)
nameFig=plotFolder+'Loss Train RecSave'
fig=plt.figure(nameFig)
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
plt.title(nameFig)
nameFig+='.png'
fig.savefig(nameFig)


xBPM,yCHV=getDataRow(exData,1)
yCHV_Cal=se.run(xFinal,feed_dict={bpm:xBPM})
nameFig=plotFolder+'train Ex. Save'
plt.figure(nameFig)
plt.clf()
plt.hold
plt.plot(np.reshape(yCHV[0,:],(14)),'bd')
plt.plot(yCHV_Cal[0,:],'rd')        
plt.title(nameFig)
nameFig+='.png'
plt.savefig(nameFig)

# Test Plot
plt.close('all')
testBPM,testCHV=getDataRow(testData,np.shape(testData)[0])
nameFig=plotFolder+'Loss Test RecSave'
fig=plt.figure(nameFig)
numPlot=30
plt.clf()
if iRec<=numPlot:
    xPlot=np.linspace(0,iRec-1,iRec)
    yPlot=lossTestRec[0:iRec:]
    yPlotMean=np.cumsum(yPlot)/(xPlot+1)
    
else:
    xPlot=np.linspace(iRec-numPlot,iRec-1,numPlot)
    yPlot=lossTestRec[iRec-numPlot:iRec:]
    yPlotMean[0:-1:]=yPlotMean[1::]
    yPlotMean[-1]=np.mean(yPlot)

plt.hold
plt.plot(xPlot,yPlot,'*b')
plt.plot(xPlot,yPlotMean,'go')
plt.grid('on')
plt.title(nameFig)
nameFig+='.png'
fig.savefig(nameFig)


xBPMT,yCHVT=getDataRow(exData,1)
yCHVT_Cal=se.run(xFinal,feed_dict={bpm:xBPMT})
nameFig=plotFolder+'Test Ex. Save'
plt.figure(nameFig)
plt.clf()
plt.hold
plt.plot(np.reshape(yCHVT[0,:],(14)),'bd')
plt.plot(yCHVT_Cal[0,:],'rd')        
plt.title(nameFig)
nameFig+='.png'
plt.savefig(nameFig)


'''

















