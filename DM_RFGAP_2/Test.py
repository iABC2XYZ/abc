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
from PartLimit import PartLimit6D,PartMaxPow6D,PartMax6D


wAlphaT=tf.Variable(tf.random_uniform(shape=[3],minval=-1.,maxval=1.))
wBetaT=tf.Variable(tf.random_uniform(shape=[3],minval=0.1,maxval=4.))

wETLMV=tf.Variable(tf.random_uniform(shape=[numCav],minval=0.001,maxval=0.3))
wLenCellM=tf.Variable(tf.random_uniform(shape=[numCav+1],minval=0.001,maxval=0.3))

##############################################################################
emitTNProd_Input=tf.reduce_prod(emitTN_Input)
emitTG_Input=EmitN2G3D(emitTN_Input,energyInMeV)

x0,xp0,y0,xp0,phi0,Ek0= PartGen6D(emitTG_Input,wAlphaT,wBetaT,numPart,energyInMeV,freqMHz)

x1,xp1,y1,xp1,phi1,Ek1=APF(wETLMV,wLenCellM,x0,xp0,y0,xp0,phi0,Ek0)

#___________________________________________________________________________
xMaxEmit,yMaxEmit,zMaxEmit=PartMaxPow6D(x1,xp1,y1,xp1,phi1,Ek1,coePow=0.01)

maxX,maxXP,maxY,maxYP,maxPhi,maxEnergy=PartMax6D(x1,xp1,y1,xp1,phi1,Ek1)

x,xp,y,xp,phi,Ek=PartLimit6D(x1,xp1,y1,xp1,phi1,Ek1)

emitTG_OutputTmp=Emit3DLimit(x,xp,y,xp,phi,Ek,energyOutMeV,freqMHz)
emitTG_Output=emitTG_OutputTmp*[xMaxEmit,yMaxEmit,zMaxEmit]


#_____________________________________________________________________________

emitTN_Output=EmitG2N3D(emitTG_Output,energyOutMeV)
emitTNProd_Output=tf.reduce_prod(tf.pow(emitTN_Output,0.01))

EmitGrowth=tf.div(emitTNProd_Output,emitTNProd_Input)

#_____________________________________________

lossEmit=EmitGrowth
optimizerEmit=tf.train.AdamOptimizer(0.001)
trainEmit=optimizerEmit.minimize(lossEmit)

#____________________________________________

#oTest=tf.concat([x,xp,y,xp,phi,Ek],0)
oTest=[maxX,maxXP,maxY,maxYP,maxPhi,maxEnergy]

#_______________________________________________

init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(300):
        print('____________________')
        print(sess.run(wBetaT))
        print(sess.run(wAlphaT))
        print(sess.run(wETLMV))
        print(sess.run(wLenCellM))
        print(sess.run(lossEmit))
        sess.run(trainEmit)
        
    

    

    


print('OK')



