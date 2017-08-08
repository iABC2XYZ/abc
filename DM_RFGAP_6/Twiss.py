#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:58:50 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:


"""

import tensorflow as tf
from InputBeam import energyOutMeV
from BetaGammaC import Energy2BetaC

def EmitXY(x,xp):
    xMean=0.
    xxVar=tf.reduce_mean(tf.square(x-xMean))
    xpMean=0.
    xpxpVar=tf.reduce_mean(tf.square(xp-xpMean))
    xxpVar=tf.reduce_mean((x-xMean)*(xp-xpMean))
    
    emitT=tf.sqrt(xxVar*xpxpVar-xxpVar*xxpVar)

    return emitT

def EmitPhiEk(z,betaC,energySyn):
    zMean=0.
    betaCMean=Energy2BetaC(energySyn)
    z_z_Var=tf.reduce_mean(tf.square(z-zMean))
    betaC_betaC_Var=tf.reduce_mean(tf.square(betaC-betaCMean))
    z_betaC_Var=tf.reduce_mean((z-zMean)*(betaC-betaCMean))

    emitT=tf.sqrt(z_z_Var*betaC_betaC_Var-z_betaC_Var*z_betaC_Var)
    
    return emitT

def Emit3D(x,xp,y,yp,z,betaC,energySyn=energyOutMeV):
    emitX=EmitXY(x,xp)
    emitY=EmitXY(y,yp)
    emitZ=EmitPhiEk(z,betaC,energySyn)
    return emitX,emitY,emitZ






