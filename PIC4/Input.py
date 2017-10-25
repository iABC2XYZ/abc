#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""

# MainBeam:
beamName='proton'
beamState='Bunched'
beamDistribition='GS6d'
beamCurrent=10     # mA
freqMHz=162.5

beamCharge=1
beamMass=1
beamEnergy=1

#Bunched beam:
emitXnorm_B,emitYnorm_B,emitZnorm_B=1.,1.,1.     # mm mrad
alphaX_B,alphaY_B,alphaZ_B=1,1,1
betaX_B,betaY_B,betaZ_B=2,2,2
muX_B,muXP_B,muY_B,muYP_B,muZ_B,muZP_B=0.,0.,0.,0.,0.,0.

#Coasting beam:
emitXnorm_C,emitYnorm_C=1.,1.     # mm mrad
alphaX_C,alphaY_C=-1,-1
betaX_C,betaY_C=2,2
dp_p_C=0.01
muX_C,muXP_C,muY_C,muYP_C=0.,0.,0.,0.



# Secondarybeam -------------------------------------------
beamSecNum=2

#######  beamSec1  #######################
beamSecName_1='proton'
beamSecState_1='Bunched'
beamSecDistribition_1='GS6d'
beamSecCurrent_1=10     # mA

beamSecCharge_1=1
beamSecMass_1=1
beamSecEnergy_1=1

#Bunched beamSec:
emitXnorm_SecB1,emitYnorm_SecB1,emitZnorm_SecB1=1.,1.,1.     # mm mrad
alphaX_SecB1,alphaY_SecB1,alphaZ_SecB1=1,1,1
betaX_SecB1,betaY_SecB1,betaZ_SecB1=2,2,2
muX_SecB1,muXP_SecB1,muY_SecB1,muYP_SecB1,muZ_SecB1,muZP_SecB1=0.,0.,0.,0.,0.,0.

#Coasting beamSec:
emitXnorm_SecC1,emitYnorm_SecC1=1.,1.     # mm mrad
alphaX_SecC1,alphaY_SecC1=-1,-1
betaX_SecC1,betaY_SecC1=2,2
dp_p_SecC1=0.01
muX_SecC1,muXP_SecC1,muY_SecC1,muYP_SecC1=0.,0.,0.,0.


#######  beamSec2  #######################
beamSecName_2='C4+'
beamSecState_2='Coasting'
beamSecDistribition_2='GS4d'
beamSecCurrent_2=10     # mA

beamSecCharge_2=4
beamSecMass_2=12
beamSecEnergy_2=1

#Bunched beamSec:
emitXnorm_SecB2,emitYnorm_SecB2,emitZnorm_SecB2=1.,1.,1.     # mm mrad
alphaX_SecB2,alphaY_SecB2,alphaZ_SecB2=1,1,1
betaX_SecB2,betaY_SecB2,betaZ_SecB2=2,2,2
muX_SecB2,muXP_SecB2,muY_SecB2,muYP_SecB2,muZ_SecB2,muZP_SecB2=0.,0.,0.,0.,0.,0.

#Coasting beamSec:
emitXnorm_SecC2,emitYnorm_SecC2=1.,1.     # mm mrad
alphaX_SecC2,alphaY_SecC2=-1,-1
betaX_SecC2,betaY_SecC2=2,2
dp_p_SecC2=0.01
muX_SecC2,muXP_SecC2,muY_SecC2,muYP_SecC2=0.,0.,0.,0.

#######  beamSec3  #######################
beamSecName_3='H-'
beamSecState_3='Coasting'
beamSecDistribition_3='GS'
beamSecCurrent_3=10     # mA

beamSecCharge_3=-1
beamSecMass_3=1
beamSecEnergy_3=1

#Bunched beamSec:
emitXnorm_SecB3,emitYnorm_SecB3,emitZnorm_SecB3=1.,1.,1.     # mm mrad
alphaX_SecB3,alphaY_SecB3,alphaZ_SecB3=1,1,1
betaX_SecB3,betaY_SecB3,betaZ_SecB3=2,2,2
muX_SecB3,muXP_SecB3,muY_SecB3,muYP_SecB3,muZ_SecB3,muZP_SecB3=0.,0.,0.,0.,0.,0.

#Coasting beamSec:
emitXnorm_SecC3,emitYnorm_SecC3=1.,1.     # mm mrad
alphaX_SecC3,alphaY_SecC3=-1,-1
betaX_SecC3,betaY_SecC3=2,2
dp_p_SecC3=0.01
muX_SecC3,muXP_SecC3,muY_SecC3,muYP_SecC3=0.,0.,0.,0.


