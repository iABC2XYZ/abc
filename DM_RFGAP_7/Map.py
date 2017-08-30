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
from Lambda import LambdaM
from InputLattice import freqMHz
from Constants import pi

def DriftTrans(L,x,xp):
    x+=xp*L
    return x,xp

def RFGapTrans(K,x,xp):
    xp+=-K*x
    return x,xp

def DriftLongi(L,z,betaC):
    lambdaM=LambdaM(freqMHz)
    z+=betaC*lambdaM/2.-L
    return z,betaC

def RFGapLongi(dBeta,z,betaC):
    betaC+=dBeta
    return z,betaC

def Drift3D(x,xp,y,yp,z,betaC,L):
    x,xp=DriftTrans(L,x,xp)
    y,yp=DriftTrans(L,y,yp)
    z,betaC=DriftLongi(L,z,betaC)
    return x,xp,y,yp,z,betaC
    
def RFGap3D(x,xp,y,yp,z,betaC,K,dBeta):
    x,xp=RFGapTrans(K,x,xp)
    y,yp=RFGapTrans(K,y,yp)
    z,betaC= RFGapLongi(dBeta,z,betaC)
    return x,xp,y,yp,z,betaC
    
    









