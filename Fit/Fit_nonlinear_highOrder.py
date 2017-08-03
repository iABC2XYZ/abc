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

x_data=np.random.rand(10000).astype(np.float32)
y_data=0.1*x_data**2+0.3

Weights=tf.Variable(tf.zeros([5]))

y=Weights[4]*x_data**4+Weights[3]*x_data**3+Weights[2]*x_data**2+Weights[1]*x_data+Weights[0]

loss=tf.reduce_mean(tf.square(y-y_data))

optimizer=tf.train.GradientDescentOptimizer(0.2)

train=optimizer.minimize(loss)

init= tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(4500):
        sess.run(train)
        yFit=sess.run(y)
        print(sess.run(loss))
        print(sess.run(Weights))
        print('_________________')

plt.figure(1)
plt.plot(x_data,y_data,'.')
plt.hold('on')
plt.plot(x_data,yFit,'r.')


