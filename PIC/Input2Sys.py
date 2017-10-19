#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 09:57:02 2017

@author: e
"""

import numpy as np

from Input import *
from BetaGammaC import *
from Constants import *
from Twiss import SigmaE4D,SigmaE6D,Mu4D,Mu6D,Emit_Norm2Geo,Emit_Geo2Norm
from RegFn import MM2M_6,MM2M_4
from BetaGammaC import NP_Energy2BetaGammaC,NP_Energy2BetaC

numPart=np.int64(numPart)

if bunchFlag==True:
    xMin,xMax,yMin,yMax=MM2M_4(xMin,xMax,yMin,yMax)
    
    betaC0=NP_Energy2BetaC(energyMeV)
    lambdaM=c/(freqMHz_C*1e6)
    betaLambdaM=betaC0*lambdaM
    zMin,zMax=-betaLambdaM/2,betaLambdaM/2
    
    
    emitNorm=np.array([emitXnorm_B,emitYnorm_B,emitZnorm_B])
    emitGeo=Emit_Norm2Geo(emitNorm,energyMeV)
    emitXGeo,emitYGeo,emitZGeo=emitGeo


    muT6D=Mu6D(muX_B,muXP_B,muY_B,muYP_B,muZ_B,muZP_B)
    sigmaT6D=SigmaE6D(alphaX_B,alphaY_B,alphaZ_B,betaX_B,betaY_B,betaZ_B,emitXGeo,emitYGeo,emitZGeo)
    
    x,xp,y,yp,z,zp=np.random.multivariate_normal(muT6D,sigmaT6D,numPart).T
    x,xp,y,yp,z,zp=MM2M_6(x,xp,y,yp,z,zp)      # m m m rad rad rad
    
    p0=NP_Energy2BetaGammaC(energyMeV)
    pz=p0*(1.+zp)               # bg
    px=xp/pz                    # bg
    py=yp/pz                    # bg
    

if bunchFlag==False:
    xMin,xMax,yMin,yMax=MM2M_4(xMin,xMax,yMin,yMax)
    
    betaC0=NP_Energy2BetaC(energyMeV)
    lambdaM=c/(freqMHz_C*1e6)
    betaLambdaM=betaC0*lambdaM
    zMin,zMax=-betaLambdaM/2.,betaLambdaM/2.
    
    emitNorm=np.array([emitXnorm_C,emitYnorm_C])
    emitGeo=Emit_Norm2Geo(emitNorm,energyMeV)
    emitXGeo,emitYGeo=emitGeo

    muT4D=Mu4D(muX_C,muXP_C,muY_B,muYP_C)
    sigmaT4D=SigmaE4D(alphaX_C,alphaY_C,betaX_C,betaY_C,emitXGeo,emitYGeo)
    x,xp,y,yp=np.random.multivariate_normal(muT4D,sigmaT4D,numPart).T
    x,xp,y,yp=MM2M_4(x,xp,y,yp)      # m m rad rad
    z=(np.random.random(numPart)-0.5)*betaLambdaM
    zp=dp_p_C*(np.random.random(numPart)*2-1)
    
    p0=NP_Energy2BetaGammaC(energyMeV)
    pz=p0*(1.+zp)
    px=xp/pz                    # bg
    py=yp/pz
    
    
    
    
    
    
    
    
    







