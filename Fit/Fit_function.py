#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 09:14:27 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
______________________________________________________


"""
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

x_data=np.linspace(-10,10,100)+np.random.randn()
y_data=0.1*x_data+0.3

Weights=tf.Variable(tf.zeros([2]))

def FitLayer(x_data,y_data,Weights):
    y=YLayer(x_data,Weights)
    loss=tf.reduce_mean(tf.square(y-y_data))
    return loss  

def YLayer(x_data,Weights):
    y=Weights[1]*x_data+Weights[0]
    return y  

y=YLayer(x_data,Weights)

loss=FitLayer(x_data,y_data,Weights)

optimizer=tf.train.GradientDescentOptimizer(0.2)

train=optimizer.minimize(loss)

init= tf.global_variables_initializer()

plt.figure(1)
plt.plot(x_data,y_data,'.')
plt.hold('on')
with tf.Session() as sess:
    sess.run(init)
    for _ in range(50):
        sess.run(train)
        yFit=sess.run(y)
        print(sess.run(loss))
        print(sess.run(Weights))
        print('_________________')


plt.figure(1)
plt.plot(x_data,y_data,'.')
plt.hold('on')
plt.plot(x_data,yFit,'r.')


























