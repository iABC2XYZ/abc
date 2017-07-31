#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 22:24:47 2017

@author: A
"""


import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from BetaGammaC import *
from GenPartilces import *
from EmitNG import * 
from Statistics import *
from BasicInput import *
from ConstPhysics import *
from RFCal import * 

def CalEnergyGain7ETL(ETL,phisPi,q=1,m=1):
    return q/m*ETL*tf.cos(phisPi)

def CalEnergyUpdate7ETL(energyIn,ETL,phisPi,q=1,m=1):
    dE=CalEnergyGain7ETL(ETL,phisPi,q=1,m=1)
    
    dEAll=tf.cumsum(dE)
        
    energyOut=tf.concat([energyIn,tf.add(dEAll,energyIn)],0)
    
    return energyOut

def CalDeltaPhi(phisPi):
    d1Phi=tf.expand_dims(phisPi[0],0)
    d2Phi=tf.expand_dims(phisPi[-1],0)
    d0Phi=phisPi[1::]-phisPi[0:-1:]
    
    dPhi=tf.concat([d1Phi,d0Phi,d2Phi],0)
    return dPhi


def CalCellLength7ETL(energyIn,ETL,phisPi,freqMHz,q=1,m=1):
    deltaPhi=CalDeltaPhi(phisPi)
    
    energyCell=CalEnergyUpdate7ETL(energyIn,ETL,phisPi,q=1,m=1)
    betalambdaMCell=Energy2BetaLambdaM(freqMHz,energyIn)    
    
    cellLength=(deltaPhi+Pi)/(2.*Pi)*betalambdaMCell

    return  cellLength
    

def MapDrift(freqMHz,lenCell,x,xp,y,yp,phiPi,energyMeV):
    
    energyMeV=tf.abs(energyMeV)        #  ###########################################
    
    x=x+tf.multiply(xp,lenCell)
    xp=xp
    y=y+tf.multiply(yp,lenCell)
    yp=yp
    
    betaLambdaM=Energy2BetaLambdaM(freqMHz,energyMeV)
    phiPi=phiPi+tf.div(2.*Pi*lenCell,betaLambdaM)-Pi
    energyMeV=energyMeV
    return x,xp,y,yp,phiPi,energyMeV
    
    

def MapGap(freqMHz,uETLMV,x,xp,y,yp,phiPi,energyMeV,massMeV=938.274,q=1.,m=1.):
    

    energyMeV=tf.abs(energyMeV)    #  ###########################################
    
    betaGammaC=Energy2BetaGammaC(energyMeV,massMeV=938.274)
    betaGammaC_3=tf.pow(betaGammaC,3)
    
    lambdaM=CalWavelength(freqMHz)
    
    K=Pi*(q/m)*uETLMV/(massMeV*betaGammaC_3*lambdaM)*tf.sin(phiPi)
    
    x=x
    xp=xp-K*x
    y=y
    yp=yp-K*y
    
    phiPi=phiPi
    energyMeV=energyMeV+(q/m)*uETLMV*tf.cos(phiPi)
    
    return x,xp,y,yp,phiPi,energyMeV



def MapAPF(numCav,freqMHz,cellLength,uGapETLMV,x,xp,y,yp,phiPi,energyMeV,massMeV=938.274,q=1.,m=1.):

    for iCav in xrange(numCav):
        lenCell=cellLength[iCav]
        uETLMV=uGapETLMV[iCav]
        x,xp,y,yp,phiPi,energyMeV=MapDrift(freqMHz,lenCell,x,xp,y,yp,phiPi,energyMeV)
        x,xp,y,yp,phiPi,energyMeV=MapGap(freqMHz,uETLMV,x,xp,y,yp,phiPi,energyMeV,massMeV=938.274,q=1.,m=1.)
    lenCell=cellLength[numCav]
    x,xp,y,yp,phiPi,energyMeV=MapDrift(freqMHz,lenCell,x,xp,y,yp,phiPi,energyMeV)
    return x,xp,y,yp,phiPi,energyMeV
    


def CalLinac(numCav,constEnergyInMeV,constFreqMHz,WeightsPhisPi,WeightsETLMV,x,xp,y,yp,phiPi,energyMeV,massMeV):
    cellLength=CalCellLength7ETL(constEnergyInMeV,WeightsETLMV,WeightsPhisPi,constFreqMHz)
    disX,disXp,disY,disYp,disPhiPi,disEnergy=MapAPF(numCav,constFreqMHz,cellLength,WeightsETLMV,x,xp,y,yp,phiPi,energyMeV,massMeV)
    return disX,disXp,disY,disYp,disPhiPi,disEnergy





        
















