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

WeightsAlphaT=tf.Variable(tf.random_uniform(shape=[3],minval=-1.,maxval=1.))
WeightsBetaT=tf.Variable(tf.random_uniform(shape=[3],minval=0.1,maxval=4.))

WeightsPotential=tf.Variable(tf.random_uniform(shape=[numCav],minval=30.,maxval=200.))
WeightsPhis=tf.Variable(tf.random_uniform(shape=[numCav],minval=-np.pi/2.,maxval=np.pi/2.))

#################################################################

constEmitG=EmitN2G(constEnergyInMeV,constEmitN)
x,xp,y,yp,z,zp=Gen6DPart5Twiss(constEmitG,WeightsAlphaT,WeightsBetaT,numPart)



emitT,alphaT,betaT,gammaT=GetTwiss6D(x,xp,y,yp,z,zp)


init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print sess.run(constEmitG)
    print sess.run(emitT)
    print "_________________"
    print(sess.run(WeightsAlphaT))
    print(sess.run(alphaT))
    print "_________________"
    print(sess.run(WeightsBetaT))
    print(sess.run(betaT))
    print "_________________"
    print sess.run(constEmitN)
    print sess.run(EmitG2N(constEnergyInMeV,emitT))    

    


print('OK')

