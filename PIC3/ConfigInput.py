#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""

from Input import *
import numpy as np
from Constants import e,c

from Twiss import Emit_Norm2Geo

from Part2SI import Bunched2SI,Coasting2SI

from BetaGammaC import NP_Energy2BetaLambdaM

from PartGen import BunchedGen, CoastingGen

from RegFn import ZMinMax

freq=freqMHz*1e6

beamNum=beamSecNum+1

inforPart=np.zeros((beamNum,5))   # num,  charge, mass, energy, current
for iBeam in range(beamNum):
    if iBeam==0:
        inforPart[iBeam,1]=eval('beamCharge')
        inforPart[iBeam,2]=eval('beamMass')
        inforPart[iBeam,3]=eval('beamEnergy')
        inforPart[iBeam,4]=eval('beamCurrent')*1e-3
    else:
        inforPart[iBeam,1]=eval('beamSecCharge_'+str(iBeam))
        inforPart[iBeam,2]=eval('beamSecMass_'+str(iBeam))
        inforPart[iBeam,3]=eval('beamSecEnergy_'+str(iBeam))
        inforPart[iBeam,4]=eval('beamSecCurrent_'+str(iBeam))*1e-3
    


numCharge=inforPart[:,4]/e/freq
numChargeQ=numCharge/np.abs(inforPart[:,1])
ratioPart=np.sum(numChargeQ)/numPart               # ratioPart 很重要
inforPart[:,0]=numChargeQ/ratioPart

inforPart[0:-1,0]=np.round(inforPart[0:-1,0])
inforPart[-1,0]=numPart-np.sum(inforPart[0:-1,0])

#print inforPart[:,0]

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
for iBeam in range(beamNum):
    numPartBeam,qBeam,mBeam,energyBeam,cBeam=inforPart[iBeam,:]
    numPartBeam=np.int64(numPartBeam)
    
    if iBeam==0:
        if beamState.lower()=='bunched':
            emitXnorm,emitYnorm,emitZnorm=emitXnorm_B,emitYnorm_B,emitZnorm_B
            alphaX,alphaY,alphaZ=alphaX_B,alphaY_B,alphaZ_B
            betaX,betaY,betaZ=betaX_B,betaY_B,betaZ_B
            muX,muXP,muY,muYP,muZ,muZP=muX_B,muXP_B,muY_B,muYP_B,muZ_B,muZP_B
            beamDistrib=beamDistribition
            
            beamStruc='bunched'
            
        if beamState.lower()=='coasting':
            emitXnorm,emitYnorm=emitXnorm_C,emitYnorm_C
            alphaX,alphaY=alphaX_C,alphaY_C
            betaX,betaY=betaX_C,betaY_C
            dp_p=dp_p_C
            muX,muXP,muY,muYP=muX_C,muXP_C,muY_C,muYP_C
            beamDistrib=beamDistribition
            
            beamStruc='coasting'
            
    else:
        if eval('beamSecState_'+str(iBeam)).lower()=='bunched':
            emitXnorm,emitYnorm,emitZnorm=eval('emitXnorm_SecB'+str(iBeam)),eval('emitYnorm_SecB'+str(iBeam)),eval('emitZnorm_SecB'+str(iBeam))
        
            alphaX,alphaY,alphaZ=eval('alphaX_SecB'+str(iBeam)),eval('alphaY_SecB'+str(iBeam)),eval('alphaZ_SecB'+str(iBeam))
            
            betaX,betaY,betaZ=eval('betaX_SecB'+str(iBeam)),eval('betaY_SecB'+str(iBeam)),eval('betaZ_SecB'+str(iBeam))
            
            muX,muXP,muY,muYP,muZ,muZP=eval('muX_SecB'+str(iBeam)),eval('muXP_SecB'+str(iBeam)),eval('muY_SecB'+str(iBeam)),eval('muYP_SecB'+str(iBeam)),eval('muZ_SecB'+str(iBeam)),eval('muZP_SecB'+str(iBeam))
            
            beamDistribition=eval('beamSecDistribition_'+str(iBeam))
            
            beamStruc='bunched'
            
        if eval('beamSecState_'+str(iBeam)).lower()=='coasting':
            emitXnorm,emitYnorm=eval('emitXnorm_SecC'+str(iBeam)),eval('emitYnorm_SecC'+str(iBeam))
        
            alphaX,alphaY=eval('alphaX_SecC'+str(iBeam)),eval('alphaY_SecC'+str(iBeam))
            
            betaX,betaY=eval('betaX_SecC'+str(iBeam)),eval('betaY_SecC'+str(iBeam))
            
            dp_p=eval('dp_p_SecC'+str(iBeam))
            
            muX,muXP,muY,muYP=eval('muX_SecC'+str(iBeam)),eval('muXP_SecC'+str(iBeam)),eval('muY_SecC'+str(iBeam)),eval('muYP_SecC'+str(iBeam))
            
            beamDistribition=eval('beamSecDistribition_'+str(iBeam))
            
            beamStruc='coasting'
            
    if beamStruc=='bunched':
        emitXgeo,emitYgeo,emitZgeo=Emit_Norm2Geo([emitXnorm,emitYnorm,emitZnorm],energyBeam)
        x,xp,y,yp,z,zp=BunchedGen(numPartBeam,emitXgeo,emitYgeo,emitZgeo,alphaX,alphaY,alphaZ,betaX,betaY,betaZ,muX,muXP,muY,muYP,muZ,muZP,beamDistribition)
        x,px,y,py,z,pz=Bunched2SI(energyBeam,x,xp,y,yp,z,zp)
    
    if beamStruc=='coasting':
        zMin,zMax=ZMinMax(energyBeam,freq)
        emitXgeo,emitYgeo=Emit_Norm2Geo([emitXnorm,emitYnorm],energyBeam)
        
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


#
#import matplotlib.pyplot as plt
#plt.close('all')
#plt.figure(1)
#plt.subplot(221)
#plt.plot(X,PX,'.')
#plt.subplot(222)
#plt.plot(Y,PY,'.')
#plt.subplot(223)
#plt.plot(Z,PZ,'.')





