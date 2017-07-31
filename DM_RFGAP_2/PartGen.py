#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:18:39 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:


"""




import tensorflow as tf
from Lambda import BetaLambdaM
from Constants import pi
from BetaGammaC import Energy2BetaGammaC,BetaGammaC2Energy

def GammaT2D(alphaT2D,betaT2D):
    gammaT2D=tf.div(1.+tf.square(alphaT2D),betaT2D)
    return gammaT2D

def PartGen2D(emitG2D,alphaT2D,betaT2D,numPart):
    x=tf.random_normal([1,numPart])
    xp=tf.random_normal([1,numPart])
    
    gammaT2D=GammaT2D(alphaT2D,betaT2D)
    X=tf.sqrt(emitG2D/gammaT2D)*(x-alphaT2D*xp)
    XP=tf.sqrt(emitG2D*gammaT2D)*xp
    return X,XP

def PartGen6D(emitG6D,alphaT6D,betaT6D,numPart,energySyn,freqMHz):
    X,XP=PartGen2D(emitG6D[0],alphaT6D[0],betaT6D[0],numPart)  
    Y,YP=PartGen2D(emitG6D[1],alphaT6D[1],betaT6D[1],numPart)
    Z,ZP=PartGen2D(emitG6D[2],alphaT6D[2],betaT6D[2],numPart)    # Emit: z-dp_p    [mm - mrad]
    
    disX=X
    disXP=XP
    disY=Y
    disYP=YP
    
    
    betaLambdaM=BetaLambdaM(energySyn,freqMHz)
    disPhiPi=Z/1000./betaLambdaM*pi*2.
    
    betaGammaCSyn=Energy2BetaGammaC(energySyn)
    betaGammaC=(1.+ZP/1000.)*betaGammaCSyn
    disEnergy=BetaGammaC2Energy(betaGammaC)
    

    return disX,disXP,disY,disYP,disPhiPi,disEnergy




















