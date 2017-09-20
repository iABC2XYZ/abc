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

emitX=1.4
alphaX=-2.3
betaX=15.3
gammaX=(1.+alphaX**2)/betaX

diagRX=LambdaR(emitX,alphaX,betaX,gammaX)

PX=OrthTrans(emitX,alphaX,betaX,gammaX)

numPart=np.int32(1e1)
Z=np.random.randn(2,numPart)/1000.

X=np.matmul(np.matmul(PX,np.linalg.inv(diagRX)),Z)

'''
plt.figure(1)
plt.plot(X[0,:],X[1,:],'r.')
plt.axis('equal')
'''

##



'''
wEmit=tf.Variable([emitX])
wAlpha=tf.Variable([alphaX])
wBeta=tf.Variable([betaX])
wGamma=tf.Variable([gammaX])
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
