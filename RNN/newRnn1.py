#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 23:18:17 2017

@author: p
"""


from __future__ import print_function, division
import numpy as np
import tensorflow as tf


numEpoch=1000
learningRate=0.3
sizeRNN=10
numHidden=4
depthLSTM=5
timeSteps=12
learningRateStart=0.08
maxGardNoem=5
numInput=4
numOutput=4
numItems=200


def GenData(numItems,numInput,numOutput):
    x=np.random.random((numItems,numInput))
    y=np.random.random((numItems,numOutput))
    return  (x,y)     

x, y_ = GenData(numItems,numInput,numOutput)



weights = {
    'input': tf.Variable(tf.truncated_normal([INPUT, N_HIDDEN_2], stddev=0.1)),
    'h1': tf.Variable(tf.truncated_normal([N_HIDDEN_2, N_HIDDEN_2], stddev=0.1)),
    'out': tf.Variable(tf.truncated_normal([N_HIDDEN_2, OUTPUT], stddev=0.1))
}

biases = {
    'input': tf.Variable(tf.zeros([N_HIDDEN_2])),
    'b1': tf.Variable(tf.zeros([N_HIDDEN_2])),
    'out': tf.Variable(tf.zeros([OUTPUT]))
}



print("E")


