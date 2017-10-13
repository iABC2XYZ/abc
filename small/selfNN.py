#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 12:11:31 2017

@author: A
"""
import numpy as np
import tensorflow as tf


def add_layer(inputs, in_size,out_size,activiation_function=None):
    Weights=tf.Variable(tf.random_normal([in_size,out_size]))
    biases=tf.Variable(tf.zeros([1,out_size])+0.1)
    Wx_plus_b=tf.matmul(inputs,Weights)+biases
    if activiation_function is None:
        outputs=Wx_plus_b
    else:
        outputs=activiation_function(Wx_plus_b)
    return outputs



x_data=np.linspace(-1,1,300)[:,np.newaxis]
noise=np.random.normal(0,0.05,x_data.shape)
y_data=np.square(x_data)-0.5+noise


xs=tf.placeholder(tf.float32,[None,1])
ys=tf.placeholder(tf.float32,[None,1])

l1=add_layer(xs,1,10,activiation_function=tf.nn.relu)


prediction=add_layer(l1,10,1,activiation_function=None)

loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))




loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))


train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)



init=tf.global_variables_initializer()



#sess = tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
with tf.Session() as sess:
    with tf.device("/gpu:0"):
        sess.run(init)
        for _ in range(1000):
            sess.run(train_step,feed_dict={xs : x_data, ys : y_data})
            if  ( _  % 50==0):
                print(sess.run(loss,feed_dict={xs : x_data, ys : y_data}))




print "OK"
