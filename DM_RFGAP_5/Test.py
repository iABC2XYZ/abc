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

import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from EmitNG import EmitN2G3D
from PartGen import PartGen
from LayerTwiss import LayerTwiss
from LayerMap import LayerMap

from ActionFunction import MyAct
from RFGap import LengthCellM
from Twiss import Emit3D




plt.close('all')

wAlphaT=tf.Variable(tf.random_uniform(shape=[3],minval=-1.,maxval=1.))
wGammaT=tf.Variable(tf.random_uniform(shape=[3],minval=0.1,maxval=4.))

wETLMV=tf.Variable(tf.random_uniform(shape=[numCav],minval=0.001,maxval=0.3))
wPhis=tf.Variable(tf.random_uniform(shape=[numCav],minval=-np.pi/2.,maxval=np.pi/2))

##############################################################################
lenCellM=LengthCellM(wETLMV,wPhis)

gEmitTInput=EmitN2G3D(nEmitTInput,energyInMeV)

nEmitXYZ_0=tf.reduce_prod(gEmitTInput)

x,xp,y,yp,z,zp=PartGen(numPart)

x,xp,y,yp,z,betaC,numPartLost=LayerTwiss(x,xp,y,yp,z,zp,gEmitTInput,wAlphaT,wGammaT)




emitN=[]
for iCav in range(numCav):
    ETLMV=wETLMV[iCav]
    lenM=lenCellM[iCav]
    if iCav<numCav-1:
        x,xp,y,yp,z,betaC,numPartLost=LayerMap(x,xp,y,yp,z,betaC,ETLMV,lenM)
    else:
        len2M=lenCellM[iCav+1]
        x,xp,y,yp,z,betaC,numPartLost=LayerMap(x,xp,y,yp,z,betaC,ETLMV,lenM,LastCellLen=len2M)
    
    emitX,emitY,emitZ=Emit3D(x,xp,y,yp,z,betaC,energyOutMeV)
    
    isNanX=tf.is_nan(emitX)
    isNanY=tf.is_nan(emitY)
    isNanZ=tf.is_nan(emitZ)
    
    isNan=tf.logical_or(isNanX,tf.logical_or(isNanY,isNanZ))
    
    nEmitXYZ=tf.cond(isNan,lambda: tf.constant([1.]),lambda: emitX*emitY*emitZ)
    
    nEmitXYZ*=tf.to_float(numPartLost+1)
    
    emitN.append(nEmitXYZ/nEmitXYZ_0)


lossPart=tf.reduce_mean(emitN)

optiPart=tf.train.GradientDescentOptimizer(0.01)
trainPart=optiPart.minimize(lossPart)

Test=[]
Test.append(x)
Test.append(xp)
Test.append(y)
Test.append(yp)
Test.append(z)
Test.append(betaC)




init=tf.global_variables_initializer()

sess=tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
#sess=tf.Session()

sess.run(init)

print(sess.run(lossPart))

for _ in range(3000):
    sess.run(trainPart)
    
    print(sess.run(lossPart))
    print(sess.run(nEmitXYZ))
    
    U=sess.run(wETLMV)
    phiS=sess.run(wPhis)
    
    plt.figure(1)
    plt.clf()
    plt.subplot(211)
    plt.plot(U,'.')

    plt.subplot(212)
    plt.plot(phiS,'.')
    
    plt.show()
    plt.pause(0.1)
    
    
