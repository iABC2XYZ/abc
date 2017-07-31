#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 16:35:43 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    lambda
    betaLambda

"""

from Constants import c
from BetaGammaC import Energy2BetaC
import numpy as np

    
def LambdaM(freqMHz):
    lambdaM=np.float32(c)/(freqMHz*1.e6)
    return lambdaM

def LambdaMM(freqMHz):
    lambdaM=LambdaM(freqMHz)
    lambdaMM=lambdaM*1000.
    return lambdaMM

def BetaLambdaM(energyMeV,freqMHz):
    betaC=Energy2BetaC(energyMeV)
    lambdaM=LambdaM(freqMHz)
    betaLambdaM=betaC*lambdaM
    return betaLambdaM

def BetaLambdaMM(energyMeV,freqMHz):
    betaLambdaM=BetaLambdaM(freqMHz,energyMeV)
    betaLambdaMM=betaLambdaM*1000.
    return betaLambdaMM


