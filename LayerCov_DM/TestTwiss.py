#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 09:59:39 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:


"""

import matplotlib.pyplot as plt
import numpy as np

def M(L,x,xp):
    #x+=L*xp
    xp-=L*x
    return x,xp

def R(x,y):
    R2=x**2+xp**2
    R=np.sqrt(np.mean(R2))
    return R


meanX=[0,0]
emitT=6.
gammaT=8.
alphaT=-0.
betaT=(1.+alphaT**2)/gammaT

covX=np.array([[betaT,-alphaT],[-alphaT,gammaT]])*emitT

numPart=5000

x,xp=np.random.multivariate_normal(meanX,covX,numPart).T

arrayR=[]
L=1e-3
for _ in range(1000):
    x,xp=M(L,x,xp)
    rMean=R(x,xp)
    arrayR.append(rMean)
    
plt.figure(1)
plt.plot(arrayR)

plt.show()