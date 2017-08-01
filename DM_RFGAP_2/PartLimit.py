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









