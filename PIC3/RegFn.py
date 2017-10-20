#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:50:03 2017

@author: e
"""
from BetaGammaC import NP_Energy2BetaLambdaM

def MM2M(x):
    x/=1000.
    return x

def MM2M_2(x1,x2):
    x1/=1000.
    x2/=1000.
    return x1,x2
def MM2M_3(x1,x2,x3):
    x1/=1000.
    x2/=1000.
    x3/=1000.
    return x1,x2,x3
def MM2M_4(x1,x2,x3,x4):
    x1/=1000.
    x2/=1000.
    x3/=1000.
    x4/=1000.
    return x1,x2,x3,x4
def MM2M_5(x1,x2,x3,x4,x5):
    x1/=1000.
    x2/=1000.
    x3/=1000.
    x4/=1000.
    x5/=1000.
    return x1,x2,x3,x4,x5
def MM2M_6(x1,x2,x3,x4,x5,x6):
    x1/=1000.
    x2/=1000.
    x3/=1000.
    x4/=1000.
    x5/=1000.
    x6/=1000.
    return x1,x2,x3,x4,x5,x6


def ZMinMax(energyMeV,freq):
    betaLambdaM=NP_Energy2BetaLambdaM(energyMeV,freq)
    zMin,zMax=-betaLambdaM/2,betaLambdaM/2
    return zMin,zMax









