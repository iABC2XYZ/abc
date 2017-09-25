#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:37:16 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    旋转使得变换。
    

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


w=tf.Variable(tf.random_normal([1,1]))
w1=tf.cos(w)
w2=tf.sin(w)


P_Row_1=tf.concat([w1,-w2],0)

P_Row_2=tf.concat([w2,w1],0)


P=tf.concat([P_Row_1,P_Row_2],1)




xI=tf.placeholder(tf.float32,[2,None])

xO=tf.matmul(P,xI)

xxp=tf.reduce_mean(xO[0]*xO[1])


lossAlpha=xxp**2


rateLearn=1e-4
optTotal=tf.train.AdamOptimizer(rateLearn)
trainAlpha=optTotal.minimize(lossAlpha)

sess = tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))

sess.run(tf.global_variables_initializer())



sizeBatch=64

for _ in xrange(8000):
    
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


