# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf
import numpy as np

global cLight
cLight=299792458.


def Energy2GammaC(energyMeV,massMeV=938.274):
    return 1.+tf.div(energyMeV,massMeV)
    
def GammaC2BetaC(gammaC):
    return tf.sqrt(1.-tf.div(1.,tf.square(gammaC)))

def BetaC2GammaC(betaC):
    return tf.div(1.,tf.sqrt(1.-tf.square(betaC)))

def GammaC2Energy(gammaC,massMeV=938.274):
    return (gammaC-1.)*massMeV

def Enerty2BetaC(energyMeV,massMeV=938.274):
    return GammaC2BetaC(Energy2GammaC(energyMeV,massMeV))

def BetaC2Energy(betaC,massMeV=938.274):
    return GammaC2Energy(BetaC2GammaC(betaC),massMeV)
    
def GenCellLen5Phis(phi1S,phi2S,betaC,frequencyMHz):
    global cLight
    return (phi2S-phi1S+np.pi)/(2.0*np.pi)*betaC*(cLight/frequencyMHz)


 
'''
def GenGammaT5Twiss(alphaT,betaT):
    return tf.div((1.+tf.square(alphaT)),betaT)

def GenParticles5Twiss(emitT,alphaT,betaT):
    gammaT=GenGammaT5Twiss(alphaT,betaT)
    #covT=tf.constant([[betaT,-alphaT],[-alphaT,gammaT]])
    #covT=tf.constant([[1,gammaT],[gammaT,4]])

    
    

    return covT
'''

'''
def GenGammaT5Twiss(alphaT,betaT):
    return (1.+alphaT**2)/betaT

def GenNormalParticles(numPart):
    x=tf.random_normal(shape=[numPart,2],mean=0.0,stddev=1.0)
    return x


def GenParticles5Twiss(emitT,alphaT,betaT):
    gammaT=GenGammaT5Twiss(alphaT,betaT)
    covT=emitT*np.array([[betaT,-alphaT],[-alphaT,gammaT]])
    eCov,vCov=np.linalg.eig(covT)
    

    return  eCov,vCov
'''
    
def layerTwiss(energyIn,emitX,emitY,emitZ, numPart):
    Weights=tf.Variable(tf.eye(6))
    return Weights

    
    


energyIn=tf.constant([10.])
emitX=tf.constant([3.])
emitY=tf.constant([4.])
emitZ=tf.constant([5.])
numPart=tf.constant([10])

with tf.Session() as sessTest:
    print sessTest.run(layerTwiss(energyIn,emitX,emitY,emitZ, numPart))
    
    
    
    
sess = tf.InteractiveSession()
x = tf.random_normal(shape=[1,5],mean=0.0,stddev=1.0,dtype=tf.float32,seed=None,name=None)
print(sess.run(x))
    
    
    
    