#######  beamSec4  #######################
beamSecName_4='U20+'
beamSecState_4='Coasting'
beamSecDistribition_4='GS'
beamSecCurrent_4=10     # mA

beamSecCharge_4=20
beamSecMass_4=87
beamSecEnergy_4=1

#Bunched beamSec:
emitXnorm_SecB4,emitYnorm_SecB4,emitZnorm_SecB4=1.,1.,1.     # mm mrad
alphaX_SecB4,alphaY_SecB4,alphaZ_SecB4=1,1,1
betaX_SecB4,betaY_SecB4,betaZ_SecB4=2,2,2
muX_SecB4,muXP_SecB4,muY_SecB4,muYP_SecB4,muZ_SecB4,muZP_SecB4=0.,0.,0.,0.,0.,0.

#Coasting beamSec:
emitXnorm_SecC4,emitYnorm_SecC4=1.,1.     # mm mrad
alphaX_SecC4,alphaY_SecC4=-1,-1
betaX_SecC4,betaY_SecC4=2,2
dp_p_SecC4=0.01
muX_SecC4,muXP_SecC4,muY_SecC4,muYP_SecC4=0.,0.,0.,0.


#######  beamSec5  #######################
beamSecName_5='Ca2+'
beamSecState_5='Bunched'
beamSecDistribition_5='GS'
beamSecCurrent_5=10     # mA

beamSecCharge_5=2
beamSecMass_5=40
beamSecEnergy_5=1

#Bunched beamSec:
emitXnorm_SecB5,emitYnorm_SecB5,emitZnorm_SecB5=1.,1.,1.     # mm mrad
alphaX_SecB5,alphaY_SecB5,alphaZ_SecB5=1,1,1
betaX_SecB5,betaY_SecB5,betaZ_SecB5=2,2,2
muX_SecB5,muXP_SecB5,muY_SecB5,muYP_SecB5,muZ_SecB5,muZP_SecB5=0.,0.,0.,0.,0.,0.

#Coasting beamSec:
emitXnorm_SecC5,emitYnorm_SecC5=1.,1.     # mm mrad
alphaX_SecC5,alphaY_SecC5=-1,-1
betaX_SecC5,betaY_SecC5=2,2
dp_p_SecC5=0.01
muX_SecC5,muXP_SecC5,muY_SecC5,muYP_SecC5=0.,0.,0.,0.

#######  beamSec6  #######################
beamSecName_6='O4+'
beamSecState_6='Bunched'
beamSecDistribition_6='GS'
beamSecCurrent_6=10     # mA

beamSecCharge_6=4
beamSecMass_6=16
beamSecEnergy_6=1

#Bunched beamSec:
emitXnorm_SecB6,emitYnorm_SecB6,emitZnorm_SecB6=1.,1.,1.     # mm mrad
alphaX_SecB6,alphaY_SecB6,alphaZ_SecB6=1,1,1
betaX_SecB6,betaY_SecB6,betaZ_SecB6=2,2,2
muX_SecB6,muXP_SecB6,muY_SecB6,muYP_SecB6,muZ_SecB6,muZP_SecB6=0.,0.,0.,0.,0.,0.

#Coasting beamSec:
emitXnorm_SecC6,emitYnorm_SecC6=1.,1.     # mm mrad
alphaX_SecC6,alphaY_SecC6=-1,-1
betaX_SecC6,betaY_SecC6=2,2
dp_p_SecC6=0.01
muX_SecC6,muXP_SecC6,muY_SecC6,muYP_SecC6=0.,0.,0.,0.


# Global Config -------------------------------------------
numPart=1e4

zBegin=100
zFinish=700.
spaceCharge,nStep,xGridLog,yGridLog,zGridLog='3D',5,4,4,4

dTG=0.1
freqMHzG=162.5
xMinG,xMaxG,yMinG,yMaxG=-12,12,-12,12


# Lattice  -------------------------------------------

ele_1='drift'
zStart_1,zEnd_1=0.,1000.
#dT_1=0.2
#freqMHz_1=162.5
#xMin_1,xMax_1,yMin_1,yMax_1=-10,10,-10,10

ele_2='rFQ'
zStart_2,zEnd_2=800.,2000.


ele_3='EMField'
zStart_3,zEnd_3=800.,2000.
EMMod_2='3D'
EMFieldLoc_2='EM.field'
#dT_2=0.1
#freqMHz_2=162.5
#xMin_2,xMax_2,yMin_2,yMax_2=-10,10,-10,10
























