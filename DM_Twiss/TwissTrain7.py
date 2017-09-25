#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:37:16 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    Train one complex objective, not better.
    

"""


import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np



plt.close('all')

emitX=1
alphaX=-15.
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

x2=tf.reduce_mean(xO[0]**2)
xp2=tf.reduce_mean(xO[1]**2)
xxp=tf.reduce_mean(xO[0]*xO[1])


lossX2=(x2-1.)**2
lossXp2=(xp2-1.)**2
lossXxp=xxp**2

rX2=tf.random_normal([1],mean=1.0)
rXp2=tf.random_normal([1],mean=1.0)
rXxp=tf.random_normal([1],mean=1.0)

#lossTotal=rX2[0]*lossX2+rXp2*lossXp2+lossXxp
#lossTotal=(rX2[0]*lossX2+1.)*(rXp2*lossXp2+1.)*(rXxp*lossXxp+1.)
lossTotal=tf.reduce_mean((xO[0]**2*xO[1]**2-1.)**2)


#xCov=tf.red


rateLearn=5e-4
optTotal=tf.train.AdamOptimizer(rateLearn)
trainTotal=optTotal.minimize(lossTotal)

sess = tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))

sess.run(tf.global_variables_initializer())



sizeBatch=1024

for _ in xrange(8000):
    
    startBatch=np.random.randint(0,high=numPart-sizeBatch-1)
    xFeed=X[:,startBatch:startBatch+sizeBatch:]
    
    sess.run(trainTotal,feed_dict={xI:xFeed})

    
    
    #print(sess.run(LambdaR))
    #print('---------------------------')
    print(sess.run(lossTotal,feed_dict={xI:X}),_)
    print('_______________________________________________')

'''
    if ( _ % 100 ==0):
        zReal=sess.run(xO,feed_dict={xI:X})
        
        
        plt.figure(20)
        plt.plot(zReal[0,:],zReal[1,:],'r.')
        plt.axis('equal')
        plt.pause(0.2)
'''     



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


