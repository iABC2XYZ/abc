#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 21:25:01 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
______________________________________________________


"""

import tensorflow as tf

def TwissInputLayer():
    pass
'''
def TwissOutputLayer(x,xp,y,yp,z,zp):
    wAlphaT=tf.Variable(tf.random_normal([3]))
    wBetaT=tf.Variable(tf.zeros([3])+0.1)
    
    wGammaT=tf.div((1.+tf.square(wAlphaT)),wBetaT)
    
    emitX2=tf.abs(wGammaT[0]*x**2+2.*wAlphaT[0]*x*xp+wBetaT[0]*xp**2)
    #emitY2=wGammaT[1]*y**2+2.*wAlphaT[1]*y*yp+wBetaT[1]*yp**2
    #emitZ2=wGammaT[2]*z**2+2.*wAlphaT[2]*z*zp+wBetaT[2]*zp**2
    
    #emitT2=emitX2*emitY2*emitZ2
    return emitX2,wAlphaT,wBetaT
'''
def TwissOutputLayer(x,xp,y,yp,z,zp):
    wAlphaT=tf.Variable(tf.random_normal([3]))
    wBetaT=tf.Variable(tf.zeros([3])+0.1)
    
    wGammaT=tf.div((1.+tf.square(wAlphaT)),wBetaT)
    
    #emitX2=tf.abs(tf.multiply(wGammaT[0],tf.square(x))+2.*tf.multiply(wAlphaT[0],tf.multiply(x,xp))+tf.multiply(wBetaT[0],tf.square(xp)))
    emitX2_0=tf.abs(wGammaT[0]*x[0]**2+2.*wAlphaT[0]*x[0]*xp[0]+wBetaT[0]*xp[0]**2)
    emitX2_1=tf.abs(wGammaT[0]*x[1]**2+2.*wAlphaT[0]*x[1]*xp[1]+wBetaT[0]*xp[1]**2)
    
    emitXN=emitX2_0*emitX2_1
    #emitY2=wGammaT[1]*y**2+2.*wAlphaT[1]*y*yp+wBetaT[1]*yp**2
    #emitZ2=wGammaT[2]*z**2+2.*wAlphaT[2]*z*zp+wBetaT[2]*zp**2
    
    #emitT2=emitX2*emitY2*emitZ2
    return emitX2_0,wAlphaT,wBetaT



def APFLayer():
    pass








