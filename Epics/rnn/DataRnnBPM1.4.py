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

numRNNHiddenLayer=128
numRNNCell=1

numInput=10
numOutput=14


nameFolder='/home/p/ABC/abc/Epics/rnn/'

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
numRNNOutput=10
wRNN=GenWeight((numRNNHiddenLayer,numRNNOutput))
bRNN=GenBias((numRNNOutput))

def RNN(xRNN, wRNN, bRNN):

    x=tf.reshape(xRNN,[-1,numInput])
    lstmCellBasic = tf.contrib.rnn.BasicLSTMCell(numRNNHiddenLayer, forget_bias=1.0)
    lstmCellMulti = tf.contrib.rnn.MultiRNNCell([lstmCellBasic]*np.int32(numRNNCell))
    outputs, states = tf.contrib.rnn.static_rnn(lstmCellMulti, x, dtype=tf.float32)
    result=tf.matmul(outputs[-1], wRNN) + bRNN

    return result



logits = RNN(xInput, wRNN, bRNN)








