#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:58:50 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:


"""

import tensorflow as tf
from InputBeam import energyOutMeV

def EmitXY(x,xp):
    xMean=0.
    xxVar=tf.reduce_mean(tf.square(x-xMean))
    xpMean=0.
    xpxpVar=tf.reduce_mean(tf.square(xp-xpMean))
    xxpVar=tf.reduce_mean((x-xMean)*(xp-xpMean))
    
    emitT=tf.sqrt(xxVar*xpxpVar-xxpVar*xxpVar)

    return emitT

def EmitPhiEk(phi,Ek):
    phiMean=0.
    EkMean=energyOutMeV
    phi_phi_Var=tf.reduce_mean(tf.square(phi-phiMean))
    Ek_Ek_Var=tf.reduce_mean(tf.square(Ek-EkMean))
    phi_Ek_Var=tf.reduce_mean((phi-phiMean)*(Ek-EkMean))

    emitT=tf.sqrt(phi_phi_Var*Ek_Ek_Var-phi_Ek_Var*phi_Ek_Var)
    
    return emitT

def Emit3D(x,xp,y,yp,phi,Ek):
    emitX=EmitXY(x,xp)
    emitY=EmitXY(y,yp)
    emitZ=EmitPhiEk(phi,Ek)
    return emitX,emitY,emitZ






