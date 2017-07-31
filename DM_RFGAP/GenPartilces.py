#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 12:23:48 2017

@author: A
"""
import tensorflow as tf
import numpy as np
from BetaGammaC import *
from RFCal import * 
from ConstPhysics import *

def GenGammaT5Twiss(alphaT2D,betaT2D):
    gammaT2D=tf.div(1.+tf.square(alphaT2D),betaT2D)
    return gammaT2D

def Gen2DPart5Twiss(emitG2D,alphaT2D,betaT2D,numPart):
    x=tf.random_normal([numPart])
    xp=tf.random_normal([numPart])
    
    gammaT2D=GenGammaT5Twiss(alphaT2D,betaT2D)
    X=tf.sqrt(emitG2D/gammaT2D)*(x-alphaT2D*xp)
    XP=tf.sqrt(emitG2D*gammaT2D)*xp
    return X,XP

def Gen2DPart5Twiss_1N(emitG2D,alphaT2D,betaT2D,numPart):
    x=tf.random_normal([1,numPart])
    xp=tf.random_normal([1,numPart])
    
    gammaT2D=GenGammaT5Twiss(alphaT2D,betaT2D)
    X=tf.sqrt(emitG2D/gammaT2D)*(x-alphaT2D*xp)
    XP=tf.sqrt(emitG2D*gammaT2D)*xp
    return X,XP

def Gen6DPart5Twiss(emitG6D,alphaT6D,betaT6D,numPart):
    X,XP=Gen2DPart5Twiss(emitG6D[0],alphaT6D[0],betaT6D[0],numPart)
    Y,YP=Gen2DPart5Twiss(emitG6D[1],alphaT6D[1],betaT6D[1],numPart)
    Z,ZP=Gen2DPart5Twiss(emitG6D[2],alphaT6D[2],betaT6D[2],numPart)
    return X,XP,Y,YP,Z,ZP

def Gen2DPart5TwissMat(emitG2D,alphaT2D,betaT2D,numPart):
    X,XP=Gen2DPart5Twiss_1N(emitG2D,alphaT2D,betaT2D,numPart)
    disPart=tf.concat([X,XP],0)
    return disPart


def Gen6DPart5TwissMat(emitG6D,alphaT6D,betaT6D,numPart):
    X,XP=Gen2DPart5Twiss_1N(emitG6D[0],alphaT6D[0],betaT6D[0],numPart)
    Y,YP=Gen2DPart5Twiss_1N(emitG6D[1],alphaT6D[1],betaT6D[1],numPart)
    Z,ZP=Gen2DPart5Twiss_1N(emitG6D[2],alphaT6D[2],betaT6D[2],numPart)
    disPart=tf.concat([X,XP,Y,YP,Z,ZP],0)
    return disPart


def Gen6DPart5Twiss4RFgap(emitG6D,alphaT6D,betaT6D,energySyn,freqMHz,numPart):
    X,XP=Gen2DPart5Twiss_1N(emitG6D[0],alphaT6D[0],betaT6D[0],numPart)  
    Y,YP=Gen2DPart5Twiss_1N(emitG6D[1],alphaT6D[1],betaT6D[1],numPart)
    Z,ZP=Gen2DPart5Twiss_1N(emitG6D[2],alphaT6D[2],betaT6D[2],numPart)    # Emit: z-dp_p    [mm - mrad]
    
    betaLAmbdaM=FreqMHz2BetaLambdaM(freqMHz,energySyn)
    disPhiPi=Z/1000./betaLAmbdaM*Pi*2.
    
    betaGammaCSyn=Energy2BetaGammaC(energySyn)
    betaGammaC=(1.+ZP/1000.)*betaGammaCSyn
    disEnergy=BetaGammaC2Energy(betaGammaC)
    
    disTrans=tf.concat([X,XP,Y,YP],0)
    
    return disTrans,disPhiPi,disEnergy
    


def Gen6D4RFgap(emitG6D,alphaT6D,betaT6D,energySyn,freqMHz,numPart):
    X,XP=Gen2DPart5Twiss_1N(emitG6D[0],alphaT6D[0],betaT6D[0],numPart)  
    Y,YP=Gen2DPart5Twiss_1N(emitG6D[1],alphaT6D[1],betaT6D[1],numPart)
    Z,ZP=Gen2DPart5Twiss_1N(emitG6D[2],alphaT6D[2],betaT6D[2],numPart)    # Emit: z-dp_p    [mm - mrad]
    
    betaLAmbdaM=FreqMHz2BetaLambdaM(freqMHz,energySyn)
    disPhiPi=Z/1000./betaLAmbdaM*Pi*2.
    
    betaGammaCSyn=Energy2BetaGammaC(energySyn)
    betaGammaC=(1.+ZP/1000.)*betaGammaCSyn
    disEnergy=BetaGammaC2Energy(betaGammaC)
    
    disX=X
    disXP=XP
    disY=Y
    disYP=YP
    
    return disX,disXP,disY,disYP,disPhiPi,disEnergy















