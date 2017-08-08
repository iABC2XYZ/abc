#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 08:48:19 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:

    可以找到Twiss参数
    就是通过椭圆-》圆，然后x**2+xp**2最小，即可得到Twiss。
    如果将Emit钉死，则寻找很慢，需要更小的学习因子。
    如果Emit是活的，那么可以使用更大一些的学习因子。
    复杂系统下，学习因子要小。
    
    下一步，试试乱七八糟的分布，是否能得到类似的结果。（main2_rand.py）
    
"""
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

plt.close('all')

def LayerCov(x,xp,wAlphaT,wGammaT,wEmitT):

    XP=1./tf.sqrt(wGammaT)/tf.sqrt(wEmitT)*xp
    X=tf.sqrt(wGammaT)/tf.sqrt(wEmitT)*x+wAlphaT*XP
    
    R2=tf.square(X)+tf.square(XP)
    
    R=tf.sqrt(R2)
    return R


wAlphaT=tf.Variable([-0.])
wGammaT=tf.Variable([1.])
wEmitT=tf.Variable([4.])
#wEmitT=tf.constant([1.])

meanX=[0,0]
emitT=4.
gammaT=6.
alphaT=-0.8
betaT=(1.+alphaT**2)/gammaT

covX=np.array([[betaT,-alphaT],[-alphaT,gammaT]])*emitT

numPart=5000


xH=tf.placeholder(tf.float32, shape=(None, 1))
xpH=tf.placeholder(tf.float32, shape=(None, 1))

R=LayerCov(xH,xpH,wAlphaT,wGammaT,wEmitT)

lossR=R

optiR=tf.train.GradientDescentOptimizer(0.00001)    #Emit 不定： 0.001   ， 钉死：0.00001
trainR=optiR.minimize(lossR)

init=tf.global_variables_initializer()

sess=tf.Session()

sess.run(init)

paraPrint=[wAlphaT,wGammaT,wEmitT]


arrayAlphaT=[]
arrayGammaT=[]
arrayEmitT=[]

for _ in range(1000):
    x,xp=np.random.multivariate_normal(meanX,covX,numPart).T
    x=x[:,np.newaxis]
    xp=xp[:,np.newaxis]
    
    sess.run(trainR,feed_dict={xH:x,xpH:xp})
    paraTwiss=sess.run(paraPrint)
    arrayAlphaT.append(paraTwiss[0])
    arrayGammaT.append(paraTwiss[1])
    arrayEmitT.append(paraTwiss[2])

plt.figure(1)
plt.clf()
plt.hold
plt.plot(arrayAlphaT,'b.')
plt.plot(arrayGammaT,'g.')
plt.plot(arrayEmitT,'r.')

plt.show()











