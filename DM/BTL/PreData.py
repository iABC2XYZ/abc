#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:51:40 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:


"""

import numpy as np
def MapQuad(K,L):
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


