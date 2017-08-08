#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 20:37:20 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
______________________________________________________


"""

import tensorflow as tf
from InputBeam import energyInMeV
from BetaGammaC import Energy2BetaGammaC,BetaGammaC2BetaC
from ActionFunction import MyAct

def TwissTrans(x,xp,emitT,alphaT,gammaT):
    X=tf.sqrt(emitT/gammaT)*(x-alphaT*xp)
    XP=tf.sqrt(emitT*gammaT)*xp
    return X,XP

def LayerTwiss(x,xp,y,yp,z,zp,emitT,alphaT,gammaT):
    X,XP=TwissTrans(x,xp,emitT[0],alphaT[0],gammaT[0])
    Y,YP=TwissTrans(y,yp,emitT[1],alphaT[1],gammaT[1])
    Z,ZP=TwissTrans(z,zp,emitT[2],alphaT[2],gammaT[2])
    
    x=X/1000.    # m
    xp=XP/1000.  # rad
    y=Y/1000.  #m
    yp=YP/1000.  #rad
    
    z=Z/1000.    # m
    betaGammaCSyn=Energy2BetaGammaC(energyInMeV)
    betaGammaC=(1.+ZP/1000.)*betaGammaCSyn
    betaC=BetaGammaC2BetaC(betaGammaC)
    
    x,xp,y,yp,z,betaC,numPartLost=MyAct(x,xp,y,yp,z,betaC)
    
    return x,xp,y,yp,z,betaC,numPartLost
    
    

    
    











