#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 17:46:12 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
______________________________________________________


"""

from PartGen import PartGen
import numpy as np
import matplotlib.pyplot as plt
from NN_Layers import TwissOutputLayer
import tensorflow as tf

emitT=np.array([2.,2.,2.])
numPart=np.int32(1)
x,xp,y,yp,z,zp=PartGen(emitT,numPart)

x=x[:,np.newaxis]
xp=xp[:,np.newaxis]
y=y[:,np.newaxis]
yp=yp[:,np.newaxis]
z=z[:,np.newaxis]
zp=zp[:,np.newaxis]

xS=tf.placeholder(tf.float32,[None,1])
xpS=tf.placeholder(tf.float32,[None,1])
yS=tf.placeholder(tf.float32,[None,1])
ypS=tf.placeholder(tf.float32,[None,1])
zS=tf.placeholder(tf.float32,[None,1])
zpS=tf.placeholder(tf.float32,[None,1])

Prediction,wAlphaT,wBetaT=TwissOutputLayer(xS,xpS,yS,ypS,zS,zpS)

loss=Prediction

trainLoss=tf.train.GradientDescentOptimizer(0.01).minimize(loss)

init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(1000):
        sess.run(trainLoss,feed_dict={xS:x,xpS:xp,yS:y,ypS:yp,zS:z,zpS:zp})
        #print(sess.run(loss,feed_dict={xS:x,xpS:xp,yS:y,ypS:yp,zS:z,zpS:zp}))
        print(sess.run(wAlphaT))
        print(sess.run(wBetaT))
        print('_____')

print('OK')








