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

rnnSize=128
rnnDepth=20

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
    cellRNN=tf.contrib.rnn.MultiRNNCell([cellLSTM] * rnnDepth)
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






