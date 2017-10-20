#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:14:29 2017

@author: e
"""

# Beam -------------------------------------------
beamNum=2
freqMHz=162.5

#######  Beam1  #######################
beamName_1='proton'
beamState_1='Bunched'
beamDistribition_1='GS6d'
beamCurrent_1=10     # mA

beamCharge_1=1
beamMass_1=1
beamEnergy_1=1

#Bunched beam:
emitXnorm_B1,emitYnorm_B1,emitZnorm_B1=1.,1.,1.     # mm mrad
alphaX_B1,alphaY_B1,alphaZ_B1=1,1,1
betaX_B1,betaY_B1,betaZ_B1=2,2,2
muX_B1,muXP_B1,muY_B1,muYP_B1,muZ_B1,muZP_B1=0.,0.,0.,0.,0.,0.

#Coasting beam:
emitXnorm_C1,emitYnorm_C1=1.,1.     # mm mrad
alphaX_C1,alphaY_C1=-1,-1
betaX_C1,betaY_C1=2,2
dp_p_C1=0.01
muX_C1,muXP_C1,muY_C1,muYP_C1=0.,0.,0.,0.


#######  Beam2  #######################
beamName_2='C4+'
beamState_2='Coasting'
beamDistribition_2='GS4d'
beamCurrent_2=10     # mA

beamCharge_2=4
beamMass_2=12
beamEnergy_2=1

#Bunched beam:
emitXnorm_B2,emitYnorm_B2,emitZnorm_B2=1.,1.,1.     # mm mrad
alphaX_B2,alphaY_B2,alphaZ_B2=1,1,1
betaX_B2,betaY_B2,betaZ_B2=2,2,2
muX_B2,muXP_B2,muY_B2,muYP_B2,muZ_B2,muZP_B2=0.,0.,0.,0.,0.,0.

#Coasting beam:
emitXnorm_C2,emitYnorm_C2=1.,1.     # mm mrad
alphaX_C2,alphaY_C2=-1,-1
betaX_C2,betaY_C2=2,2
dp_p_C2=0.01
muX_C2,muXP_C2,muY_C2,muYP_C2=0.,0.,0.,0.

#######  Beam3  #######################
beamName_3='H-'
beamState_3='Coasting'
beamDistribition_3='GS'
beamCurrent_3=10     # mA

beamCharge_3=-1
beamMass_3=1
beamEnergy_3=1

#Bunched beam:
emitXnorm_B3,emitYnorm_B3,emitZnorm_B3=1.,1.,1.     # mm mrad
alphaX_B3,alphaY_B3,alphaZ_B3=1,1,1
betaX_B3,betaY_B3,betaZ_B3=2,2,2
muX_B3,muXP_B3,muY_B3,muYP_B3,muZ_B3,muZP_B3=0.,0.,0.,0.,0.,0.

#Coasting beam:
emitXnorm_C3,emitYnorm_C3=1.,1.     # mm mrad
alphaX_C3,alphaY_C3=-1,-1
betaX_C3,betaY_C3=2,2
dp_p_C3=0.01
muX_C3,muXP_C3,muY_C3,muYP_C3=0.,0.,0.,0.


#######  Beam4  #######################
beamName_4='U20+'
beamState_4='Coasting'
beamDistribition_4='GS'
beamCurrent_4=10     # mA

beamCharge_4=20
beamMass_4=87
beamEnergy_4=1

#Bunched beam:
emitXnorm_B4,emitYnorm_B4,emitZnorm_B4=1.,1.,1.     # mm mrad
alphaX_B4,alphaY_B4,alphaZ_B4=1,1,1
betaX_B4,betaY_B4,betaZ_B4=2,2,2
muX_B4,muXP_B4,muY_B4,muYP_B4,muZ_B4,muZP_B4=0.,0.,0.,0.,0.,0.

#Coasting beam:
emitXnorm_C4,emitYnorm_C4=1.,1.     # mm mrad
alphaX_C4,alphaY_C4=-1,-1
betaX_C4,betaY_C4=2,2
dp_p_C4=0.01
muX_C4,muXP_C4,muY_C4,muYP_C4=0.,0.,0.,0.


#######  Beam5  #######################
beamName_5='Ca2+'
beamState_5='Bunched'
beamDistribition_5='GS'
beamCurrent_5=10     # mA

beamCharge_5=2
beamMass_5=40
beamEnergy_5=1

#Bunched beam:
emitXnorm_B5,emitYnorm_B5,emitZnorm_B5=1.,1.,1.     # mm mrad
alphaX_B5,alphaY_B5,alphaZ_B5=1,1,1
betaX_B5,betaY_B5,betaZ_B5=2,2,2
muX_B5,muXP_B5,muY_B5,muYP_B5,muZ_B5,muZP_B5=0.,0.,0.,0.,0.,0.

#Coasting beam:
emitXnorm_C5,emitYnorm_C5=1.,1.     # mm mrad
alphaX_C5,alphaY_C5=-1,-1
betaX_C5,betaY_C5=2,2
dp_p_C5=0.01
muX_C5,muXP_C5,muY_C5,muYP_C5=0.,0.,0.,0.

#######  Beam6  #######################
beamName_6='O4+'
beamState_6='Bunched'
beamDistribition_6='GS'
beamCurrent_6=10     # mA

beamCharge_6=4
beamMass_6=16
beamEnergy_6=1

#Bunched beam:
emitXnorm_B6,emitYnorm_B6,emitZnorm_B6=1.,1.,1.     # mm mrad
alphaX_B6,alphaY_B6,alphaZ_B6=1,1,1
betaX_B6,betaY_B6,betaZ_B6=2,2,2
muX_B6,muXP_B6,muY_B6,muYP_B6,muZ_B6,muZP_B6=0.,0.,0.,0.,0.,0.

#Coasting beam:
emitXnorm_C6,emitYnorm_C6=1.,1.     # mm mrad
alphaX_C6,alphaY_C6=-1,-1
betaX_C6,betaY_C6=2,2
dp_p_C6=0.01
muX_C6,muXP_C6,muY_C6,muYP_C6=0.,0.,0.,0.


# config -------------------------------------------
numPart=1e4


# Lattice  -------------------------------------------

# Section1:  Mapfield :

Section=1

spaceChage='3D'
xGridLog,yGridLog,zGridLog=4,4,6
xMinMM,xMaxMM=-14.,14    #mm
yMinMM,yMaxMM=-14.,14    #mm


Section=2
spaceChage='2D'
xGridLog,yGridLog,zGridLog=4,4,6
xMinMM,xMaxMM=-14.,14    #mm
yMinMM,yMaxMM=-14.,14    #mm









