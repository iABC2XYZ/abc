#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:12:38 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    Map
______________________________________________________

    DriftTrans()=[1,L;0,1]
    RFGapTrans()=[1,0;-K,1]
    
    

"""
import tensorflow as tf
from Lambda import BetaLambdaM
from InputLattice import freqMHz
from Constants import pi

def DriftTrans(L,x,xp):
    x=tf.add(x,xp*L)
    return x,xp

def RFGapTrans(K,x,xp):
    xp=tf.add(xp,-K*x)
    return x,xp

def DriftLongi(L,phiPi,energyMeV):
    betaLambdaM=BetaLambdaM(energyMeV,freqMHz)
    phiPi=phiPi+tf.div(2.*pi*L,betaLambdaM)-pi
    return phiPi,energyMeV

def RFGapLongi(dE,phiPi,energyMeV):
    energyMeV=tf.add(dE,energyMeV)
    return phiPi,energyMeV

def Drift3D(L,x,xp,y,yp,phiPi,energyMeV):
    x,xp=DriftTrans(L,x,xp)
    y,yp=DriftTrans(L,y,yp)
    phiPi,energyMeV=DriftLongi(L,phiPi,energyMeV)
    return x,xp,y,yp,phiPi,energyMeV
    
def RFGap3D(K,dE,x,xp,y,yp,phiPi,energyMeV):
    x,xp=RFGapTrans(K,x,xp)
    y,yp=RFGapTrans(K,y,yp)
    phiPi,energyMeV= RFGapLongi(dE,phiPi,energyMeV)
    return x,xp,y,yp,phiPi,energyMeV
    
    









