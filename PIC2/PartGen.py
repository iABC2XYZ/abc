#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:29:44 2017

@author: e
"""
import numpy as np
from Twiss import Mu6D,SigmaE6D,Mu4D,SigmaE4D


def BunchedGen(numPartBeam,emitXgeo,emitYgeo,emitZgeo,alphaX,alphaY,alphaZ,betaX,betaY,betaZ,muX,muXP,muY,muYP,muZ,muZP,beamDistribition):
    if beamDistribition.lower()=='gs6d':
        
        muT6D=Mu6D(muX,muXP,muY,muYP,muZ,muZP)
        sigmaT6D=SigmaE6D(alphaX,alphaY,alphaZ,betaX,betaY,betaZ,emitXgeo,emitYgeo,emitZgeo)
    
        x,xp,y,yp,z,zp=np.random.multivariate_normal(muT6D,sigmaT6D,numPartBeam).T
        
    if beamDistribition.lower()=='wb6d':
        pass
    
    
    return x,xp,y,yp,z,zp


def CoastingGen(numPartBeam,emitXgeo,emitYgeo,alphaX,alphaY,betaX,betaY,zMin,zMax,dp_p,muX,muXP,muY,muYP,beamDistribition):
    if beamDistribition.lower()=='gs4d':
        muT4D=Mu4D(muX,muXP,muY,muYP)
        sigmaT4D=SigmaE4D(alphaX,alphaY,betaX,betaY,emitXgeo,emitYgeo)
        
        x,xp,y,yp=np.random.multivariate_normal(muT4D,sigmaT4D,numPartBeam).T
        
    if beamDistribition.lower()=='kv4d':
        pass
    if beamDistribition.lower()=='wb4d':
        pass

    
    z=np.random.random(numPartBeam)*(zMax-zMin)+zMin
    zp=dp_p*(np.random.random(numPartBeam)*2-1)
    
    return x,xp,y,yp,z,zp


