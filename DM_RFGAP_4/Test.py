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
from EmitNG import EmitN2G3D,EmitG2N3D,EmitN2G
from PartGen import PartGen
from LayerTwiss import LayerTwiss
from LayerMap import LayerMap
from ActionFunction import MyAct, Action_Min_Max
from Constants import pi

from RFGap import LengthCellM
from Twiss import Emit3D

plt.close('all')

wAlphaT=tf.Variable(tf.random_uniform(shape=[3],minval=-1.,maxval=1.))
wGammaT=tf.Variable(tf.random_uniform(shape=[3],minval=0.1,maxval=4.))

wETLMV=tf.Variable(tf.random_uniform(shape=[numCav],minval=0.001,maxval=0.3))
wPhis=tf.Variable(tf.random_uniform(shape=[numCav],minval=-np.pi/2.,maxval=np.pi/2))

##############################################################################


gEmitTInput=EmitN2G3D(nEmitTInput,energyInMeV)
x,xp,y,yp,z,zp=PartGen(numPart)

x,xp,y,yp,phi,Ek=LayerTwiss(x,xp,y,yp,z,zp,gEmitTInput,wAlphaT,wGammaT)

lenCellM=LengthCellM(wETLMV,wPhis)


for iCav in range(numCav):
    ETLMV=wETLMV[iCav]
    lenM=lenCellM[iCav]
    if iCav<numCav-1:
        x,xp,y,yp,phi,Ek=LayerMap(x,xp,y,yp,phi,Ek,ETLMV,lenM)
    else:
        len2M=lenCellM[iCav+1]
        x,xp,y,yp,phi,Ek=LayerMap(x,xp,y,yp,phi,Ek,ETLMV,lenM,LastCellLen=len2M)
    
emitX,emitY,emitZ=Emit3D(x,xp,y,yp,phi,Ek)

lossEmit=emitX*emitY*emitZ                       #  should use n times other than emittance

trainEmit=tf.train.GradientDescentOptimizer(0.01).minimize(lossEmit)



init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(1000):
        sess.run(trainEmit)
    
    
        xRun=sess.run(x)
        xpRun=sess.run(xp)
        yRun=sess.run(y)
        ypRun=sess.run(yp)
        phiRun=sess.run(phi)
        EkRun=sess.run(Ek)
        
        phisRun=sess.run(wPhis)
        ETLRun=sess.run(wETLMV)
        lossEmitRun=sess.run(lossEmit)
    
        
        print('____________________')
        print(phisRun)
        print(ETLRun)
        print(lossEmitRun)

        plt.figure(1)
        plt.clf()
        plt.subplot(221)
        plt.plot(xRun,xpRun,'.')

        plt.subplot(222)
        plt.plot(yRun,ypRun,'.')
    
        plt.subplot(223)
        plt.plot(phiRun,EkRun,'.')
        
        plt.subplot(224)
        plt.hold
        plt.plot(phisRun,'b.')
        plt.plot(ETLRun,'r.')
        
        plt.show()
        
        plt.pause(0.1)


print('OK')



"""

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
"""
'''
init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    
    xRun=sess.run(x1)
    xpRun=sess.run(xp1)
    

    
    print('____________________')
    print(sess.run(nEmitTInput))
    print(sess.run(gEmitTInput))
    print('++++++++++++')
    print(xRun)


    plt.figure(1)
    plt.clf()
    plt.plot(xRun,'.')

    


print('OK')
'''


