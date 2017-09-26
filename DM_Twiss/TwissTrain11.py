#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:37:16 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    旋转+拉伸：Qinqing  AdadeltaOptimizer
    

"""


import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np



plt.close('all')

emitX=12
alphaX=-10.
betaX=13.
gammaX=(1.+alphaX**2)/betaX

sigmaX=np.array([[betaX,-alphaX],[-alphaX,gammaX]])*emitX;

numPart=np.int32(1e5);
X=np.random.multivariate_normal([0.,0.],sigmaX,numPart).T

plt.figure(1)
plt.plot(X[0,:],X[1,:],'.')

##


w1=tf.Variable(tf.random_normal([1,1]))
w2=tf.Variable(tf.random_normal([1,1]))
O=tf.constant([0.],shape=[1,1])


P_Row_1=tf.concat([w1,w1*w2],0)

P_Row_2=tf.concat([O,1./w1],0)


P=tf.concat([P_Row_1,P_Row_2],1)




xI=tf.placeholder(tf.float32,[2,None])

xO=tf.matmul(P,xI)


xR=xO[0]**2+xO[1]**2



lossR=xR

rateLearn=8
optMethod=tf.train.AdadeltaOptimizer(rateLearn)
train=optMethod.minimize(lossR)



sess = tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))

sess.run(tf.global_variables_initializer())



sizeBatch=16

for _ in xrange(20000):
    
    pickBatch=np.int32(np.random.rand(sizeBatch)*numPart)
    xFeed=X[:,pickBatch]
    
    sess.run(train,feed_dict={xI:xFeed})



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


xOringinCov=np.cov(X)
emitXOrigin=np.sqrt(np.linalg.det(xOringinCov))


zRealCov=np.cov(zReal)
emitXReal=np.sqrt(np.linalg.det(zRealCov))


print('+++++++++++++++++++')
print(sess.run(P))
print('_________________________')

print(xOringinCov)

print(emitXOrigin)

print('________________________')

print(zRealCov)

print(emitXReal)


