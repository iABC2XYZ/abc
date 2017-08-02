#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 22:10:38 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    RFGap
__________________________________________________
    
    K,dE=RFGap()
"""

from InputBeam import qParticle,massMeV,mParticle
from Constants import pi
from BetaGammaC import Energy2BetaGammaC
from InputLattice import freqMHz
from Lambda import LambdaM
import tensorflow as tf

def RFGap(ETLMV,phiPi,energyMeV):
    q_m_ETL=qParticle/mParticle*ETLMV
    pi_q_m_ETL=pi*q_m_ETL
    betaGammaC=Energy2BetaGammaC(energyMeV)
    betaGammaC3=tf.pow(betaGammaC,3)
    lambdaM=LambdaM(freqMHz)
    mc2_beta3_gamma3_lambda=massMeV*betaGammaC3*lambdaM
    sinPhi=tf.sin(phiPi)
    cosPhi=tf.cos(phiPi)
    
    K=tf.multiply(tf.div(pi_q_m_ETL,mc2_beta3_gamma3_lambda),sinPhi)
    dE=tf.multiply(q_m_ETL,cosPhi)
    return K,dE
    








