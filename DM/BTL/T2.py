#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:52:28 2017

@author: p

    NN
    
"""


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PreData import RandItemMulti

plt.close('all')

def GenWeight(shape):
    initial = tf.truncated_normal(shape, stddev=1.)
    return tf.Variable(initial)
def GenBias(shape):
    initial = tf.constant(1., shape=shape)
    return tf.Variable(initial)



numItem=64
numSample=2**8
numQuadHigh=20

weightSize=[numSample*4,2**6,2**4,numQuadHigh*3]

wFC1 = GenWeight([weightSize[0],weightSize[1]])
bFC1=GenWeight([weightSize[1]])

wFC2 = GenWeight([weightSize[1],weightSize[2]])
bFC2=GenWeight([weightSize[2]])

wFC3 = GenWeight([weightSize[2],weightSize[3]])
bFC3=GenWeight([weightSize[3]])


xInput=tf.placeholder(tf.float32,shape=[None,weightSize[0]])
yInput=tf.placeholder(tf.float32,shape=[None,weightSize[-1]])

xFC1=tf.matmul(xInput,wFC1)+bFC1
xAct1=tf.nn.relu(xFC1)
xFC2=tf.matmul(xAct1,wFC2)+bFC2
xAct2=tf.nn.relu(xFC2)
xFC3=tf.matmul(xAct2,wFC3)+bFC3

xFinal=xFC3

xOutput=xFinal
yOutput=yInput

costFunc=tf.reduce_sum((yOutput-xOutput)**2)

trainBTL=tf.train.AdamOptimizer(0.01)
optBTL=trainBTL.minimize(costFunc)

iniBTL=tf.global_variables_initializer()

numRun=10
costRec=np.zeros(numRun)

with tf.Session() as se:
    se.run(iniBTL)
    
    for _ in xrange(numRun):
        dataLattice,dataBeam=RandItemMulti(numItem,numSample,numQuadHigh)
       
        #T1=se.run(costFunc,feed_dict={xInput:dataBeam.reshape(numItem,weightSize[0]),yInput:dataLattice.reshape(numItem,weightSize[-1])}) 
        se.run(optBTL,feed_dict={xInput:dataBeam.reshape(numItem,weightSize[0]),yInput:dataLattice.reshape(numItem,weightSize[-1])})
        T2=se.run(costFunc,feed_dict={xInput:dataBeam.reshape(numItem,weightSize[0]),yInput:dataLattice.reshape(numItem,weightSize[-1])})
        costRec[_]=T2
        print str(np.round((np.float32(_)/np.float32(numRun))*100.))+'%'

plt.close('all')
plt.figure(1)
x=np.linspace(0,numRun,numRun)
plt.subplot(231)
xRatioStart=0.
xStart=np.int32(xRatioStart*numRun)
plt.plot(x[xStart::],costRec[xStart::])

plt.subplot(232)
xRatioStart=0.3
xStart=np.int32(xRatioStart*numRun)
plt.plot(x[xStart::],costRec[xStart::])

plt.subplot(233)
xRatioStart=0.6
xStart=np.int32(xRatioStart*numRun)
plt.plot(x[xStart::],costRec[xStart::])

plt.subplot(234)
xRatioStart=0.8
xStart=np.int32(xRatioStart*numRun)
plt.plot(x[xStart::],costRec[xStart::])

plt.subplot(235)
xRatioStart=0.9
xStart=np.int32(xRatioStart*numRun)
plt.plot(x[xStart::],costRec[xStart::])

plt.subplot(236)
xRatioStart=0.90
xStart=np.int32(xRatioStart*numRun)
plt.plot(x[xStart::],costRec[xStart::])













