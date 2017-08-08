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




