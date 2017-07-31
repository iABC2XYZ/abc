#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 08:29:25 2017

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
from RFGap import * 



WeightsAlphaT=tf.Variable(tf.random_uniform(shape=[3],minval=-1.,maxval=1.))
WeightsBetaT=tf.Variable(tf.random_uniform(shape=[3],minval=0.1,maxval=4.))

WeightsETLMV=tf.Variable(tf.random_uniform(shape=[numCav],minval=0.030,maxval=0.200))
WeightsPhisPi=tf.Variable(tf.random_uniform(shape=[numCav],minval=-np.pi/2.,maxval=np.pi/2.))

#_____________________________________________________________________________________________________
constEmitG=Emit3DN2G(constEnergyInMeV,constEmitN)

#################################################################

WeightsETLMVUpdate=tf.abs(WeightsETLMV)

disX,disXp,disY,disYp,disPhiPi,disEnergy=Gen6D4RFgap(constEmitG,WeightsAlphaT,WeightsBetaT,constEnergyInMeV,constFreqMHz,numPart)

disX,disXp,disY,disYp,disPhiPi,disEnergy= CalLinac(numCav,constEnergyInMeV,constFreqMHz,WeightsPhisPi,WeightsETLMV,disX,disXp,disY,disYp,disPhiPi,disEnergy,massMeV)

emitT,alphaT,betaT,gammaT=CalTwiss6D(disX,disXp,disY,disYp,disPhiPi,disEnergy,constEnergyOutMeV,constFreqMHz)

endEmitTN=Emit3DG2N(constEnergyOutMeV,emitT)


lossEmit=tf.div(tf.reduce_prod(endEmitTN),tf.reduce_prod(constEmitN))
optimizerEmit=tf.train.AdamOptimizer(0.5)

trainEmit=optimizerEmit.minimize(lossEmit)



init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for _ in xrange(100):
        print sess.run(endEmitTN)
        print sess.run(disX)
        sess.run(WeightsETLMVUpdate)
        sess.run(trainEmit)
        #print sess.run(lossEmit)

    


























'''
emitT,alphaT,betaT,gammaT=GetTwiss6DMat(x)


lossX=tf.reduce_mean(tf.abs(alphaT)+tf.abs(betaT)+tf.abs(gammaT))

optimizerX=tf.train.AdamOptimizer(0.5)

trainX=optimizerX.minimize(lossX)


#def EnergyGain(potentialMV,phisPi):


    



#_____________________________________________________________________________________________________
init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in xrange(50):
        sess.run(trainX)
        print sess.run(lossX)
'''

    
    

    


print('OK')




