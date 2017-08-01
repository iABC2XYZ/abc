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
import numpy as np


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


def PartNonNan6D(disX,disXP,disY,disYP,disPhiPi,disEnergy):
    xNonNan=~tf.is_nan(disX)
    xpNonNan=~tf.is_nan(disXP)
    yNonNan=~tf.is_nan(disY)
    ypNonNan=~tf.is_nan(disYP)
    phiNonNan=~tf.is_nan(disPhiPi)
    energyNonNan=~tf.is_nan(disEnergy)
    
    xBoolNonNan=tf.logical_and(xNonNan,xpNonNan)
    yBoolNonNan=tf.logical_and(yNonNan,ypNonNan)
    zBoolNonNan=tf.logical_and(phiNonNan,energyNonNan)
    xyBoolNonNan=tf.logical_and(xBoolNonNan,yBoolNonNan)
    boolNonNan=tf.logical_and(xyBoolNonNan,zBoolNonNan)
    
    x=tf.boolean_mask(disX,boolNonNan)
    xp=tf.boolean_mask(disXP,boolNonNan)
    y=tf.boolean_mask(disY,boolNonNan)
    yp=tf.boolean_mask(disYP,boolNonNan)
    phi=tf.boolean_mask(disPhiPi,boolNonNan)
    energy=tf.boolean_mask(disEnergy,boolNonNan)
    
    numParNon=tf.shape(energy)
    numParNan=numPart-numParNon[0]

    return x,xp,y,yp,phi,energy,numParNan
    

def Twiss6DNan(disX,disXP,disY,disYP,disPhiPi,disEnergy,energySyn,freqMHz):
    x,xp,y,xp,phi,Ek,numParNan=PartNonNan6D(disX,disXP,disY,disYP,disPhiPi,disEnergy)
    emitT=tf.where(tf.is_inf(xp))
    
    

    return emitT


#x2,xp2,y2,yp2,phi2,Ek2,numParNon=PartNonNan6D(x,xp,y,xp,phi,Ek)

emitT2=Twiss6DNan(x,xp,y,xp,phi,Ek,energyOutMeV,freqMHz)


init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(emitT2))
    

    
    #xp2T=sess.run(xp2)
    #y2T=sess.run(y2)
    #yp2T=sess.run(yp2)
    #phi2T=sess.run(phi2)
    #Ek2T=sess.run(Ek2)   
    
    #print(AllTestT.shape)
    
    

    #print([len(x2T),len(xp2T),len(y2T),len(yp2T),len(phi2T),len(Ek2T)])

    


print('OK')



