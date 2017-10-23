#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:10:52 2017

@author: e
"""
import numpy as np
from BetaGammaC import NP_Energy2BetaC_GammaC

def GammaT(alphaT,betaT):
    gammaT=(1.+alphaT**2)/betaT
    return gammaT

def SigmaT2D(alphaT,betaT):
    gammaT=GammaT(alphaT,betaT)
    sigmaT=np.array([[betaT,-alphaT],[-alphaT,gammaT]])
    return sigmaT

def SigmaT4D(alphaX,betaX,alphaY,betaY):
    xSigmaT,ySigmaT= SigmaT2D(alphaX,betaX), SigmaT2D(alphaY,betaY)
    O2=np.zeros((2,2))
    sigmaT=np.vstack((np.hstack((xSigmaT,O2)),np.hstack((O2,ySigmaT))))
    return sigmaT

def SigmaT6D(alphaX,betaX,alphaY,betaY,alphaZ,betaZ):
    xSigmaT,ySigmaT,zSigmaT= SigmaT2D(alphaX,betaX), SigmaT2D(alphaY,betaY),SigmaT2D(alphaZ,betaZ)
    O2=np.zeros((2,2))
    sigmaT=np.vstack((np.hstack((xSigmaT,O2,O2)),np.hstack((O2,ySigmaT,O2)),np.hstack((O2,O2,zSigmaT))))
    return sigmaT


def SigmaE2D(alphaT,betaT,emit):
    sigmaT=SigmaT2D(alphaT,betaT)
    sigmaE=sigmaT*emit
    return sigmaE

def SigmaE4D(alphaX,alphaY,betaX,betaY,emitX,emitY):
    xSigmaT,ySigmaT= SigmaT2D(alphaX,betaX), SigmaT2D(alphaY,betaY)
    xSigmaE,ySigmaE=xSigmaT*emitX,ySigmaT*emitY
    O2=np.zeros((2,2))
    sigmaE=np.vstack((np.hstack((xSigmaE,O2)),np.hstack((O2,ySigmaE))))
    return sigmaE

def SigmaE6D(alphaX,alphaY,alphaZ,betaX,betaY,betaZ,emitX,emitY,emitZ):
    xSigmaT,ySigmaT,zSigmaT= SigmaT2D(alphaX,betaX), SigmaT2D(alphaY,betaY),SigmaT2D(alphaZ,betaZ)
    xSigmaE,ySigmaE,zSigmaE=xSigmaT*emitX,ySigmaT*emitY,zSigmaT*emitZ
    O2=np.zeros((2,2))
    sigmaE=np.vstack((np.hstack((xSigmaE,O2,O2)),np.hstack((O2,ySigmaE,O2)),np.hstack((O2,O2,zSigmaE))))
    return sigmaE




def Mu2D(muX,muXP):
    muT=np.array([muX,muXP])
    return muT
def Mu4D(muX,muXP,muY,muYP):
    muT=np.array([muX,muXP,muY,muYP])
    return muT
def Mu6D(muX,muXP,muY,muYP,muZ,muZP):
    muT=np.array([muX,muXP,muY,muYP,muZ,muZP])
    return muT


def Emit_Norm2Geo(emitNorm,energyMeV):
    emitGeo=np.empty_like(emitNorm)
    betaC,gammaC=NP_Energy2BetaC_GammaC(energyMeV)
    betaCgammaC=betaC*gammaC
    
    if len(emitNorm)==3:
        betaCgammaC3=betaC*gammaC**3
        emitGeo[0]=emitNorm[0]/betaCgammaC
        emitGeo[1]=emitNorm[1]/betaCgammaC
        emitGeo[2]=emitNorm[2]/betaCgammaC3
    elif len(emitNorm)==2:
        emitGeo[0]=emitNorm[0]/betaCgammaC
        emitGeo[1]=emitNorm[1]/betaCgammaC
    elif len(emitNorm)==1:
        emitGeo[0]=emitNorm[0]/betaCgammaC
    return emitGeo

def Emit_Geo2Norm(emitGeo,energyMeV):
    emitNorm=np.empty_like(emitGeo)
    betaC,gammaC=NP_Energy2BetaC_GammaC(energyMeV)
    betaCgammaC=betaC*gammaC
    
    if len(emitGeo)==3:
        betaCgammaC3=betaC*gammaC**3
        emitNorm[0]=emitGeo[0]*betaCgammaC
        emitNorm[1]=emitGeo[1]*betaCgammaC
        emitNorm[2]=emitGeo[2]*betaCgammaC3
    elif len(emitNorm)==2:
        emitNorm[0]=emitGeo[0]*betaCgammaC
        emitNorm[1]=emitGeo[1]*betaCgammaC
    elif len(emitNorm)==1:
        emitNorm[0]=emitGeo[0]*betaCgammaC
    return emitNorm

        
    









