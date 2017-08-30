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
from InputLattice import freqMHz
import tensorflow as tf
from BetaGammaC import Beta2GammaC
from Lambda import LambdaM,BetaLambdaM




def RFGap(z,betaC,ETLMV):
    q_m_ETL=qParticle/mParticle*ETLMV
    pi_q_m_ETL=pi*q_m_ETL
    
    gammaC=Beta2GammaC(betaC)
    
    betaCGammaC3=betaC*gammaC**3
    betaC3GammaC3=betaC**3*gammaC**3
    
    lambdaM=LambdaM(freqMHz)
    
    phi=2.*pi*z/(betaC*lambdaM)
    
    K=pi_q_m_ETL/(betaC3GammaC3*lambdaM*massMeV)*tf.sin(phi)
    dBeta=q_m_ETL/(betaCGammaC3*massMeV)*tf.cos(phi)
    
    return K,dBeta
    


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






