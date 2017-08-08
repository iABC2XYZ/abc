#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:10:29 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    椭圆到圆

"""

import matplotlib.pyplot as plt
import numpy as np



meanX=[0,0]
emitT=4.
gammaT=4.
alphaT=-0.
betaT=(1.+alphaT**2)/gammaT

covX=np.array([[betaT,-alphaT],[-alphaT,gammaT]])*emitT

numPart=5000

x,xp=np.random.multivariate_normal(meanX,covX,numPart).T

XP=1./np.sqrt(emitT*gammaT)*xp
X=np.sqrt(gammaT/emitT)*x+alphaT*XP


XP2=1./np.sqrt(gammaT)*xp
X2=np.sqrt(gammaT)*x+alphaT*XP

plt.figure(1)
plt.plot(x,xp,'.')
plt.axis('equal')

plt.figure(2)
plt.plot(X,XP,'.')
plt.axis('equal')


plt.figure(3)
plt.plot(X2,XP2,'.')
plt.axis('equal')














