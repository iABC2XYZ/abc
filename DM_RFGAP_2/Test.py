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



WeightsAlphaT=tf.Variable(tf.random_uniform(shape=[3],minval=-1.,maxval=1.))
WeightsBetaT=tf.Variable(tf.random_uniform(shape=[3],minval=0.1,maxval=4.))

disX,disXP,disY,disYP,disPhiPi,disEnergy= PartGen6D(emitN,WeightsAlphaT,WeightsBetaT,numPart,energyInMeV,freqMHz)

emitT,alphaT,betaT,gammaT=Twiss6D(disX,disXP,disY,disYP,disPhiPi,disEnergy,energyInMeV,freqMHz)


init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print sess.run(emitT)
    print sess.run(alphaT)
    print sess.run(WeightsAlphaT)
    print sess.run(betaT)
    print sess.run(WeightsBetaT)
    
    plt.figure('x')
    plt.plot(x,xp,'.')



