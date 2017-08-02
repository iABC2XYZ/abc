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
from Twiss import Emit3DLimit

import matplotlib.pyplot as plt

import tensorflow as tf
from APF import * 
from EmitNG import EmitG2N3D,EmitN2G3D
import numpy as np
from PartLimit import PartLimit6D


wAlphaT=tf.Variable(tf.random_uniform(shape=[3],minval=-1.,maxval=1.))
wBetaT=tf.Variable(tf.random_uniform(shape=[3],minval=0.1,maxval=4.))

wETLMV=tf.Variable(tf.random_uniform(shape=[numCav],minval=0.001,maxval=0.3))
wLenCellM=tf.Variable(tf.random_uniform(shape=[numCav+1],minval=0.001,maxval=0.3))

##############################################################################
emitTNProd_bk=tf.reduce_prod(tf.pow(emitN,0.1))
emitG=EmitN2G3D(emitN,energyInMeV)

x0,xp0,y0,xp0,phi0,Ek0= PartGen6D(emitG,wAlphaT,wBetaT,numPart,energyInMeV,freqMHz)

x1,xp1,y1,xp1,phi1,Ek1=APF(wETLMV,wLenCellM,x0,xp0,y0,xp0,phi0,Ek0)

x,xp,y,xp,phi,Ek=PartLimit6D(x1,xp1,y1,xp1,phi1,Ek1)

emitTG=Emit3DLimit(x,xp,y,xp,phi,Ek,energyOutMeV,freqMHz)

#_____________________________________________________________________________

emitTN=EmitG2N3D(emitTG,energyOutMeV)
emitTNProd=tf.reduce_prod(tf.pow(emitTN,0.1))

EmitGrowth=tf.div(emitTNProd,emitTNProd_bk)

lossEmit=EmitGrowth
optimizerEmit=tf.train.AdamOptimizer(0.001)
trainEmit=optimizerEmit.minimize(lossEmit)



init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(emitTG))
    for _ in range(30):
        print(sess.run(Ek))
        print(sess.run(lossEmit))
        print(sess.run(emitTN))
        sess.run(trainEmit)
        
    

    
    #xp2T=sess.run(xp2)
    #y2T=sess.run(y2)
    #yp2T=sess.run(yp2)
    #phi2T=sess.run(phi2)
    #Ek2T=sess.run(Ek2)   
    
    #print(AllTestT.shape)
    
    

    #print([len(x2T),len(xp2T),len(y2T),len(yp2T),len(phi2T),len(Ek2T)])

    


print('OK')



