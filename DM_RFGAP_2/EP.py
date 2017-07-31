#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:48:25 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    Energy <-> Momentum    :     E  <-> P
    
    
    
    

"""

from BetaGammaC import *

def dE2dP_gammaC(dE_E,gammaSyn):
    dP_P=tf.div(gammaSyn,1+gammaSyn)*dE_E
    return dP_P

def dP2dE_gammaC(dP_P,gammaSyn):
    dE_E=tf.div(1+gammaSyn,gammaSyn)*dP_P
    return dE_E

def dE2dP_energy(dE_E,energySyn):
    gammaSyn=Energy2GammaC(energySyn)
    dP_P=tf.div(gammaSyn,1+gammaSyn)*dE_E
    return dP_P

def dP2dE_energy(dP_P,energySyn):
    gammaSyn=Energy2GammaC(energySyn)
    dE_E=tf.div(1+gammaSyn,gammaSyn)*dP_P
    return dE_E


