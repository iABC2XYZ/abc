#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:37:16 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    拉神使得变换。
    

"""


import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np



plt.close('all')

emitX=12
alphaX=-10.
betaX=1300.
gammaX=(1.+alphaX**2)/betaX

sigmaX=np.array([[betaX,-alphaX],[-alphaX,gammaX]])*emitX;

numPart=np.int32(1e5);
X=np.random.multivariate_normal([0.,0.],sigmaX,numPart).T

plt.figure(1)
plt.plot(X[0,:],X[1,:],'.')



##


w11=tf.Variable(tf.random_normal([1,1]))
w12=tf.Variable(tf.random_normal([1,1]))

P_Row_1=tf.concat([w11,w12],0)

w21=1./w12
w22=tf.constant([0.],shape=[1,1])

P_Row_2=tf.concat([w21,w22],0)

P=tf.concat([P_Row_1,P_Row_2],1)




xI=tf.placeholder(tf.float32,[2,None])

xO=tf.matmul(P,xI)

xxp=tf.reduce_mean(xO[0]*xO[1])


lossAlpha=xxp**2


rateLearn=5e-3
optTotal=tf.train.AdamOptimizer(rateLearn)
trainAlpha=optTotal.minimize(lossAlpha)

sess = tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))

sess.run(tf.global_variables_initializer())



sizeBatch=32

for _ in xrange(5000):
    
    startBatch=np.random.randint(0,high=numPart-sizeBatch-1)
    xFeed=X[:,startBatch:startBatch+sizeBatch:]
    
    sess.run(trainAlpha,feed_dict={xI:xFeed})

    
    
    #print(sess.run(LambdaR))
    #print('---------------------------')
    print(sess.run(lossAlpha,feed_dict={xI:X}),_)
    print('_______________________________________________')



zReal=sess.run(xO,feed_dict={xI:X})


plt.figure(2)
plt.plot(zReal[0,:],zReal[1,:],'r.')
plt.axis('equal')



plt.figure(10)
plt.hold
plt.plot(zReal[0,:],zReal[1,:],'r.')
plt.plot(X[0,:],X[1,:],'b.')
#plt.plot(zReal[0,:],zReal[1,:],'r.')
plt.axis('equal')


plt.figure(11)
plt.hold
#plt.plot(zReal[0,:],zReal[1,:],'r.')
plt.plot(X[0,:],X[1,:],'b.')
plt.plot(zReal[0,:],zReal[1,:],'r.')
plt.axis('equal')


zRealCov=np.cov(zReal)
emitXReal=np.sqrt(np.linalg.det(zRealCov))

print(emitXReal)


