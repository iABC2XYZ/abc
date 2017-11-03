#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""


import numpy as np
import matplotlib.pyplot as plt

def MapQuad(K,L):
    # 生成四极铁的装配矩阵，其中K表示聚焦因子，L 表示四极铁的长度。
    K2=np.sqrt(np.abs(K*1.))
    K2_L=K2*L
    
    if K>0:
        C=np.cos(K2_L)
        S=np.sin(K2_L)/K2
        Sp=-np.sin(K2_L)*K2
    else:
        C=np.cosh(K2_L)
        S=np.sinh(K2_L)/K2
        Sp=np.sinh(K2_L)*K2
    
    M=np.array([[C,S],[Sp,C]])
    return M
            
def MapDrift(L):
    M=np.array([[1.,L],[0.,1.]])
    return M


def CalBTL(numSample,sigmaTx,sigmaTy,quadL,quadK,driftL):
    lenBTL=np.sum(quadL)+np.sum(driftL)
    
    nCell=len(quadK)
    kStart=np.zeros([nCell])
    kEnd=np.zeros([nCell])
    
    for iCell in range(nCell):
        if iCell==0:
            kStart[0]=driftL[0]
            kEnd[0]=kStart[0]+quadL[0]
            continue
        kStart[iCell]=kEnd[iCell-1]+driftL[iCell]
        kEnd[iCell]=kStart[iCell]+quadL[iCell]
    
    Z=np.linspace(0.,lenBTL,numSample)
    K=np.zeros([numSample])
    
    for iCell in range(nCell):
        K[(Z>=kStart[iCell]) * (Z<=kEnd[iCell])]=quadK[iCell]
    
    dL=lenBTL/(numSample-1.)
    alphaX=np.zeros([numSample])
    alphaY=np.zeros([numSample])
    betaX=np.zeros([numSample])
    betaY=np.zeros([numSample])
    
    for iL in range(numSample):
        if iL==0:
            betaX[0]=sigmaTx[0,0]
            betaY[0]=sigmaTy[0,0]
        kLocal=K[iL]
        if np.abs(kLocal)<1e-6:
            Mx=MapDrift(dL)
            My=Mx
        else:
            Mx=MapQuad(kLocal,dL)
            My=MapQuad(-kLocal,dL)
        sigmaTx=np.matmul(np.matmul(Mx,sigmaTx),Mx.T)
        sigmaTy=np.matmul(np.matmul(My,sigmaTy),My.T)
        
        alphaX[iL]=-sigmaTx[0,1]
        alphaY[iL]=-sigmaTy[0,1]
        betaX[iL]=sigmaTx[0,0]
        betaY[iL]=sigmaTy[0,0]
    
    
    
    return Z,alphaX,alphaY,betaX,betaY

def GammaT(alphaT,betaT):
    gammaT=(1.+alphaT**2)/betaT
    return gammaT

def TwissT(alphaT,betaT):
    gammaT=GammaT(alphaT,betaT)
    sigmaT=np.array([[betaT,-alphaT],[-alphaT,gammaT]])
    return sigmaT




numSample=np.int32(1e3)
#alphaX0=0.23
#alphaY0=-0.314
#betaX0=0.229
#betaY0=0.112

alphaX0=0.44632
alphaY0=-0.244
betaX0=0.3022
betaY0=0.151
sigmaT0x=TwissT(alphaX0,betaX0)
sigmaT0y=TwissT(alphaX0,betaX0)


quadL=np.array([0.0818,0.1036,0.0818,0.08196,0.08203,0.08204,0.08212])
quadK=-np.array([45.482,-64.085,57.96,0,-45.227,64.017,-25.197])
#quadK=-np.array([9.388,-12.24,9.388,0,10.02,-13.89,5.088])/0.2095134377
driftL=np.array([0.25,0.09,0.09,0.34,0.6075,0.09,0.09,0.56])



Z,alphaX,alphaY,betaX,betaY=CalBTL(numSample,sigmaT0x,sigmaT0y,quadL,quadK,driftL)

plt.close('all')
plt.figure(1)
plt.clf()
plt.hold
plt.subplot(211)
plt.plot(Z,betaX,'b.')
plt.grid('on')
plt.subplot(212)
plt.plot(Z,betaY,'r.')
plt.grid('on')


