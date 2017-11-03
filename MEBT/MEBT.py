#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@author: Jiang Peiyong 
 email:  jiangpeiyong@impcas.ac.cn
 
"""


import numpy as np
from scipy import interpolate
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


def RandSigma(betaMax):
    betaT=np.random.random()*betaMax
    alphaT=np.random.random()*np.sign(np.random.random()-0.5)
    gammaT=(1.+alphaT**2)/betaT
    
    sigmaT=np.array([[betaT,-alphaT],[-alphaT,gammaT]])
    return sigmaT


def RandLatticeBPL(numQuad):
    quadL=np.random.random([numQuad])
    quadK=np.random.random([numQuad])-0.5
    driftL=np.random.random([numQuad+1])
    
    return quadL,quadK,driftL

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
        
        betaX[iL]=sigmaTx[0,0]
        betaY[iL]=sigmaTy[0,0]
    
    
    
    return Z,betaX,betaY

def RandItemSingle(numSample,numQuadHigh):
    numQuad=np.random.randint(0,high=numQuadHigh)
    
    flagEle=np.zeros([numSample])
    flagEle[0:numQuad+1:2]=1     # D
    flagEle[1:numQuad:2]=4     # Q
    
    quadL,quadK,driftL=RandLatticeBPL(numQuad)
    
    betaMax=100.
    sigmaTx=RandSigma(betaMax)
    sigmaTy=RandSigma(betaMax)
    Z,betaX,betaY=CalBTL(numSample,sigmaTx,sigmaTy,quadL,quadK,driftL)
    
    dataLattice=np.zeros([numQuadHigh,3])
    dataBeam=np.zeros([numSample,4])
    
    dataLattice[0:numQuad+1,0]=driftL
    dataLattice[0:numQuad,1]=quadK
    dataLattice[0:numQuad,2]=quadL
    
    dataBeam[:,0]=Z
    dataBeam[:,1]=betaX
    dataBeam[:,2]=betaY
    dataBeam[:,3]=flagEle
    
    return dataLattice,dataBeam

def RandItemMulti(numItem,numSample,numQuadHigh):
    dataLattice=np.zeros([numItem,numQuadHigh,3])
    dataBeam=np.zeros([numItem,numSample,4])
    for iItem in range(numItem):
        dataLatticeSingle,dataBeamSingle=RandItemSingle(numSample,numQuadHigh)
        dataLattice[iItem,:,:]=dataLatticeSingle
        dataBeam[iItem,:,:]=dataBeamSingle
    return dataLattice,dataBeam



def DealBeta(zGiven,betaXGiven,betaYGiven,numSample,numQuad):
    
    interpX=interpolate.interp1d(zGiven,betaXGiven,kind='cubic')
    interpY=interpolate.interp1d(zGiven,betaYGiven,kind='cubic')

    Z=np.linspace(zGiven[0],zGiven[-1],numSample)
    
    betaX=interpX(Z)
    betaY=interpY(Z)
    
    flagEle=np.zeros([numSample])
    flagEle[0:numQuad+1:2]=1     # D
    flagEle[1:numQuad:2]=4     # Q
    
    dataBeam=np.zeros([numSample,4])
    
    dataBeam[:,0]=Z
    dataBeam[:,1]=betaX
    dataBeam[:,2]=betaY
    dataBeam[:,3]=flagEle
    
    return dataBeam


zGiven=np.array([0,2,3,5,6,7,9,12,15,16,17])
betaXGiven=np.sin(zGiven+np.random.random(np.size(zGiven)))+3
betaYGiven=-np.sin(zGiven+np.random.random(np.size(zGiven)))+3

plt.figure('betaGiven')
plt.clf()
plt.hold
plt.plot(zGiven,betaXGiven)
plt.plot(zGiven,betaYGiven)

numSample=2**8
numQuad=5
dataBeam=DealBeta(zGiven,betaXGiven,betaYGiven,numSample,numQuad)

Z=dataBeam[:,0]
betaX=dataBeam[:,1]
betaY=dataBeam[:,2]
flagEle=dataBeam[:,3]

plt.figure('beta')
plt.clf()
plt.hold
plt.plot(Z,betaX)
plt.plot(Z,betaY)

plt.figure('flagEle')
plt.plot(flagEle)

def DealUnpack(dataBeam,dataLattice):
    Z=dataBeam[0:2,0]
    betaX=dataBeam[0:2,1]
    betaY=dataBeam[0:2,2]
    flagEle=dataBeam[:,3]
    
    numQuad=np.sum(flagEle>0)
    
    numQuadHigh=len(dataLattice[:,0])
    
    driftL=dataLattice[0:numQuad+1,0]
    quadK=dataLattice[0:numQuad,1]
    quadL=dataLattice[0:numQuad,2]
    
    numSample=len(flagEle)
    
    dZ=Z[1]-Z[0]
    dBetaX=betaX[1]-betaX[0]
    dBetaY=betaY[1]-betaY[0]
    alphaX=-dBetaX/dZ
    alphaY=-dBetaY/dZ
    gammaX=(1.+alphaX**2)/betaX[0]
    gammaY=(1.+alphaY**2)/betaY[0]
    
    sigmaTx=np.array([[betaX[0],-alphaX],[-alphaX,gammaX]])
    sigmaTy=np.array([[betaY[0],-alphaY],[-alphaY,gammaY]])
    

    return numSample,numQuadHigh,sigmaTx,sigmaTy,quadL,quadK,driftL
    
numItem=64
numSample=8   
numQuadHigh=8

dataLattice,dataBeam=RandItemSingle(numSample,numQuadHigh)
    
numSample,numQuadHigh,sigmaTx,sigmaTy,quadL,quadK,driftL=DealUnpack(dataBeam,dataLattice)
  
print(numSample)  
print(numSample)
print 'sigmaTx'
print sigmaTx
print 'sigmaTy'
print sigmaTy
print 'quadL'
print quadL
print 'quadK'
print quadK
print 'driftL'
print driftL
print 'dataLattice'
print dataLattice

def RoundItemSingle(numSample,numQuadHigh,sigmaTx,sigmaTy,quadL,quadK,driftL):
    quadL=quadL*np.abs(1.+np.random.randn()/3.)
    quadK=quadK*(1.+np.random.randn()/3.)
    driftL=driftL*np.abs(1.+np.random.randn()/3.)
    
    Z,betaX,betaY=CalBTL(numSample,sigmaTx,sigmaTy,quadL,quadK,driftL)
    
    dataLattice=np.zeros([numQuadHigh,3])
    dataBeam=np.zeros([numSample,4])
    
    numQuad=len(quadK)
    dataLattice[0:numQuad+1,0]=driftL
    dataLattice[0:numQuad,1]=quadK
    dataLattice[0:numQuad,2]=quadL
    
    flagEle=np.zeros([numSample])
    flagEle[0:numQuad+1:2]=1     # D
    flagEle[1:numQuad:2]=4     # Q
    
    dataBeam[:,0]=Z
    dataBeam[:,1]=betaX
    dataBeam[:,2]=betaY
    dataBeam[:,3]=flagEle
    
    return dataLattice,dataBeam
    
dataLattice,dataBeam= RoundItemSingle(numSample,numQuadHigh,sigmaTx,sigmaTy,quadL,quadK,driftL)   
    
print 'dataLattice'
print dataLattice
    

def RoundItemMulti(numItem,numSample,numQuadHigh,sigmaTx,sigmaTy,quadL,quadK,driftL):
    dataLattice=np.zeros([numItem,numQuadHigh,3])
    dataBeam=np.zeros([numItem,numSample,4])
    for iItem in range(numItem):
        dataLatticeSingle,dataBeamSingle= RoundItemSingle(numSample,numQuadHigh,sigmaTx,sigmaTy,quadL,quadK,driftL)   
        dataLattice[iItem,:,:]=dataLatticeSingle
        dataBeam[iItem,:,:]=dataBeamSingle
    return dataLattice,dataBeam


dataLattice,dataBeam=RoundItemMulti(numItem,numSample,numQuadHigh,sigmaTx,sigmaTy,quadL,quadK,driftL)
print 'dataLattice'
print dataLattice

print 'dataBeam'
print dataBeam


def RoundItemMultiPack(numItem,dataBeamSingle,dataLatticeSingle):
    numSample,numQuadHigh,sigmaTx,sigmaTy,quadL,quadK,driftL=DealUnpack(dataBeamSingle,dataLatticeSingle)
    dataLattice,dataBeam=RoundItemMulti(numItem,numSample,numQuadHigh,sigmaTx,sigmaTy,quadL,quadK,driftL)
    return dataLattice,dataBeam

dataLatticeSingle,dataBeamSingle=RandItemSingle(numSample,numQuadHigh)
    
dataLattice,dataBeam=RoundItemMultiPack(numItem,dataBeamSingle,dataLatticeSingle)

print '+'*180
print dataLattice
print '-'*180
print dataBeam









