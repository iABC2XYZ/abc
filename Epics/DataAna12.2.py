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

plotFolder='./12.2/'  
    

def GenWeight(shape):
    initial = tf.truncated_normal(shape, stddev=1.)
    return tf.Variable(initial)
def GenBias(shape):
    initial = tf.constant(1., shape=shape)
    return tf.Variable(initial)



def getDataRow(exData,sizeRow,numMem=1):
    numEx=np.shape(exData)[0]
    idChoose1=np.random.randint(0,high=numEx-numMem,size=(sizeRow))
    idChoose2=idChoose1+numMem
    yCHV1=np.reshape(exData[idChoose1,0:14],(sizeRow,14))
    xBPM1=np.reshape(exData[idChoose1,14:24],(sizeRow,10))
    yCHV2=np.reshape(exData[idChoose2,0:14],(sizeRow,14))
    xBPM2=np.reshape(exData[idChoose2,14:24],(sizeRow,10))
    # x: 当前电流yCHV1  [14]，当前位置xBPM1 [１０]，需要改变到的位置xBPM２　【１０】
    # y: 需要改变到的电流yCHV1　【１４】
    X=np.hstack((xBPM1,xBPM2,yCHV1))
    Y=yCHV2
    return X,Y



def conv1d(x, W):
    return tf.nn.conv1d(x, W, stride=1, padding="SAME")

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding="SAME")


nameFolder='/home/node1/Templates/ABC/abc/Epics/'
exData=np.loadtxt(nameFolder+'Rec.dat')
testData=np.loadtxt(nameFolder+'testRec.dat')


bpm=tf.placeholder(tf.float32,shape=(None,34))
cHV=tf.placeholder(tf.float32,shape=(None,14))


xInput=bpm
yInput=cHV

#

numX1=20
w1= GenWeight([34,numX1])
b1=GenBias([numX1])
x1=tf.atan(tf.matmul(xInput,w1)+b1)

#
numX2=20
w2= GenWeight([numX1,numX2])
b2=GenBias([numX2])
x2=tf.atan(tf.matmul(x1,w2)+b2)

#
numX3=14
w3= GenWeight([numX2,numX3])
b3=GenBias([numX3])
x3=tf.matmul(x2,w3)+b3

#
tf.nn.dropout(x3,0.5)

##

xFinal=x3

xOutput=tf.reshape(xFinal,(-1,14))
yOutput=tf.reshape(yInput,(-1,14))


lossFn=tf.sqrt(tf.reduce_mean(tf.square(xOutput-yOutput)))



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


nIt=2e7
sizeRow=100
stepLossRec=50
nLossRec=np.int32(nIt/stepLossRec+1)

lossRec=np.zeros((nLossRec))
lossTestRec=np.zeros((nLossRec))

iRec=0
for i in range(np.int32(nIt)):
    xBPM,yCHV=getDataRow(exData,sizeRow)
    se.run(optBPM,feed_dict={bpm:xBPM,cHV:yCHV})
    
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
        
        numMean=30
        numPlot=np.max([np.round(iRec/5),numMean])
        
        plt.clf()
        plt.subplot(1,2,1)
        if iRec<=numPlot:
            xPlot=np.linspace(0,iRec-1,iRec)
            yPlot=lossRec[0:iRec:]
            yPlotMean=np.cumsum(yPlot)/(xPlot+1)
            
        else:
            
            xPlot=np.linspace(iRec-numPlot,iRec-1,numPlot)
            yPlot=lossRec[iRec-numPlot:iRec:]
            yPlotMean=np.zeros(np.int32(numPlot))

            for iPlot in range(numPlot):
                meanStart=iRec-(numPlot-iPlot)-numMean
                meanEnd=iRec-(numPlot-iPlot)
                
                yPlotMean[iPlot]=np.mean(lossRec[meanStart:meanEnd])
            

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
            yPlotMeanT=np.zeros(np.int32(numPlot))

            for iPlot in range(numPlot):
                meanTStart=iRec-(numPlot-iPlot)-numMean
                meanTEnd=iRec-(numPlot-iPlot)
                
                yPlotMeanT[iPlot]=np.mean(lossTestRec[meanTStart:meanTEnd])

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
    yPlotMean=np.zeros(np.int32(numPlot))

    for iPlot in range(numPlot):
        meanStart=iRec-(numPlot-iPlot)-numMean
        meanEnd=iRec-(numPlot-iPlot)
        
        yPlotMean[iPlot]=np.mean(lossRec[meanStart:meanEnd])

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
    xPlotT=np.linspace(iRec-numPlot,iRec-1,numPlot)
    yPlotT=lossTestRec[iRec-numPlot:iRec:]
    yPlotMeanT=np.zeros(np.int32(numPlot))

    for iPlot in range(numPlot):
        meanTStart=iRec-(numPlot-iPlot)-numMean
        meanTEnd=iRec-(numPlot-iPlot)
        
        yPlotMeanT[iPlot]=np.mean(lossTestRec[meanTStart:meanTEnd])

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


##
    

    
    
    


testBPM,testCHV=getDataRow(testData,np.shape(testData)[0])
testCHVCal=np.reshape(se.run(xFinal,feed_dict={bpm:testBPM}),np.shape(testCHV))


for i in range(7):
    for j in range(2):
        if j==0:
            nameFigure=plotFolder+'Test x: '+str(i+1)
        else:
            nameFigure=plotFolder+'Test y: '+str(i+1)
        
        plt.figure(nameFigure)
        plt.clf()
        plt.hold
        plt.plot(testCHV[:,i+j*7],'r.')
        plt.plot(testCHVCal[:,i+j*7],'b.')
        plt.title(nameFigure)
        nameFig=nameFigure+'.png'
        plt.savefig(nameFig)


for i in range(7):
    for j in range(2):
        if j==0:
            nameFigure=plotFolder+'Ratio Test x: '+str(i+1)
        else:
            nameFigure=plotFolder+'Ratio Test y: '+str(i+1)
        
        plt.figure(nameFigure)
        plt.clf()
        plt.hold
        plt.plot((testCHV[:,i+j*7]-testCHVCal[:,i+j*7])/testCHV[:,i+j*7],'r.')
        nameFig=nameFigure+'.png'
        plt.savefig(nameFig)
  

plt.close('all')









