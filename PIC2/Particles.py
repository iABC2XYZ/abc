#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:06:36 2017

@author: e
"""
import numpy as np

from Constants import e,c
from BetaGammaC import NP_Energy2BetaLambdaM

from PartGen import BunchedGen, CoastingGen

from Input import *

from Twiss import Emit_Norm2Geo

from Part2SI import Bunched2SI,Coasting2SI



def ZMinMax(energyMeV,freq):
    betaLambdaM=NP_Energy2BetaLambdaM(energyMeV,freq)
    zMin,zMax=-betaLambdaM/2,betaLambdaM/2
    return zMin,zMax



freq=freqMHz*1e6

def ParticleInitial():

    inforPart=np.zeros((beamNum,5))   # num,  charge, mass, energy, current
    for iBeam in range(beamNum):
        inforPart[iBeam,1]=eval('beamCharge_'+str(iBeam+1))
        inforPart[iBeam,2]=eval('beamMass_'+str(iBeam+1))
        inforPart[iBeam,3]=eval('beamEnergy_'+str(iBeam+1))
        inforPart[iBeam,4]=eval('beamCurrent_'+str(iBeam+1))*1e-3
    
    
    numCharge=inforPart[:,4]/e/freq
    numChargeQ=numCharge/np.abs(inforPart[:,1])
    ratioPart=np.sum(numChargeQ)/numPart               # ratioPart 很重要
    inforPart[:,0]=numChargeQ/ratioPart
    
    inforPart[0:-1,0]=np.int64(inforPart[0:-1,0])
    inforPart[-1,0]=np.int64(numPart-np.sum(inforPart[0:-1,0]))
    
    numPart=np.int64(numPart)
    X=np.zeros((numPart,1))
    PX=np.zeros((numPart,1))
    Y=np.zeros((numPart,1))
    PY=np.zeros((numPart,1))
    Z=np.zeros((numPart,1))
    PZ=np.zeros((numPart,1))
    Q=np.zeros((numPart,1))
    M=np.zeros((numPart,1))
    
    
    numPartRec=0
    for iBeam in range(1,beamNum+1):
        numPartBeam,qBeam,mBeam,energyBeam,cBeam=inforPart[iBeam-1,:]
        numPartBeam=np.int64(numPartBeam)
        
        if eval('beamState_'+str(iBeam)).lower()=='bunched':
            emitXnorm,emitYnorm,emitZnorm=eval('emitXnorm_B'+str(iBeam)),eval('emitYnorm_B'+str(iBeam)),eval('emitZnorm_B'+str(iBeam))
            
            alphaX,alphaY,alphaZ=eval('alphaX_B'+str(iBeam)),eval('alphaY_B'+str(iBeam)),eval('alphaZ_B'+str(iBeam))
            
            betaX,betaY,betaZ=eval('betaX_B'+str(iBeam)),eval('betaY_B'+str(iBeam)),eval('betaZ_B'+str(iBeam))
            
            muX,muXP,muY,muYP,muZ,muZP=eval('muX_B'+str(iBeam)),eval('muXP_B'+str(iBeam)),eval('muY_B'+str(iBeam)),eval('muYP_B'+str(iBeam)),eval('muZ_B'+str(iBeam)),eval('muZP_B'+str(iBeam))
            
            beamDistribition=eval('beamDistribition_'+str(iBeam))
            
            zMin,zMax=ZMinMax(energyBeam,freq)
            
            emitXgeo,emitYgeo,emitZgeo=Emit_Norm2Geo([emitXnorm,emitYnorm,emitZnorm],energyBeam)
            
            x,xp,y,yp,z,zp=BunchedGen(numPartBeam,emitXgeo,emitYgeo,emitZgeo,alphaX,alphaY,alphaZ,betaX,betaY,betaZ,muX,muXP,muY,muYP,muZ,muZP,beamDistribition)
            x,px,y,py,z,pz=Bunched2SI(energyBeam,x,xp,y,yp,z,zp)
            
        if eval('beamState_'+str(iBeam)).lower()=='coasting':
            emitXnorm,emitYnorm=eval('emitXnorm_C'+str(iBeam)),eval('emitYnorm_C'+str(iBeam))
            
            alphaX,alphaY=eval('alphaX_C'+str(iBeam)),eval('alphaY_C'+str(iBeam))
            
            betaX,betaY=eval('betaX_C'+str(iBeam)),eval('betaY_C'+str(iBeam))
            
            dp_p=eval('dp_p_C'+str(iBeam))
            
            muX,muXP,muY,muYP=eval('muX_C'+str(iBeam)),eval('muXP_C'+str(iBeam)),eval('muY_C'+str(iBeam)),eval('muYP_C'+str(iBeam))
            
            beamDistribition=eval('beamDistribition_'+str(iBeam))
            
            zMin,zMax=ZMinMax(energyBeam,freq)
            emitXgeo,emitYgeo,emitZgeo=Emit_Norm2Geo([emitXnorm,emitYnorm,emitZnorm],energyBeam)
            
            x,xp,y,yp,z,zp=CoastingGen(numPartBeam,emitXgeo,emitYgeo,alphaX,alphaY,betaX,betaY,zMin,zMax,dp_p,muX,muXP,muY,muYP,beamDistribition)
            x,px,y,py,z,pz=Bunched2SI(energyBeam,x,xp,y,yp,z,zp)
        
        X[numPartRec:numPartRec+numPartBeam,0]=x
        PX[numPartRec:numPartRec+numPartBeam,0]=xp
        Y[numPartRec:numPartRec+numPartBeam,0]=y
        PY[numPartRec:numPartRec+numPartBeam,0]=yp
        Z[numPartRec:numPartRec+numPartBeam,0]=z
        PZ[numPartRec:numPartRec+numPartBeam,0]=zp
        Q[numPartRec:numPartRec+numPartBeam,0]=qBeam
        M[numPartRec:numPartRec+numPartBeam,0]=mBeam
        
        numPartRec+=numPartBeam
    
    QReal=Q*ratioPart
    return X,PX,Y,PY,Z,PZ,Q,M,QReal,zMin,zMax



#--------------------------------------------------------------





