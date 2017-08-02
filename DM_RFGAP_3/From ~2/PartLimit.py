#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 00:09:19 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
        Deal with Particles: 
______________________________________________________
        Nan
        Loss

"""
import tensorflow as tf
from InputBeam import numPart

def PartNonNan6D(disX,disXP,disY,disYP,disPhiPi,disEnergy):
    xNonNan=~tf.is_nan(disX)
    xpNonNan=~tf.is_nan(disXP)
    yNonNan=~tf.is_nan(disY)
    ypNonNan=~tf.is_nan(disYP)
    phiNonNan=~tf.is_nan(disPhiPi)
    energyNonNan=~tf.is_nan(disEnergy)
    
    xBoolNonNan=tf.logical_and(xNonNan,xpNonNan)
    yBoolNonNan=tf.logical_and(yNonNan,ypNonNan)
    zBoolNonNan=tf.logical_and(phiNonNan,energyNonNan)
    xyBoolNonNan=tf.logical_and(xBoolNonNan,yBoolNonNan)
    boolNonNan=tf.logical_and(xyBoolNonNan,zBoolNonNan)
    
    x=tf.boolean_mask(disX,boolNonNan)
    xp=tf.boolean_mask(disXP,boolNonNan)
    y=tf.boolean_mask(disY,boolNonNan)
    yp=tf.boolean_mask(disYP,boolNonNan)
    phi=tf.boolean_mask(disPhiPi,boolNonNan)
    energy=tf.boolean_mask(disEnergy,boolNonNan)
    
    numParNon=tf.shape(energy)
    numParNan=numPart-numParNon[0]

    return x,xp,y,yp,phi,energy,numParNan
    

def PartLimitXY4D(disX,disXP,disY,disYP):
    xLimit=tf.abs(disX)<1.e3
    xpLimit=tf.abs(disXP)<1.e3
    yLimit=tf.abs(disY)<1.e3
    ypLimit=tf.abs(disYP)<1.e3
    
    xxpLimit=tf.logical_and(xLimit,xpLimit)
    yypLimit=tf.logical_and(yLimit,ypLimit)
    xyLimit=tf.logical_and(xxpLimit,yypLimit)
    
    x=tf.boolean_mask(disX,xyLimit)
    xp=tf.boolean_mask(disXP,xyLimit)
    y=tf.boolean_mask(disY,xyLimit)
    yp=tf.boolean_mask(disYP,xyLimit)
    
    numPartLimit=tf.shape(x)
    numPartDisX=tf.shape(disX)
    numPartXYLoss=numPartDisX[0]-numPartLimit[0]
    return x,xp,y,yp,numPartXYLoss

def PartLimit6D(disX,disXP,disY,disYP,disPhiPi,disEnergy):
    xLimit=tf.abs(disX)<1.e3
    xpLimit=tf.abs(disXP)<1.e3
    yLimit=tf.abs(disY)<1.e3
    ypLimit=tf.abs(disYP)<1.e3
    phiLimit=tf.abs(disPhiPi)<6.e6
    energyLimit=tf.abs(disEnergy)<1.e4
    
    
    xxpLimit=tf.logical_and(xLimit,xpLimit)
    yypLimit=tf.logical_and(yLimit,ypLimit)
    phienergyLimit=tf.logical_and(phiLimit,energyLimit)
    
    xyLimit=tf.logical_and(xxpLimit,yypLimit)
    allLimit=tf.logical_and(phienergyLimit,xyLimit)
    
    
    x=tf.boolean_mask(disX,allLimit)
    xp=tf.boolean_mask(disXP,allLimit)
    y=tf.boolean_mask(disY,allLimit)
    yp=tf.boolean_mask(disYP,allLimit)
    phi=tf.boolean_mask(disPhiPi,allLimit)
    energy=tf.boolean_mask(disEnergy,allLimit)
    
    return x,xp,y,yp,phi,energy


def PartMax1D(x):
    boolFinite=tf.is_finite(x)
    xFinite=tf.boolean_mask(x,boolFinite)
    maxXFinite=tf.reduce_max(tf.abs(xFinite))
    return maxXFinite

def PartMax6D(disX,disXP,disY,disYP,disPhiPi,disEnergy):
    maxX=PartMax1D(disX)
    maxXP=PartMax1D(disXP)
    maxY=PartMax1D(disY)
    maxYP=PartMax1D(disYP)
    maxPhi=PartMax1D(disPhiPi)
    maxEnergy=PartMax1D(disEnergy)
    return maxX,maxXP,maxY,maxYP,maxPhi,maxEnergy
    
def PartMaxPow6D(disX,disXP,disY,disYP,disPhiPi,disEnergy,coePow=0.15):
    maxX,maxXP,maxY,maxYP,maxPhi,maxEnergy=PartMax6D(disX,disXP,disY,disYP,disPhiPi,disEnergy)
    maxXPow=tf.pow(maxX,coePow)
    maxXpPow=tf.pow(maxXP,coePow)
    maxYPow=tf.pow(maxY,coePow)
    maxYpPow=tf.pow(maxYP,coePow)
    maxPhiPow=tf.pow(maxPhi,coePow)
    maxEnergyPow=tf.pow(maxEnergy,coePow)
    
    xMaxEmit=maxXPow*maxXpPow
    yMaxEmit=maxYPow*maxYpPow
    zMaxEmit=maxPhiPow*maxEnergyPow
    
    return xMaxEmit,yMaxEmit,zMaxEmit
    
    
    
    


