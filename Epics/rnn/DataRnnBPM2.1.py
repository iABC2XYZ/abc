#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function, division
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import matplotlib.pyplot as plt

plt.close('all')



numEpoch=1000
learningRate=0.3

depthRNN=8

numInput=10
numOutput=14


nameFolder='/home/e/ABC/abc/Epics/rnn/'

def GenWeight(shape):
    initial = tf.truncated_normal(shape, stddev=1.)
    return tf.Variable(initial)
def GenBias(shape):
    initial = tf.Variable(tf.zeros([shape]))
    return tf.Variable(initial)

def getDataRow(exData,sizeRow):
    numEx=np.shape(exData)[0]
    idChoose=np.random.randint(0,high=numEx,size=(sizeRow))
    yCHV=np.reshape(exData[idChoose,0:14],(sizeRow,14))
    xBPM=np.reshape(exData[idChoose,14:24],(sizeRow,10))
    return xBPM,yCHV


dataTrain=np.loadtxt(nameFolder+'recTrain.dat')
dataTest=np.loadtxt(nameFolder+'recTest.dat')


#
bpm=tf.placeholder(tf.float32,shape=(None,numInput))
cHV=tf.placeholder(tf.float32,shape=(None,numOutput))


xInput=bpm
yInput=cHV


#
numX1=10
w1=GenWeight((numInput,numX1))
b1=GenBias((numX1))
x1 = [tf.nn.xw_plus_b(xInput, w1, b1)]



#

numX2=12
w2=GenWeight((numX1,numX2))
b2=GenBias((numX2))

lstmCell = tf.contrib.rnn.GRUCell(numX1)
lstmMulti = tf.contrib.rnn.MultiRNNCell([lstmCell] * depthRNN)
statesSeries, stateCurrent = tf.contrib.rnn.static_rnn(lstmMulti,x1, dtype=tf.float32)
x2 = tf.nn.relu(tf.nn.xw_plus_b(statesSeries[-1], w2, b2))

#
numX3=14
w3=GenWeight((numX2,numX3))
b3=GenBias((numX3))
x3=tf.nn.xw_plus_b(x2, w3, b3)


#
xFinal=x3

xOutput=tf.reshape(xFinal,(-1,numOutput))
yOutput=tf.reshape(yInput,(-1,numOutput))

#

lossRNN = tf.reduce_mean(tf.losses.mean_squared_error(xOutput, yOutput))
trainRNN = tf.train.AdagradOptimizer(learningRate)
optRNN = trainRNN.minimize(lossRNN)


iniRNN=tf.global_variables_initializer()


try:
    if vars().has_key('se'):
        se.close()
except:
    pass
se= tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
se.run(iniRNN)

nIt = 2e7
sizeRow = 100
stepLossRec = 50
nLossRec = np.int32(nIt / stepLossRec + 1)

lossRec = np.zeros((nLossRec))
lossTestRec = np.zeros((nLossRec))

iRec = 0
for i in range(np.int32(nIt)):
    xBPM, yCHV = getDataRow(dataTrain, sizeRow)
    se.run(optRNN, feed_dict={bpm: xBPM, cHV: yCHV})

    if i % stepLossRec == 0:
        lossRecTmp = se.run(lossRNN, feed_dict={bpm: xBPM, cHV: yCHV})
        lossRec[iRec] = lossRecTmp

        # testBPM,testCHV=getDataRow(testData,np.shape(testData)[0])
        testBPM, testCHV = getDataRow(dataTest, sizeRow)
        lossTestRecTmp = se.run(lossRNN, feed_dict={bpm: testBPM, cHV: testCHV})
        lossTestRec[iRec] = lossTestRecTmp

        iRec += 1

        print
        lossRecTmp, lossTestRecTmp

        plt.figure('lossRec')
        numPlot = 30
        plt.clf()
        plt.subplot(1, 2, 1)
        if iRec <= numPlot:
            xPlot = np.linspace(0, iRec - 1, iRec)
            yPlot = lossRec[0:iRec:]
            yPlotMean = np.cumsum(yPlot) / (xPlot + 1)


        else:
            xPlot = np.linspace(iRec - numPlot, iRec - 1, numPlot)
            yPlot = lossRec[iRec - numPlot:iRec:]
            yPlotMean[0:-1:] = yPlotMean[1::]
            yPlotMean[-1] = np.mean(yPlot)

        plt.hold
        plt.plot(xPlot, yPlot, '*b')
        plt.plot(xPlot, yPlotMean, 'go')

        plt.grid('on')
        plt.title('Train  ' + str(i))

        #
        plt.subplot(1, 2, 2)

        if iRec <= numPlot:
            xPlotT = np.linspace(0, iRec - 1, iRec)
            yPlotT = lossTestRec[0:iRec:]
            yPlotMeanT = np.cumsum(yPlotT) / (xPlotT + 1)


        else:
            xPlotT = np.linspace(iRec - numPlot, iRec - 1, numPlot)
            yPlotT = lossTestRec[iRec - numPlot:iRec:]
            yPlotMeanT[0:-1:] = yPlotMeanT[1::]
            yPlotMeanT[-1] = np.mean(yPlotT)

        plt.hold
        plt.plot(xPlotT, yPlotT, '*b')
        plt.plot(xPlotT, yPlotMeanT, 'go')

        plt.grid('on')
        plt.title('Test  ' + str(i))

        plt.pause(0.05)

        xBPM, yCHV = getDataRow(dataTrain, 1)
        yCHV_Cal = se.run(xFinal, feed_dict={bpm: xBPM})
        testBPM, testCHV = getDataRow(dataTest, 1)
        testCHV_Cal = se.run(xFinal, feed_dict={bpm: testBPM})
        plt.figure('EX')
        plt.clf()
        plt.subplot(121)
        plt.hold
        plt.plot(np.reshape(yCHV[0, :], (14)), 'bd')
        plt.plot(yCHV_Cal[0, :], 'rd')
        plt.title(i)
        plt.subplot(122)
        plt.hold
        plt.plot(np.reshape(testCHV[0, :], (14)), 'bd')
        plt.plot(testCHV_Cal[0, :], 'rd')
        plt.title(i)
        #plt.show()
        plt.pause(0.05)


print("E")



