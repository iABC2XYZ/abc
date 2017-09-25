#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:37:16 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    Check that the Distribution generation method is right.

"""


import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np



plt.close('all')

emitX=1
alphaX=-0.
betaX=1.
gammaX=(1.+alphaX**2)/betaX

sigmaX=np.array([[betaX,-alphaX],[-alphaX,gammaX]])*emitX;

numPart=np.int32(1e5);
X=np.random.multivariate_normal([0.,0.],sigmaX,numPart).T

plt.figure(1)
plt.plot(X[0,:],X[1,:],'.')



##


def WeightP(shape):
    initial=tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)




P_1=WeightP([2,2])


xI=tf.placeholder(tf.float32,[2,None])

xO=tf.matmul(P_1,xI)

xR=tf.reduce_mean(xO[0]**2)*tf.reduce_mean(xO[1]**2)

#xR=(xO[0]**2)*(xO[1]**2)
lossXR=(xR-1.)**2

#xCov=tf.red


rateLearn=1.8e-4
optXR=tf.train.AdamOptimizer(rateLearn)

trainXR=optXR.minimize(lossXR)

meanLossXR=tf.reduce_mean(lossXR)


sess = tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))

sess.run(tf.global_variables_initializer())



sizeBatch=32

for _ in xrange(3000):
    
    startBatch=np.random.randint(0,high=numPart-sizeBatch-1)
    xFeed=X[:,startBatch:startBatch+sizeBatch:]
    
    sess.run(trainXR,feed_dict={xI:xFeed})
    
    
    #print(sess.run(LambdaR))
    #print('---------------------------')
    print(sess.run(meanLossXR,feed_dict={xI:X}),_)
    print('_______________________________________________')


    '''
    zReal=sess.run(xO,feed_dict={xI:X})
    
    
    plt.figure(2)
    plt.clf()
    plt.plot(zReal[0,:],zReal[1,:],'r.')
    plt.axis('equal')
    plt.pause(0.001)
    ''' 
    
LambdaRGet=sess.run(LambdaR)

print(LambdaRGet)
print('---------------------------')
print(1./(LambdaRGet[0,0]*LambdaRGet[1,1]))

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


