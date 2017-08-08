#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 20:40:03 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    Action Function
______________________________________________________


"""
import tensorflow as tf
from MinMax import *
from InputBeam import numPart


def MyAct(x,xp,y,yp,z,betaC):
    xTrue=tf.abs(x)<xMax
    xpTrue=tf.abs(xp)<xpMax
    yTrue=tf.abs(y)<yMax
    ypTrue=tf.abs(yp)<ypMax
    
    zTure=tf.abs(z)<zMax
    betaCTrue_Min=betaC>betaCMin
    betaCTrue_Max=betaC<betaCMax
    
    x_True=tf.logical_and(xTrue,xpTrue)
    y_True=tf.logical_and(yTrue,ypTrue)
    xy_True=tf.logical_and(x_True,y_True)
    
    beta_True=tf.logical_and(betaCTrue_Min,betaCTrue_Max)
    z_True=tf.logical_and(zTure,beta_True)
    
    flagTure=tf.logical_and(xy_True,z_True)
    
    x=tf.boolean_mask(x,flagTure)
    xp=tf.boolean_mask(xp,flagTure)
    y=tf.boolean_mask(y,flagTure)
    yp=tf.boolean_mask(yp,flagTure)
    z=tf.boolean_mask(z,flagTure)
    betaC=tf.boolean_mask(betaC,flagTure)
    
    xShape=tf.shape(x)
    numPartRemain=xShape[0]
    nunPartLost=numPart-numPartRemain
    
    return x,xp,y,yp,z,betaC,nunPartLost









'''
from Constants import pi

def Action_Min_Max(x,Min,Max):
    X=tf.maximum(tf.minimum(x,Max),Min)
    return X

def MyAct(x,xp,y,yp,phi,energy):
    x=Action_Min_Max(x,xMin,xMax)
    xp=Action_Min_Max(xp,xpMin,xpMax)
    y=Action_Min_Max(y,yMin,yMax)
    yp=Action_Min_Max(yp,ypMin,ypMax)
    phi=Action_Min_Max(phi,phiMin,phiMax)
    energy=Action_Min_Max(energy,energyMin,energyMax)
    return x,xp,y,yp,phi,energy


def MyZoomIn(x,xp,y,yp,phi,energy):
    x/=(xMax-xMin)
    xp/=(xpMax-xpMin)
    y/=(yMax-yMin)
    yp/=(ypMax-ypMin)
    
    phi/=phiMax
    energy/=energyMax
    return x,xp,y,yp,phi,energy

def MyZoomOut(x,xp,y,yp,phi,energy):
    x*=(xMax-xMin)
    xp*=(xpMax-xpMin)
    y*=(yMax-yMin)
    yp*=(ypMax-ypMin)
    
    phi*=phiMax
    energy*=energyMax
    return x,xp,y,yp,phi,energy

'''


