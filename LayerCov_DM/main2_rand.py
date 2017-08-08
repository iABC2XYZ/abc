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
    
    下一步，试试乱七八糟的分布，是否能得到类似的结果。
    
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

numPart=5000


xH=tf.placeholder(tf.float32, shape=(None, 1))
xpH=tf.placeholder(tf.float32, shape=(None, 1))

R=LayerCov(xH,xpH,wAlphaT,wGammaT,wEmitT)

lossR=R

optiR=tf.train.GradientDescentOptimizer(0.001)
trainR=optiR.minimize(lossR)

init=tf.global_variables_initializer()

sess=tf.Session()

sess.run(init)

paraPrint=[wAlphaT,wGammaT,wEmitT]


arrayAlphaT=[]
arrayGammaT=[]
arrayEmitT=[]

for _ in range(1000):
    x=np.random.rand((numPart))*2-1.
    xp=np.random.rand((numPart))*2-1.
    
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

alphaTTest=arrayAlphaT[-1]
gammaTTest=arrayGammaT[-1]
betaTTest=(1.+alphaTTest**2)/gammaTTest
covTest=np.array([[betaTTest[0],-alphaTTest[0]],[-alphaTTest[0],gammaTTest[0]]])
meanTest=np.array([0.,0.])
xTest,yTest=np.random.multivariate_normal(meanTest,covTest,numPart).T


plt.figure(10)
plt.clf()
plt.hold
plt.plot(x,xp,'b.')
plt.plot(xTest,yTest,'.r')
plt.plot(x,xp,'b.')





