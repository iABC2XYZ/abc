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

x_data=np.random.rand(100).astype(np.float32)
y_data=x_data*0.1+0.3

Weights=tf.Variable(tf.random_uniform([1],-1.,1.))
biases=tf.Variable(tf.zeros([1]))

y=Weights*x_data+biases

loss=tf.reduce_mean(tf.square(y-y_data))

optimizer=tf.train.GradientDescentOptimizer(0.2)

train=optimizer.minimize(loss)

init= tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(10):
        sess.run(train)
        print(sess.run(loss))
        print(sess.run(Weights),sess.run(biases))
        print('_________________')













