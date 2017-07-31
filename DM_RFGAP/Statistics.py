#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 12:42:13 2017

@author: A
"""

import tensorflow as tf
from BetaGammaC import *

def GetTwiss2D(x,xp):
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



def GetTwiss6D(x,xp,y,yp,z,zp):
    xEmitT,xAlphaT,xBetaT,xGammaT=GetTwiss2D(x,xp)
    yEmitT,yAlphaT,yBetaT,yGammaT=GetTwiss2D(y,yp)
    zEmitT,zAlphaT,zBetaT,zGammaT=GetTwiss2D(z,zp)
    
    emitT=[xEmitT,yEmitT,zEmitT]
    alphaT=[xAlphaT,yAlphaT,zAlphaT]
    betaT=[xBetaT,yBetaT,zBetaT]
    gammaT=[xGammaT,yGammaT,zGammaT]
    
    return emitT,alphaT,betaT,gammaT


def GetTwiss6DMat(X):
    x=X[0,:]
    xp=X[1,:]
    y=X[2,:]
    yp=X[3,:]
    z=X[4,:]
    zp=X[5,:]    
    emitT,alphaT,betaT,gammaT=GetTwiss6D(x,xp,y,yp,z,zp)
    return emitT,alphaT,betaT,gammaT


def GetTwiss4D(x,xp,y,yp):
    xEmitT,xAlphaT,xBetaT,xGammaT=GetTwiss2D(x,xp)
    yEmitT,yAlphaT,yBetaT,yGammaT=GetTwiss2D(y,yp)


    emitT=[xEmitT,yEmitT]
    alphaT=[xAlphaT,yAlphaT]
    betaT=[xBetaT,yBetaT]
    gammaT=[xGammaT,yGammaT]
    
    return emitT,alphaT,betaT,gammaT



def GetTwiss4DMat(X):
    x=X[0,:]
    xp=X[1,:]
    y=X[2,:]
    yp=X[3,:]
    emitT,alphaT,betaT,gammaT=GetTwiss4D(x,xp,y,yp)
    return emitT,alphaT,betaT,gammaT

def GetTwiss7PhiPi_dP_P(disPhiPi,disEnergy,energyMeV,freqMHz):
    betaLambdaM=FreqMHz2BetaLambdaM(freqMHz,energyMeV)
    Z=disPhiPi/(2.*Pi)*betaLambdaM*1000.
    
    dE_E=(disEnergy-energyMeV)/energyMeV
    dP_P=dE_E2dP_P7Energy(dE_E,energyMeV)*1000.
    
    emitT,alphaT,betaT,gammaT=GetTwiss2D(Z,dP_P)
    
    return emitT,alphaT,betaT,gammaT
    

def GetTwiss6D_ALL(disTrans,disPhiPi,disEnergy,energyMeV,freqMHz):
     transEmitT,transAlphaT,transBetaT,transGammaT=GetTwiss4DMat(disTrans)
     longiEmitT,longiAlphaT,longiBetaT,longiGammaT=GetTwiss7PhiPi_dP_P(disPhiPi,disEnergy,energyMeV,freqMHz)
     
     
     emitT=[transEmitT[0],transEmitT[1],longiEmitT]
     alphaT=[transAlphaT[0],transAlphaT[1],longiAlphaT]
     betaT=[transBetaT[0],transBetaT[1],longiBetaT]
     gammaT=[transGammaT[0],transGammaT[1],longiGammaT]
     return emitT,alphaT,betaT,gammaT


def CalTwiss6D(disX,disXP,disY,disYP,disPhiPi,disEnergy,energyMeV,freqMHz):
    xEmitT,xAlphaT,xBetaT,xGammaT=GetTwiss2D(disX,disXP)
    yEmitT,yAlphaT,yBetaT,yGammaT=GetTwiss2D(disY,disYP)
    zEmitT,zAlphaT,zBetaT,zGammaT=GetTwiss7PhiPi_dP_P(disPhiPi,disEnergy,energyMeV,freqMHz)
     

    emitT=[xEmitT,yEmitT,zEmitT]
    alphaT=[xAlphaT,yAlphaT,zAlphaT]
    betaT=[xBetaT,yBetaT,zBetaT]
    gammaT=[xGammaT,yGammaT,zGammaT]
    
    return emitT,alphaT,betaT,gammaT






