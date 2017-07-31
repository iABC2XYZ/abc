#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:39:56 2017

@author: A
"""

import tensorflow as tf
from RFCal import * 

def Energy2GammaC(energyMeV,massMeV=938.274):
    return 1.+tf.div(energyMeV,massMeV)
    
def GammaC2BetaC(gammaC):
    return tf.sqrt(1.-tf.div(1.,tf.square(gammaC)))

def BetaC2GammaC(betaC):
    return tf.div(1.,tf.sqrt(1.-tf.square(betaC)))

def GammaC2Energy(gammaC,massMeV=938.274):
    return (gammaC-1.)*massMeV

def Energy2BetaC(energyMeV,massMeV=938.274):
    return GammaC2BetaC(Energy2GammaC(energyMeV,massMeV))

def BetaC2Energy(betaC,massMeV=938.274):
    return GammaC2Energy(BetaC2GammaC(betaC),massMeV)


def GammaC2BetaGammaC(gammaC):
    return tf.sqrt(tf.square(gammaC)-1.)

def BetaGammaC2GammC(betaGammaC):
    return  tf.sqrt(tf.square(betaGammaC)+1.)


def dE_E2dP_P7GammaC(dE_E,gammaSyn):
    return tf.div(gammaSyn,1+gammaSyn)*dE_E

def dP_P2dE_E7GammaC(dP_P,gammaSyn):
    return tf.div(1+gammaSyn,gammaSyn)*dP_P
    
    
def dE_E2dP_P7Energy(dE_E,energySyn,massMeV=938.274):
    gammaSyn=Energy2GammaC(energySyn,massMeV)
    return dE_E2dP_P7GammaC(dE_E,gammaSyn)

def dP_P2dE_E7Energy(dP_P,energySyn,massMeV=938.274):
    gammaSyn=Energy2GammaC(energySyn,massMeV)
    return dP_P2dE_E7GammaC(dP_P,gammaSyn)
    
    
def Energy2BetaGammaC(energySyn,massMeV=938.274):
    gammaCSyn=Energy2GammaC(energySyn,massMeV)
    return GammaC2BetaGammaC(gammaCSyn)

def BetaGammaC2Energy(betaGammaC,massMeV=938.274):
    gammaC=BetaGammaC2GammC(betaGammaC)
    return GammaC2Energy(gammaC,massMeV)
    
    
def FreqMHz2BetaLambdaM(freqMHz,energyMeV,massMeV=938.274):
    lambdaM=CalWavelength(freqMHz)
    betaC=Energy2BetaC(energyMeV,massMeV)
    return betaC*lambdaM
    
def Energy2BetaLambdaM(freqMHz,energyMeV,massMeV=938.274):
    return FreqMHz2BetaLambdaM(freqMHz,energyMeV,massMeV=938.274)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


