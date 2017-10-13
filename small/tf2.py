#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 08:29:25 2017

@author: A
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

import sys
sys.path.append("/home/A/Pictures")

import BetaGammaC

#import('/home/A/Pictures/BetaGammaC')

constEnergyInMeV=tf.constant([0.6])
constEnergyOutMeV=tf.constant([4.])

constEmitN=tf.constant([1.,1.,1.])

numPart=np.int32(1e5)

numCav=np.int32(60)

#####################


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



constGammaIn=Energy2GammaC(constEnergyInMeV)
constBetaIn=Enerty2BetaC(constEnergyInMeV)
constEmitG=constEmitN/(constGammaIn*constBetaIn)


#################################################################

WeightsBetaT=tf.Variable(tf.random_uniform(shape=[3],minval=0.1,maxval=4.))
WeightsAlphaT=tf.Variable(tf.random_uniform(shape=[3],minval=-1.,maxval=1.))


def GenGammaT5Twiss(alphaT2D,betaT2D):
    gammaT2D=tf.div(1.+tf.square(alphaT2D),betaT2D)
    return gammaT2D

def Gen2DPart5Twiss(emitG2D,alphaT2D,betaT2D):
    x=tf.random_normal([numPart])
    xp=tf.random_normal([numPart])
    
    gammaT2D=GenGammaT5Twiss(alphaT2D,betaT2D)
    X=tf.sqrt(emitG2D/gammaT2D)*(x-alphaT2D*xp)
    XP=tf.sqrt(emitG2D*gammaT2D)*xp
    return X,XP
    
def GetTwiss2D(x,xp):
    xMean=tf.reduce_mean(x)
    xxVar=tf.reduce_mean(tf.square(x-xMean))
    xpMean=tf.reduce_mean(xp)
    xpxpVar=tf.reduce_mean(tf.square(xp-xpMean))
    xxpVar=tf.reduce_mean((x-xMean)*(xp-xpMean))
    
    emitT=tf.sqrt(xxVar*xpxpVar-xxpVar*xxpVar)
    betaT=xxVar/emitT
    alphaT=-xxpVar/emitT
    gammaT=xpxpVar/emitT
    
    return emitT,alphaT,betaT,gammaT
    

def Gen6DPart5Twiss(emitG6D,alphaT6D,betaT6D):
    X,XP=Gen2DPart5Twiss(emitG6D[0],alphaT6D[0],betaT6D[0])
    Y,YP=Gen2DPart5Twiss(emitG6D[1],alphaT6D[1],betaT6D[1])
    Z,ZP=Gen2DPart5Twiss(emitG6D[2],alphaT6D[2],betaT6D[2])
    return X,XP,Y,YP,Z,ZP






    
x,xp=Gen2DPart5Twiss(1,0.5,1)
emitT,alphaT,betaT,gammaT=GetTwiss2D(x,xp)

tmp=[emitT,alphaT,betaT,gammaT]




init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print sess.run(tmp)
    print sess.run(constEmitG)
    

    
    
    
    #print sess.run(WeightsBetaT)
    #print sess.run(WeightsAlphaT)
    #print sess.run(weightsGammaT)






print('OK')





import os
print os.getcwd()
