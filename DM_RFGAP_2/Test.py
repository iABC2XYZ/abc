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

xNan=tf.is_nan(x)

#xNanPrint=x[xNan]

init=tf.global_variables_initializer()



with tf.Session() as sess:
    sess.run(init)
    print(sess.run(x))
    print(sess.run(xNan))
    #print(sess.run(xNanPrint))


    


print('OK')




