#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:39:56 2017

@author: A
"""

import tensorflow as tf

def Energy2GammaC(energyMeV,massMeV=938.274):
    return 1.+tf.div(energyMeV,massMeV)
    
def GammaC2BetaC(gammaC):
    return tf.sqrt(1.-tf.div(1.,tf.square(gammaC)))

def BetaC2GammaC(betaC):
    return tf.div(1.,tf.sqrt(1.-tf.square(betaC)))

def GammaC2Energy(gammaC,massMeV=938.274):
    return (gammaC-1.)*massMeV

def Enerty2BetaC(energyMeV,massMeV=938.274):
    return GammaC2BetaC(Energy2GammaC(energyMeV,massMeV))

def BetaC2Energy(betaC,massMeV=938.274):
    return GammaC2Energy(BetaC2GammaC(betaC),massMeV)



