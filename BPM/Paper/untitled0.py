#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function, division
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import matplotlib.pyplot as plt

plt.close('all')


numEpoch=2000000
batchSize= 50

stepRec = 200


learningRate=0.01

rnnSize=16
rnnDepth=1

numInput=10
numOutput=14


nameFolder='/home/e/ABC/abc/Epics/rnn/'

def GenWeight(shape):
    initial = tf.truncated_normal(shape, stddev=1.)
    return tf.Variable(initial)
def GenBias(shape):
    initial = tf.Variable(tf.zeros([shape]))
    return tf.Variable(initial)

def getDataRowAll(exData):
    yCHV=exData[:,0:14]
    xBPM=exData[:,14:24]
    return xBPM,yCHV

def getDataRowBatch(exData,batchSize):
    numEx = np.shape(exData)[0]
    numChosen=numEx-np.floor(numEx/batchSize)*batchSize
    idChoose=np.random.randint(0, high=numChosen)

    xBPM1 = np.reshape(exData[idChoose:idChoose+batchSize, 14:24], (batchSize, 10))
    yCHV1 = np.reshape(exData[idChoose:idChoose + batchSize, 0:14], (batchSize, 14))
    yCHV1[11]=0.

    return xBPM1, yCHV1


#
dataTrain=np.loadtxt(nameFolder+'recTrain.dat')
dataTest=np.loadtxt(nameFolder+'recTest.dat')


#
bpm=tf.placeholder(tf.float32,shape=(None,numInput))
cHV=tf.placeholder(tf.float32,shape=(None,numOutput))

xInput=bpm
yInput=cHV

##

def RNN(numInput,rnnSize,rnnDepth):

    wRNNpre=GenWeight((numInput,rnnSize))
    bRNNpre=GenBias((rnnSize))
    rnnInput=[tf.nn.xw_plus_b(xInput,wRNNpre,bRNNpre)]

    wRNN=GenWeight((rnnSize,rnnSize))
    bRNN=GenBias((rnnSize))
    cellLSTM = tf.nn.rnn_cell.LSTMCell(rnnSize, state_is_tuple=True)
    cellRNN=tf.nn.rnn_cell.DropoutWrapper(tf.contrib.rnn.MultiRNNCell([cellLSTM] * rnnDepth),output_keep_prob=0.5)
    outRNN, stateRNN = tf.contrib.rnn.static_rnn(cellRNN, rnnInput, dtype=tf.float32)
    rnnOutput=tf.nn.xw_plus_b(outRNN[-1],wRNN,bRNN)
    xRnnOutput=tf.nn.relu(rnnOutput)

    return xRnnOutput

xRnnOutput=RNN(numInput,rnnSize,rnnDepth)

##
wFinal = GenWeight((rnnSize, numOutput))
bFinal = GenBias((numOutput))
xFinal=tf.nn.xw_plus_b(xRnnOutput,wFinal,bFinal)


##
xOutput=tf.reshape(xFinal,(-1,numOutput))
yOutput=tf.reshape(yInput,(-1,numOutput))



##---------------------------------------------------------

lossFn = tf.sqrt(tf.losses.mean_squared_error(xOutput , yOutput))


trainBPM = tf.train.AdamOptimizer(learningRate)
optBPM = trainBPM.minimize(lossFn)

iniBPM = tf.global_variables_initializer()

try:
    if vars().has_key('se'):
        se.close()
except:
    pass
se = tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
se.run(iniBPM)



nLossRec = np.int32(numEpoch/ stepRec + 1)

lossRec = []
lossTestRec = []
lossRecMean = []
lossTestRecMean = []

rCHV=[]


for i in range(np.int32(numEpoch)):
    xBPM, yCHV = getDataRowBatch(dataTrain,batchSize)

    se.run(optBPM, feed_dict={bpm: xBPM, cHV: yCHV})

    if i % stepRec==0:
        xTestBPM, yTestCHV = getDataRowBatch(dataTrain, batchSize)
        lossTestBPM=se.run(lossFn, feed_dict={bpm: xTestBPM, cHV: yTestCHV})
        lossBPM=se.run(lossFn, feed_dict={bpm: xBPM, cHV: yCHV})

        lossRec.append(lossBPM)
        lossTestRec.append(lossTestBPM)
        lossRecMean.append(np.mean(lossRec))
        lossTestRecMean.append(np.mean(lossTestRec))

        if len(lossRec)>=stepRec:
            if i % (stepRec*2)==0:
                lossRec.pop(0)
                lossTestRec.pop(0)
                lossRecMean.pop(0)
                lossTestRecMean.pop(0)

        print(lossBPM,lossTestBPM)

        plt.figure('Loss')
        plt.clf()
        plt.subplot(121)
        plt.plot(lossRec,'b.')
        plt.plot(lossRecMean, 'r.')

        plt.grid('on')
        plt.title(str(i)+'       lossTrain           lossTest')
        plt.subplot(122)
        plt.plot(lossTestRec, 'b.')
        plt.plot(lossTestRecMean,'r.')
        plt.grid('on')
        plt.pause(0.001)

        #####--------------------------------------------

        xExBPM=np.array([np.mean(xBPM[:,0]),0.,0,0,0,np.mean(xBPM[:,5]),0,0,0,0])[:,np.newaxis].T
        yExCHV=se.run(xFinal, feed_dict={bpm: xExBPM})

        rCHV.append(np.mean(np.square(yExCHV)))

        if len(lossRec)>=stepRec:
            if i % (stepRec*2)==0:
                rCHV.pop(0)

        plt.figure('RCHV')
        plt.clf()
        plt.plot(rCHV,'.')


        print('-----   xExBPM   --------')
        print(np.round(xExBPM*100)/100.)
        print('-----   yExCHV   --------')
        print(np.round(yExCHV*100)/100)

print('END')













