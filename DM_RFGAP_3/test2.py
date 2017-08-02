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
numPart=np.int32(5000)
x,xp,y,yp,z,zp=PartGen(emitT,numPart)

numPart_2=np.int32(numPart/2)
x=x.reshape((numPart_2,2))
xp=xp.reshape((numPart_2,2))
y=y.reshape((numPart_2,2))
yp=yp.reshape((numPart_2,2))
z=z.reshape((numPart_2,2))
zp=zp.reshape((numPart_2,2))


print(z.shape)

xS=tf.placeholder(tf.float32,[None,2])
xpS=tf.placeholder(tf.float32,[None,2])
yS=tf.placeholder(tf.float32,[None,2])
ypS=tf.placeholder(tf.float32,[None,2])
zS=tf.placeholder(tf.float32,[None,2])
zpS=tf.placeholder(tf.float32,[None,2])

Prediction,wAlphaT,wBetaT=TwissOutputLayer(xS,xpS,yS,ypS,zS,zpS)

loss=Prediction

trainLoss=tf.train.GradientDescentOptimizer(0.01).minimize(loss)

init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(10):
        print(sess.run(wAlphaT))
        print(sess.run(wBetaT))
        print(sess.run(Prediction))
        #sess.run(trainLoss,feed_dict={xS:x,xpS:xp,yS:y,ypS:yp,zS:z,zpS:zp})
        #print(sess.run(loss,feed_dict={xS:x,xpS:xp,yS:y,ypS:yp,zS:z,zpS:zp}))
        print('_____')




print('OK')















