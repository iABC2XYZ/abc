#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:29:03 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    Test

        完整可用，带优化
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
#wETLMV=tf.constant(0.15,shape=[numCav])

wPhis=tf.Variable(tf.random_uniform(shape=[numCav],minval=-np.pi/2.,maxval=np.pi/2))

##############################################################################


gEmitTInput=EmitN2G3D(nEmitTInput,energyInMeV)


xH=tf.placeholder(tf.float32,[None,1])
xpH=tf.placeholder(tf.float32,[None,1])
yH=tf.placeholder(tf.float32,[None,1])
ypH=tf.placeholder(tf.float32,[None,1])
zH=tf.placeholder(tf.float32,[None,1])
zpH=tf.placeholder(tf.float32,[None,1])


def ETLHandle(ETLMV,countNumber=3):
    newETL=[]

    cutRatio=tf.constant([0.05])
    
    for iCav in range(numCav):

        
        if iCav<countNumber:
            meanLocal=tf.reduce_mean(ETLMV[0:iCav+countNumber])
        elif iCav>numCav-countNumber-1:
            meanLocal=tf.reduce_mean(ETLMV[iCav-countNumber::])
        else:
            meanLocal=tf.reduce_mean(ETLMV[iCav-countNumber:iCav+countNumber:])
        
        localETL=ETLMV[iCav]    
        
        ratioLocal=tf.abs(localETL-meanLocal)/(meanLocal+tf.constant([1.e-29]))
    
    
        
        newLocalETL= tf.cond(ratioLocal[0] > cutRatio[0], lambda: meanLocal, lambda: localETL)  
        
        newETL.append(newLocalETL)
        
    newETL=tf.abs(newETL)
        
    return newETL


         
            
wETLMV=ETLHandle(wETLMV,20)
wPhis=ETLHandle(wPhis,3)



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
loss4D_Lost=loss4D*tf.to_float(numPartLost)
lossZ=z**2+dBetaC**2

optiLoss=tf.train.AdamOptimizer(0.004)
trainX=optiLoss.minimize(lossZ)



partOut=[]
partOut.append(x)
partOut.append(xp)
partOut.append(y)
partOut.append(yp)
partOut.append(z)
partOut.append(betaC)
    

#________________________________________________________________________________________________________
init=tf.global_variables_initializer()

#sess=tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
sess=tf.Session()

sess.run(init)
print(sess.run(lenCellM))



for _ in range(10000):
    
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

    
    if _ % 10 ==0:

        partOutR=sess.run(partOut,feed_dict={xH:xIn,xpH:xpIn,yH:yIn,ypH:ypIn,zH:zIn,zpH:zpIn})
        
        
        xR=partOutR[0]
        xpR=partOutR[1]
        yR=partOutR[2]
        ypR=partOutR[3]
        zR=partOutR[4]
        betaCR=partOutR[5]
    
        plt.figure('Dis')
        plt.clf()
        plt.subplot(221)
        plt.plot(xR,xpR,'.')
        
        plt.subplot(222)
        plt.plot(yR,ypR,'.')
        
        plt.subplot(223)
        plt.plot(zR,betaCR,'.')
        

        plt.pause(0.1)
    
    










