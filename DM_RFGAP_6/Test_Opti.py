#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:29:03 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    Test

        完整可用，但不带优化
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
from BetaGammaC import Energy2BetaC




plt.close('all')

wAlphaT=tf.Variable(tf.random_uniform(shape=[3],minval=-1.,maxval=1.))
wGammaT=tf.Variable(tf.random_uniform(shape=[3],minval=0.1,maxval=4.))

wETLMV=tf.Variable(tf.random_uniform(shape=[numCav],minval=0.001,maxval=0.3))
wPhis=tf.Variable(tf.random_uniform(shape=[numCav],minval=-np.pi/2.,maxval=np.pi/2))

##############################################################################


gEmitTInput=EmitN2G3D(nEmitTInput,energyInMeV)


xH=tf.placeholder(tf.float32,[None,1])
xpH=tf.placeholder(tf.float32,[None,1])
yH=tf.placeholder(tf.float32,[None,1])
ypH=tf.placeholder(tf.float32,[None,1])
zH=tf.placeholder(tf.float32,[None,1])
zpH=tf.placeholder(tf.float32,[None,1])

#for iCav in range(numCav):
tf.assign(wETLMV,tf.abs(wETLMV))


lenCellM=LengthCellM(wETLMV,wPhis)

x,xp,y,yp,z,betaC,numPartLost=LayerTwiss(xH,xpH,yH,ypH,zH,zpH,gEmitTInput,wAlphaT,wGammaT)


for iCav in range(numCav):
    ETLMV=wETLMV[iCav]
    lenM=lenCellM[iCav]
    if iCav<numCav-1:
        x,xp,y,yp,z,betaC,numPartLost=LayerMap(x,xp,y,yp,z,betaC,ETLMV,lenM)
    else:
        len2M=lenCellM[iCav+1]
        x,xp,y,yp,z,betaC,numPartLost=LayerMap(x,xp,y,yp,z,betaC,ETLMV,lenM,LastCellLen=len2M)
    




betaCOut=Energy2BetaC(energyOutMeV)
dBetaC=tf.abs(betaC-betaCOut)


lossBetaC=dBetaC
lossX=x
lossX2=x**2+xp**2
loss4D=x**2+xp**2+z**2+dBetaC**2


optiLoss=tf.train.AdamOptimizer(0.025)
trainBetaC=optiLoss.minimize(lossBetaC)
trainX=optiLoss.minimize(loss4D)

#________________________________________________________________________________________________________
init=tf.global_variables_initializer()

sess=tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=False))


sess.run(init)

#U=[]
#phiS=[]

for _ in range(1000):
    
    xIn,xpIn,yIn,ypIn,zIn,zpIn=PartGen(numPart)
    
    #sess.run(trainBetaC,feed_dict={xH:xIn,xpH:xpIn,yH:yIn,ypH:ypIn,zH:zIn,zpH:zpIn})
    sess.run(trainX,feed_dict={xH:xIn,xpH:xpIn,yH:yIn,ypH:ypIn,zH:zIn,zpH:zpIn})
    
    UR=sess.run(wETLMV)
    phisR=sess.run(wPhis)
    
    print(UR)
    
    if _ ==0:
        plt.figure(2)
        plt.clf()
        plt.subplot(211)
        plt.plot(UR,'r.')
        
        plt.subplot(212)
        plt.plot(phisR,'r.')
        
        plt.pause(0.1)
        plt.show()
    
    
    plt.figure(1)
    plt.clf()
    plt.subplot(211)
    plt.plot(UR,'.')
    
    plt.subplot(212)
    plt.plot(phisR,'.')
    
    plt.pause(0.1)
    plt.show()
    















