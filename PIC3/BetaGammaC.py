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

from Constants import massMeV
import numpy as np
from Constants import c


def NP_Energy2GammaC(energyMeV):
    gammaC=1.+energyMeV/massMeV
    return gammaC

def NP_Energy2BetaC(energyMeV):
    gammaC=NP_Energy2GammaC(energyMeV)
    betaC=NP_GammaC2BetaC(gammaC)
    return betaC

def NP_Energy2BetaGammaC(energyMeV):
    gammaC=NP_Energy2GammaC(energyMeV)
    betaC=NP_GammaC2BetaC(gammaC)
    betaGammaC=betaC*gammaC
    return betaGammaC

def NP_Energy2BetaC_GammaC(energyMeV):
    gammaC=NP_Energy2GammaC(energyMeV)
    betaC=NP_GammaC2BetaC(gammaC)
    return betaC,gammaC
    

def NP_GammaC2Energy(gammaC):
    energyMeV=(gammaC-1.)*massMeV
    return energyMeV

def NP_GammaC2BetaC(gammaC):
    betaC=np.sqrt(1.-1./gammaC**2)
    return betaC

def NP_GammaC2BetaGammaC(gammaC):
    betaC=NP_GammaC2BetaC(gammaC)
    betaGammaC=betaC*gammaC
    return betaGammaC

def NP_Beta2Energy(betaC):
    gammaC=NP_Beta2GammaC(betaC)
    energyMeV=NP_GammaC2Energy(gammaC)
    return energyMeV

def NP_Beta2GammaC(betaC):
    gammaC=1./np.sqrt(1.-betaC**2)
    return gammaC

def NP_Beta2BetaGammaC(betaC):
    gammaC=NP_Beta2GammaC(betaC)
    betaGammaC=betaC*gammaC
    return betaGammaC    

def NP_BetaGammaC2Energy(betaGammaC):
    gammaC=NP_BetaGammaC2GammaC(betaGammaC)
    energyMeV=NP_GammaC2Energy(gammaC)
    return energyMeV

def NP_BetaGammaC2GammaC(betaGammaC):
    gammaC=np.sqrt(betaGammaC**2+1.)
    return gammaC

def NP_BetaGammaC2BetaC(betaGammaC):
    gammaC=NP_BetaGammaC2GammaC(betaGammaC)
    betaC=NP_GammaC2BetaC(gammaC)
    return betaC

def NP_BetaGammaC2BetaC_gammaC(betaGammaC):
    gammaC=NP_BetaGammaC2GammaC(betaGammaC)
    betaC=NP_GammaC2BetaC(gammaC)
    return betaC,gammaC

#-------------------------------------------------------------------------
def NP_LambdaM(freq):
    lamndaM=c/(freq)
    return lamndaM
    

def NP_Energy2BetaLambdaM(energyMeV,freq):
    betaC=NP_Energy2BetaC(energyMeV)
    lamndaM=NP_LambdaM(freq)
    betaLambdaM=betaC*lamndaM
    return betaLambdaM












