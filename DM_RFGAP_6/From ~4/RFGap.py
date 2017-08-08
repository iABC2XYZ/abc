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

from InputBeam import qParticle,massMeV,mParticle,energyInMeV
from Constants import pi
from BetaGammaC import Energy2BetaGammaC
from InputLattice import freqMHz
from Lambda import LambdaM
import tensorflow as tf
from Lambda import BetaLambdaM


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
    

def LengthCellM(wETLMV,wPhis):
    dE=qParticle/mParticle*wETLMV*tf.cos(wPhis)
    Ek=energyInMeV+tf.cumsum(dE)
    energy=tf.concat([energyInMeV,Ek],0)
    betaLambdaM=BetaLambdaM(energy,freqMHz)
    
    dPhi_0=wPhis[1::]-wPhis[0:-1:]+pi
    dPhi_1=tf.expand_dims(wPhis[0]+pi, 0)
    dPhi_2=tf.expand_dims(wPhis[-1]+pi,0)
    dPhi=tf.concat([dPhi_1,dPhi_0,dPhi_2],0)
    
    lenCellM=betaLambdaM*dPhi/(2.*pi)
    
    return lenCellM






