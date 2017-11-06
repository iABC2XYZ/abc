#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function, division
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import matplotlib.pyplot as plt

plt.close('all')



numEpoch=200000
learningRate=0.01
sizeRow = 100


numInput=10
numOutput=14


nameFolder='/home/p/ABC/abc/Epics/rnn/'

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

def getDataRow_inOrder(exData,sizeRow,idOrder):
    numEx=np.shape(exData)[0]
    if idOrder+sizeRow>=numEx:
        sizeRow=numEx-idOrder

    yCHV=np.reshape(exData[idOrder:idOrder+sizeRow,0:14],(sizeRow,14))
    xBPM=np.reshape(exData[idOrder:idOrder+sizeRow,14:24],(sizeRow,10))
    return xBPM,yCHV,idOrder







dataTrain=np.loadtxt(nameFolder+'recTrain.dat')
dataTest=np.loadtxt(nameFolder+'recTest.dat')


#
bpm=tf.placeholder(tf.float32,shape=(None,numInput))
cHV=tf.placeholder(tf.float32,shape=(None,numOutput))


xInput=bpm
yInput=cHV


#
numX1=100
w1=GenWeight((numInput,numX1))
b1=GenBias((numX1))
x1 = [tf.nn.xw_plus_b(tf.reshape(xInput,[-1,numInput]), w1, b1)]


#

numX2=5
depthRNN=1
w2=GenWeight((numX1,numX2))
b2=GenBias((numX2))

lstmCell = tf.contrib.rnn.GRUCell(numX1)
lstmMulti = tf.contrib.rnn.MultiRNNCell([lstmCell] * depthRNN)

initState = lstmMulti.zero_state(sizeRow , dtype=tf.float32)  # 初始化全零 state

x1In= tf.reshape(x1, [-1, numInput, numX2])
outputs, stateFinal = tf.nn.dynamic_rnn(lstmMulti, x1In, initial_state=initState, time_major=False)


x2 = tf.nn.relu(tf.nn.xw_plus_b(outputs[-1], w2, b2))



numX3=14
w3=GenWeight((numX2,numX3))
b3=GenBias((numX3))
x3=tf.nn.dropout(tf.nn.xw_plus_b(x2, w3, b3),keep_prob=0.8)


#
xFinal=x3

print(xFinal)

'''
xOutput=tf.reshape(xFinal,(-1,numOutput))
yOutput=tf.reshape(yInput,(-1,numOutput))

#

print(xOutput)
print(yOutput)

lossRNN = tf.sqrt(tf.reduce_mean(tf.losses.mean_squared_error(xOutput, yOutput)))
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



stepLossRec = 50
nLossRec = np.int32(numEpoch / stepLossRec + 1)

lossRec = np.zeros((nLossRec))
lossTestRec = np.zeros((nLossRec))


iRec = 0
idOrder=0
for i in range(np.int32(numEpoch)):
    xBPM, yCHV ,idOrder= getDataRow_inOrder(dataTrain,sizeRow,idOrder)
    #se.run(optRNN, feed_dict={bpm: xBPM, cHV: yCHV})


    
    if i % stepLossRec == 0:
        lossRecTmp = se.run(lossRNN, feed_dict={bpm: xBPM, cHV: yCHV})
        lossRec[iRec] = lossRecTmp

        # testBPM,testCHV=getDataRow(testData,np.shape(testData)[0])
        #testBPM, testCHV = getDataRow(dataTest, sizeRow)
        testBPM, testCHV,testIDOrder=getDataRow_inOrder(dataTest,np.shape(dataTest)[0],0)

        lossTestRecTmp = se.run(lossRNN, feed_dict={bpm: testBPM, cHV: testCHV})
        lossTestRec[iRec] = lossTestRecTmp

        iRec += 1

        print(lossRecTmp, lossTestRecTmp)

        plt.figure('lossRec')
        numMean=np.int32(30)
        numPlot = np.int32(np.max([numMean,np.round(iRec/4)]))
        plt.clf()
        plt.subplot(1, 2, 1)
        if iRec <= numPlot:
            xPlot = np.linspace(0, iRec - 1, iRec)
            yPlot = lossRec[0:iRec:]
            yPlotMean = np.cumsum(yPlot) / (xPlot + 1)


        else:
            xPlot = np.linspace(iRec - numPlot, iRec - 1, numPlot)
            yPlot = lossRec[iRec - numPlot:iRec:]
            yPlotMean = np.zeros(np.int32(numPlot))

            for iPlot in range(numPlot):
                meanStart = iRec - (numPlot - iPlot) - numMean
                meanEnd = iRec - (numPlot - iPlot)

                yPlotMean[iPlot] = np.mean(lossRec[meanStart:meanEnd])

            print('--------------')
            print(xPlot)
            print(yPlotMean)

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
            yPlotMeanT = np.zeros(np.int32(numPlot))

            for iPlot in range(numPlot):
                meanTStart = iRec - (numPlot - iPlot) - numMean
                meanTEnd = iRec - (numPlot - iPlot)

                yPlotMeanT[iPlot] = np.mean(lossTestRec[meanTStart:meanTEnd])

        plt.hold
        plt.plot(xPlotT, yPlotT, '*b')
        plt.plot(xPlotT, yPlotMeanT, 'go')

        plt.grid('on')
        plt.title('Test  ' + str(i))

        plt.pause(0.01)


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
        plt.pause(0.01)

'''

print("E")



