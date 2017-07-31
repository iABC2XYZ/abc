#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:29:03 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    Test

"""
from InputBeam import *
from InputLattice import *

from PartGen import PartGen6D
from Twiss import Twiss6D

import matplotlib.pyplot as plt

import tensorflow as tf
from APF import * 
from EmitNG import EmitG2N3D,EmitN2G3D

wAlphaT=tf.Variable(tf.random_uniform(shape=[3],minval=-1.,maxval=1.))
wBetaT=tf.Variable(tf.random_uniform(shape=[3],minval=0.1,maxval=4.))

wETLMV=tf.Variable(tf.random_uniform(shape=[numCav],minval=0.001,maxval=0.3))
wLenCellM=tf.Variable(tf.random_uniform(shape=[numCav+1],minval=0.001,maxval=0.3))

##############################################################################

emitG=EmitN2G3D(emitN,energyInMeV)

x,xp,y,xp,phi,Ek= PartGen6D(emitG,wAlphaT,wBetaT,numPart,energyInMeV,freqMHz)

emitT,alphaT,betaT,gammaT=Twiss6D(x,xp,y,xp,phi,Ek,energyOutMeV,freqMHz)

test=tf.multiply(alphaT,emitT)


x,xp,y,xp,phi,Ek=APF(wETLMV,wLenCellM,x,xp,y,xp,phi,Ek)

def IDNonNan6D(disX,disXP,disY,disYP,disPhiPi,disEnergy):
    xNan=tf.is_nan(disX)
    xpNan=tf.is_nan(disXP)
    yNan=tf.is_nan(disY)
    ypNan=tf.is_nan(disYP)
    phiNan=tf.is_nan(disPhiPi)
    energyNan=tf.is_nan(disEnergy)
    
    idXNan=tf.transpose(tf.where(~xNan))
    idXpNan=tf.transpose(tf.where(~xpNan))
    idYNan=tf.transpose(tf.where(~yNan))
    idYpNan=tf.transpose(tf.where(~ypNan))
    idPhiNan=tf.transpose(tf.where(~phiNan))
    idEnergyNan=tf.transpose(tf.where(~energyNan))
    
    idNonNanAll=tf.concat([idXNan,idXpNan,idYNan,idYpNan,idPhiNan,idEnergyNan],1)
    
    idNonNan,idNonNanAllTmp=tf.unique(idNonNanAll[0,:])

    return idNonNan

def PartNonNan6D(disX,disXP,disY,disYP,disPhiPi,disEnergy):
    idNonNan=IDNonNan6D(disX,disXP,disY,disYP,disPhiPi,disEnergy)
    x=tf.gather(disX,idNonNan)
    xp=tf.gather(disXP,idNonNan)
    y=tf.gather(disY,idNonNan)
    yp=tf.gather(disYP,idNonNan)
    phi=tf.gather(disPhiPi,idNonNan)
    energy=tf.gather(disEnergy,idNonNan)
    numNonNan=tf.shape(idNonNan)
    return x,xp,y,yp,phi,energy,numNonNan
    
 
x2,xp2,y2,yp2,phi2,energy2,numNonNan=PartNonNan6D(x,xp,y,xp,phi,Ek)



init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(x2))


    


print('OK')




