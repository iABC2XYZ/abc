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

from Orth import LambdaR,OrthTrans
from TFOrth import TFLambdaR,TFOrthTrans

plt.close('all')

emitX=4.8
alphaX=-2.3
betaX=15.3
gammaX=(1.+alphaX**2)/betaX

diagRX=LambdaR(emitX,alphaX,betaX,gammaX)

PX=OrthTrans(emitX,alphaX,betaX,gammaX)

numPart=np.int32(1e5)
Z=np.random.randn(2,numPart)

X=np.matmul(np.matmul(PX,np.linalg.inv(diagRX)),Z)


plt.figure(1)
plt.plot(X[0,:],X[1,:],'r.')
plt.axis('equal')


##


def WeightP(shape):
    initial=tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)

def WeightLambda2D():
    lambda1=tf.Variable(tf.random_uniform([1,1]),dtype=tf.float32)
    lambda2=tf.Variable(tf.random_uniform([1,1]),dtype=tf.float32)
    
    O=tf.reshape(tf.constant(0,tf.float32),[1,1])
    
    LambdaR1=tf.concat([lambda1,O],0)
    LambdaR2=tf.concat([O,lambda2],0)
    LambdaR=tf.concat([LambdaR1,LambdaR2],1)

    return LambdaR


P_1=WeightP([2,2])
LambdaR=WeightLambda2D()


xI=tf.placeholder(tf.float32,[2,None])

xL1=tf.matmul(P_1,xI)

xO=tf.matmul(LambdaR,xL1)

xR=xO[0]**2+xO[1]**2

lossXR=(xR-2.)**2


rateLearn=5e-4
optXR=tf.train.AdamOptimizer(rateLearn)

trainXR=optXR.minimize(lossXR)

meanLossXR=tf.reduce_mean(lossXR)


sess = tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))

sess.run(tf.global_variables_initializer())




sizeBatch=64

for _ in xrange(30000):
    
    startBatch=np.random.randint(0,high=numPart-sizeBatch-1)
    xFeed=X[:,startBatch:startBatch+sizeBatch:]
    
    sess.run(trainXR,feed_dict={xI:xFeed})
    
    
    #print(sess.run(LambdaR))
    #print('---------------------------')
    print(sess.run(meanLossXR,feed_dict={xI:X}))
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






'''
print(sess.run(P_1))

print(sess.run(LambdaR))


print(sess.run(xR,feed_dict={xI:X}))
'''









'''
wEmit=tf.Variable([emitX])
wAlpha=tf.Variable([alphaX])
wBeta=tf.Variable([betaX])
wGamma=tf.Variable([gammaX])
'''

'''
wEmit=tf.Variable([13.])
wAlpha=tf.Variable([1.3])
wBeta=tf.Variable([0.5])
#wGamma=tf.Variable([0.5])
wGamma=(1.+wAlpha**2)/wBeta


xH=tf.placeholder(tf.float32,[2,None])

diagR,diagRT=TFLambdaR(wEmit,wAlpha,wBeta,wGamma)
P,PI=TFOrthTrans(wEmit,wAlpha,wBeta,wGamma)

zH=tf.matmul(tf.matmul(diagR,PI),xH)

R=zH[0]**2+zH[1]**2
#lossR=tf.abs(R-2.e-6)
lossR=R

optR=tf.train.GradientDescentOptimizer(0.01)

trainR=optR.minimize(lossR)

sess=tf.Session()

sess.run(tf.global_variables_initializer())
#sess.run(diagR)

print(sess.run(R,feed_dict={xH:X}))




numIter=10
recEmit=np.zeros(numIter)
recAlpha=np.zeros(numIter)
recBeta=np.zeros(numIter)
recGamma=np.zeros(numIter)
recLoss=np.zeros(numIter)

for _ in xrange(numIter):
    sess.run(trainR,feed_dict={xH:X})
    recEmit[_]=sess.run(wEmit)
    recAlpha[_]=sess.run(wAlpha)
    recBeta[_]=sess.run(wBeta)
    recGamma[_]=sess.run(wGamma)
    recLoss[_]=sess.run(tf.reduce_mean(lossR))


print(recEmit)
print(recAlpha)
#print(sess.run(R,feed_dict={xH:X}))

plt.figure('emit')
plt.plot(recEmit)

plt.figure('alpha')
plt.plot(recAlpha)

plt.figure('beta')
plt.plot(recBeta)

plt.figure('gamma')
plt.plot(recGamma)

plt.figure('Loss')
plt.plot(recLoss)

'''

'''
zGet=sess.run(zH,feed_dict={xH:X})
print(sess.run(lossR,feed_dict={xH:X}))
'''
'''
plt.figure('Check')
plt.hold('on')
plt.plot(Z[0,:],Z[1,:],'bo')
plt.plot(zGet[0,:],zGet[1,:],'r.')
plt.axis('equal')
'''


'''
print(sess.run(wEmit))
print(sess.run(wAlpha))
print(sess.run(wBeta))
print(sess.run(wGamma))

print(sess.run(diagR))
print(sess.run(diagRT))
'''
#print(PX)
#print(sess.run(P))
#print(sess.run(zH,feed_dict={xH:X}))
