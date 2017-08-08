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

plt.close('all')

meanX=[0,0]
emitT=1.
gammaT=8.
alphaT=0.3
betaT=(1.+alphaT**2)/gammaT

covX=np.array([[betaT,-alphaT],[-alphaT,gammaT]])*emitT

numPart=5000

x,xp=np.random.multivariate_normal(meanX,covX,numPart).T

def M(x,xp,alphaT,gammaT):
    XP=1./np.sqrt(gammaT)*xp
    X=np.sqrt(gammaT)*x+alphaT*XP
    return X,XP


xArray=[]
xpArray=[]
numPoints=500
gammaTArray=np.linspace(1.e-1,18.,numPoints)
for _ in range(numPoints):
    X,XP=M(x,xp,alphaT,gammaTArray[_])
    xArray.append(np.mean(X**2))
    xpArray.append(np.mean(XP**2))
    
    
plt.figure(1)
plt.plot(gammaTArray,xArray)


plt.figure(2)
plt.plot(gammaTArray,xpArray)

plt.figure(3)
plt.plot(gammaTArray,np.array(xArray)+np.array(xpArray))



