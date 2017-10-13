#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 12:11:31 2017

@author: A
"""
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt



constEmit=tf.constant([1.,1.,1.])
numPart=np.int32(1e5)

WeightsBetaT=tf.Variable(tf.random_uniform(shape=[3],minval=0.1,maxval=1.))
WeightsAlphaT=tf.Variable(tf.random_uniform(shape=[3],minval=-1.,maxval=1.))

weightsGammaT=tf.div(1.+tf.square(WeightsAlphaT),WeightsBetaT)

xCov=[[WeightsBetaT[0],-WeightsAlphaT[0]],[-WeightsAlphaT[0],weightsGammaT[0]]]

xCov=[[1.,0.5],[0.5,1.25]]

eXCov,vXCov=tf.self_adjoint_eig(xCov)
x0=tf.random_normal([2,numPart])
matMul=tf.diag(tf.sqrt(eXCov))
#matMul=tf.diag(eXCov)
x=tf.matmul(matMul,tf.matmul(vXCov,x0))





init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print sess.run(vXCov)
    print sess.run(tf.matmul(vXCov,vXCov))
    print sess.run(tf.matmul(vXCov,tf.transpose(vXCov)))
    print sess.run(tf.matmul(vXCov,tf.matmul(tf.diag(eXCov),tf.transpose(vXCov))))

    
    '''
    print sess.run(WeightsBetaT)
    print sess.run(WeightsAlphaT)
    print sess.run(weightsGammaT)
    print sess.run(constEmit)    
    print('*************')
    
    
    print sess.run(xCov)
    print "____________"
    
    
    print sess.run(eXCov)
    print('vXCov')
    print sess.run(vXCov)
    
    print('+++++++++++++')
    '''
    xPlot=sess.run(x)
    print np.cov(xPlot)
    
    plt.plot(xPlot[0,:],xPlot[1,:],'.')
    
    '''
    print('^^^^^^^^^^^^^^^^^')
    print(sess.run(c))
    '''
    
    #print sess.run(WeightsBetaT)
    #print sess.run(WeightsAlphaT)
    #print sess.run(weightsGammaT)
    #print sess.run(constEmit)
    '''
    print('xCov')
    print sess.run(xCov)
    print('eXCov')
    print sess.run(eXCov)
    print('vXCov')
    print sess.run(vXCov)
    print('matMul')
    print sess.run(matMul)
    x=sess.run(x0)
    plt.plot(x[0,:],x[1,:],'.')
    
    
    #print sess.run(matMul)
    '''


print "OK"



