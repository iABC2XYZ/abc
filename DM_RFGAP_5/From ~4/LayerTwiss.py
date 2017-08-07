#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 20:37:20 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
______________________________________________________


"""

import tensorflow as tf
from ActionFunction import MyAct,MyZoomIn,MyZoomOut
from InputBeam import energyInMeV
from InputLattice import freqMHz 
from Lambda import BetaLambdaM
from Constants import pi
from BetaGammaC import BetaGammaC2Energy,Energy2BetaGammaC

def TwissTrans(x,xp,emitT,alphaT,gammaT):
    X=tf.sqrt(emitT/gammaT)*(x-alphaT*xp)
    XP=tf.sqrt(emitT*gammaT)*xp
    return X,XP

def LayerTwiss(x,xp,y,yp,z,zp,emitT,alphaT,gammaT):
    X,XP=TwissTrans(x,xp,emitT[0],alphaT[0],gammaT[0])
    Y,YP=TwissTrans(y,yp,emitT[1],alphaT[1],gammaT[1])
    Z,ZP=TwissTrans(z,zp,emitT[2],alphaT[2],gammaT[2])
    
    betaLambdaM=BetaLambdaM(energyInMeV,freqMHz)
    PHI=Z/1000./betaLambdaM*pi*2.
    
    betaGammaCSyn=Energy2BetaGammaC(energyInMeV)
    betaGammaC=(1.+ZP/1000.)*betaGammaCSyn
    ENERGY=BetaGammaC2Energy(betaGammaC)

    X,XP,Y,YP,PHI,ENERGY=MyAct(X,XP,Y,YP,PHI,ENERGY)
    
    x,xp,y,yp,phi,energy=MyZoomIn(X,XP,Y,YP,PHI,ENERGY)
    
    return x,xp,y,yp,phi,energy
    
    

    
    











