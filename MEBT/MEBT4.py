#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：
    hDCmrad和vDCmrad是输入的二极校正铁量，限制范围是[-10,10]。
    通过调用　xBPM,yBPM= Simulator(hDCmrad,vDCmrad)　可以获得５个ｚ点处ＢＰＭ测得的束流在ｘ和ｙ方向的位置。
    
    备注：系统为简化系统

"""
import numpy as np

def GammaT(alphaT,betaT):
    gammaT=(1.+alphaT**2)/betaT
    return gammaT

def TwissT(alphaT,betaT):
    gammaT=GammaT(alphaT,betaT)
    sigmaT=np.array([[betaT,-alphaT],[-alphaT,gammaT]])
    return sigmaT


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



def CalBTL(numSample,beamError,xError,yError,quadL,quadK,driftL,hDCmrad,vDCmrad):
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
    
    xT=np.array([[beamError[0]],[beamError[1]]])
    yT=np.array([[beamError[2]],[beamError[3]]])
    
    X=np.zeros([numSample])
    XP=np.zeros([numSample])
    Y=np.zeros([numSample])
    YP=np.zeros([numSample])
    
    kLocal0=0
    for iL in range(numSample):
        if iL==0:
            X[0]=xT[0,0]
            XP[0]=xT[1,0]
            Y[0]=yT[0,0]
            YP[0]=yT[1,0]
        kLocal=K[iL]
        if np.abs(kLocal)<1e-6:
            Mx=MapDrift(dL)
            My=Mx
        else:
            Mx=MapQuad(kLocal,dL)
            My=MapQuad(-kLocal,dL)
        
        xT[0,0]-=xError[iCell]
        yT[0,0]-=yError[iCell]
        xT=np.matmul(Mx,xT)
        yT=np.matmul(My,yT)
        xT[0,0]+=xError[iCell]
        yT[0,0]+=yError[iCell]
        
        
        if (np.abs(kLocal0)<1e-6) and (np.abs(kLocal)>1e-6):
            xT[1,0]+=hDCmrad[iCell]
            yT[1,0]+=vDCmrad[iCell]
        
        kLocal0=kLocal


        
        X[iL]=xT[0,0]
        XP[iL]=xT[1,0]
        Y[iL]=yT[0,0]
        YP[iL]=yT[1,0]
    
    
    
    return Z,X,XP,Y,YP




def Simulator(hDCmrad,vDCmrad):
    
    numSample=np.int32(1e3)
    
    x0=2.
    xp0=0.
    y0=-1.2
    yp0=0.
    beamError=[x0,xp0,y0,yp0]
    
    quadL=np.array([0.0818,0.1036,0.0818,0.08196,0.08203,0.08204,0.08212])
    quadK=-np.array([45.482,-64.085,57.96,1e-5,-45.227,64.017,-25.197])
    driftL=np.array([0.25,0.09,0.09,0.34,0.6075,0.09,0.09,0.56])
    xError=np.array([-0.41, 0.11, 0.06, 0.06, 0.13, -0.05, -0.24])
    yError=np.array([0.27, -0.33, -0.01, -0.08, -0.12, -0.07, -0.11])
    zBPM=np.array([0.29,1.07,1.7575,2.0975,2.53])
    
    Z,X,XP,Y,YP=CalBTL(numSample,beamError,xError,yError,quadL,quadK,driftL,hDCmrad,vDCmrad)

    xBPM,yBPM=np.zeros((5)),np.zeros((5))
    for iBPM in range(5):
        idBPM=np.argmin(np.abs(Z-zBPM[iBPM]))
        xBPM[iBPM]=X[idBPM]
        yBPM[iBPM]=Y[idBPM]
    return xBPM,yBPM


hDCmrad=(np.random.random([7])*2-1)*10
vDCmrad=(np.random.random([7])*2-1)*10

xBPM,yBPM= Simulator(hDCmrad,vDCmrad)






