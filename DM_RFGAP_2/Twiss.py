#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:58:50 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:


"""

import tensorflow as tf
from Lambda import BetaLambdaM
from Constants import pi
from EP import dE2dP_energy
from PartLimit import PartNonNan6D,PartLimitXY4D
from InputBeam import numPart

def Twiss2D(x,xp):
    xMean=tf.reduce_mean(x)
    xxVar=tf.reduce_mean(tf.square(x-xMean))
    xpMean=tf.reduce_mean(xp)
    xpxpVar=tf.reduce_mean(tf.square(xp-xpMean))
    xxpVar=tf.reduce_mean((x-xMean)*(xp-xpMean))
    
    emitT=tf.sqrt(xxVar*xpxpVar-xxpVar*xxpVar)
    betaT=xxVar/emitT
    alphaT=-xxpVar/emitT
    gammaT=xpxpVar/emitT
    
    return emitT,alphaT,betaT,gammaT

def TwissPhiP(disPhiPi,disEnergy,energySyn,freqMHz):
    betaLambdaM=BetaLambdaM(energySyn,freqMHz)
    Z=disPhiPi/(2.*pi)*betaLambdaM*1000.
    
    dE_E=(disEnergy-energySyn)/energySyn
    dP_P=dE2dP_energy(dE_E,energySyn)*1000.
    
    emitT,alphaT,betaT,gammaT=Twiss2D(Z,dP_P)
    
    return emitT,alphaT,betaT,gammaT



def Twiss6D(disX,disXP,disY,disYP,disPhiPi,disEnergy,energySyn,freqMHz):
    xEmitT,xAlphaT,xBetaT,xGammaT=Twiss2D(disX,disXP)
    yEmitT,yAlphaT,yBetaT,yGammaT=Twiss2D(disY,disYP)
    zEmitT,zAlphaT,zBetaT,zGammaT=TwissPhiP(disPhiPi,disEnergy,energySyn,freqMHz)
     

    emitT=[xEmitT,yEmitT,zEmitT]
    alphaT=[xAlphaT,yAlphaT,zAlphaT]
    betaT=[xBetaT,yBetaT,zBetaT]
    gammaT=[xGammaT,yGammaT,zGammaT]
    
    return emitT,alphaT,betaT,gammaT


def Emit3D_Nan_xyLimit(disX,disXP,disY,disYP,disPhiPi,disEnergy,energySyn,freqMHz):
    x,xp,y,yp,phi,Ek,numParNan=PartNonNan6D(disX,disXP,disY,disYP,disPhiPi,disEnergy)
    x,xp,y,yp,numPartXYLoss=PartLimitXY4D(x,xp,y,yp)
    
    emitT,alphaT,betaT,gammaT= Twiss6D(x,xp,y,yp,phi,Ek,energySyn,freqMHz)
    
    coeEmit=1.+tf.to_float(numParNan+numPartXYLoss)
    emitT=emitT*coeEmit
    
    return emitT






def Emit3DLimit(disX,disXP,disY,disYP,disPhiPi,disEnergy,energySyn,freqMHz):
    numPartDisXTmp=tf.shape(disX)
    numPartDisX=numPartDisXTmp[0]
    
    coeEmit=1.+tf.to_float(numPart-numPartDisX)
    
    
    #emitTOri=tf.cond(tf.less(numPartDisX,tf.constant([3])),SetEmitT(),GetEmitT(disX,disXP,disY,disYP,disPhiPi,disEnergy,energySyn,freqMHz))

    numPartCut=tf.constant(3)
    
    emitTConstMax=tf.constant([1.e6,1.e6,6.e10])
    emitTOri,alphaT,betaT,gammaT= Twiss6D(disX,disXP,disY,disYP,disPhiPi,disEnergy,energySyn,freqMHz)

    emitT = tf.cond(tf.less(numPartDisX, numPartCut), lambda: tf.multiply(emitTConstMax,coeEmit), lambda: tf.multiply(emitTOri, coeEmit))


    return emitT










