#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 09:23:42 2017

@author: e
"""

# Beam

beamParticle='proton'    # C
chargeParticle=1.
massParicle=1

energyMeV=1.


bunchFlag=False

#Bunch beam:
emitXnorm_B,emitYnorm_B,emitZnorm_B=1.,1.,1.     # mm mrad
alphaX_B,alphaY_B,alphaZ_B=1,1,1
betaX_B,betaY_B,betaZ_B=2,2,2
muX_B,muXP_B,muY_B,muYP_B,muZ_B,muZP_B=0.,0.,0.,0.,0.,0.

#Coasting beam:
emitXnorm_C,emitYnorm_C=1.,1.     # mm mrad
alphaX_C,alphaY_C=-1,-1
betaX_C,betaY_C=2,2
freqMHz_C=162.5
dp_p_C=0.01
muX_C,muXP_C,muY_C,muYP_C,muZ_C,muZP_C=0.,0.,0.,0.,0.,0.





#sysconfig
numPart=1e4

# mapfield

xGridLog,yGridLog,zGridLog=4,4,6
xMin,xMax=-14.,14    #mm
yMin,yMax=-14.,14    #mm




















