#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 17:36:43 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:


"""


import tensorflow as tf

lambda1=tf.Variable(tf.random_uniform([1,1]),dtype=tf.float32)
lambda2=tf.Variable(tf.random_uniform([1,1]),dtype=tf.float32)

O=tf.reshape(tf.constant(0,tf.float32),[1,1])

LambdaR1=tf.concat([lambda1,O],0)
LambdaR2=tf.concat([O,lambda2],0)
LambdaR=tf.concat([LambdaR1,LambdaR2],1)


sess=tf.Session()

sess.run(tf.global_variables_initializer())

print(sess.run(LambdaR))

#print(LambdaR1.eval(sess))

