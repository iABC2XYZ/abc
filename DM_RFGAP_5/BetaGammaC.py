#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:19:35 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    BetaC & GammaC:
    _______________________________________________________
    
    Energy -> Gamma
    Energy -> Beta
    Energy->Beta*Gamma
    Energy->Beta, Gamma
    
    Gamma->Energy
    Gamma->Beta
    Gamma->Beta*Gamma
    
    Beta->Gamma
    Beta->Energy
    Beta->Beta*Gamma
    
    Beta*Gamma->Energy
    Beta*Gamma->Gamma
    Beta*Gamma->Beta
    Beta*Gamma->Beta,Gamma
    
    

"""


import tensorflow as tf
from InputBeam import massMeV


def Energy2GammaC(energyMeV):
    gammaC=1.+tf.div(energyMeV,massMeV)
    return gammaC

def Energy2BetaC(energyMeV):
    gammaC=Energy2GammaC(energyMeV)
    betaC=GammaC2BetaC(gammaC)
    return betaC

def Energy2BetaGammaC(energyMeV):
    gammaC=Energy2GammaC(energyMeV)
    betaC=GammaC2BetaC(gammaC)
    betaGammaC=betaC*gammaC
    return betaGammaC

def Energy2BetaC_GammaC(energyMeV):
    gammaC=Energy2GammaC(energyMeV)
    betaC=GammaC2BetaC(gammaC)
    return betaC,gammaC
    

def GammaC2Energy(gammaC):
    energyMeV=(gammaC-1.)*massMeV
    return energyMeV

def GammaC2BetaC(gammaC):
    betaC=tf.sqrt(1.-tf.div(1.,tf.square(gammaC)))
    return betaC

def GammaC2BetaGammaC(gammaC):
    betaC=GammaC2BetaC(gammaC)
    betaGammaC=betaC*gammaC
    return betaGammaC

def Beta2Energy(betaC):
    gammaC=Beta2GammaC(betaC)
    energyMeV=GammaC2Energy(gammaC)
    return energyMeV

def Beta2GammaC(betaC):
    gammaC=tf.div(1.,tf.sqrt(1.-tf.square(betaC)))
    return gammaC

def Beta2BetaGammaC(betaC):
    gammaC=Beta2GammaC(betaC)
    betaGammaC=betaC*gammaC
    return betaGammaC    

def BetaGammaC2Energy(betaGammaC):
    gammaC=BetaGammaC2GammaC(betaGammaC)
    energyMeV=GammaC2Energy(gammaC)
    return energyMeV

def BetaGammaC2GammaC(betaGammaC):
    gammaC=tf.sqrt(tf.square(betaGammaC)+1.)
    return gammaC

def BetaGammaC2BetaC(betaGammaC):
    gammaC=BetaGammaC2GammaC(betaGammaC)
    betaC=GammaC2BetaC(gammaC)
    return betaC

def BetaGammaC2BetaC_gammaC(betaGammaC):
    gammaC=BetaGammaC2GammaC(betaGammaC)
    betaC=GammaC2BetaC(gammaC)
    return betaC,gammaC

