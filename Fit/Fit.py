#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 08:27:24 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
______________________________________________________


"""

import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt

def FitLayer(x,y):
    wWeights=tf.Variable(tf.zeros(7))
    y_=wWeights[6]*tf.pow(x,6)+wWeights[5]*tf.pow(x,5)+wWeights[4]*tf.pow(x,4)+wWeights[3]*tf.pow(x,3)+wWeights[2]*tf.pow(x,2)+wWeights[1]*tf.pow(x,1)+wWeights[0]
    deltaY=tf.abs(y-y_)
    return deltaY,wWeights

x=np.linspace(-100.,100.,500)+np.random.randn()
y=0.8*x**5+1.7*x**2

x=x[:,np.newaxis]
y=y[:,np.newaxis]

#plt.figure(1)
#plt.plot(x,y,'.')

xS=tf.placeholder(tf.float32,[None,1])
yS=tf.placeholder(tf.float32,[None,1])

FitTest,wWeights=FitLayer(xS,yS)

TrainLoss=FitTest

FitTrain=tf.train.GradientDescentOptimizer(0.01).minimize(TrainLoss)

init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(1000):
        sess.run(FitTrain,feed_dict={xS:x,yS:y})
        print(sess.run(wWeights,feed_dict={xS:x,yS:y}))













