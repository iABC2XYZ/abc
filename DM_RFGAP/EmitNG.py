#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 12:30:42 2017

@author: A
"""
import tensorflow as tf
from BetaGammaC import *


def EmitN2G(constEnergyInMeV,constEmitN,axis='x'):
    constGammaIn=Energy2GammaC(constEnergyInMeV)
    constBetaIn=Energy2BetaC(constEnergyInMeV)
    if axis=='z' :
        constEmitG=constEmitN/(constGammaIn**3*constBetaIn)
    else:
        constEmitG=constEmitN/(constGammaIn*constBetaIn)
    return constEmitG

def EmitG2N(constEnergyInMeV,constEmitG,axis='x'):
    constGammaIn=Energy2GammaC(constEnergyInMeV)
    constBetaIn=Energy2BetaC(constEnergyInMeV)
    if axis=='z' :
        constEmitN=constEmitG*(constGammaIn**3*constBetaIn)
    else:
        constEmitN=constEmitG*(constGammaIn*constBetaIn)

    return constEmitN




def Emit3DG2N(constEnergyInMeV,constEmitG):
    xEmitN=EmitG2N(constEnergyInMeV,constEmitG[0],axis='x')
    yEmitN=EmitG2N(constEnergyInMeV,constEmitG[1],axis='y')
    zEmitN=EmitG2N(constEnergyInMeV,constEmitG[2],axis='z')
    constEmitN=tf.concat([xEmitN,yEmitN,zEmitN],0)
    return constEmitN

def Emit3DN2G(constEnergyInMeV,constEmitN):
    xEmitG=EmitN2G(constEnergyInMeV,constEmitN[0],axis='x')
    yEmitG=EmitN2G(constEnergyInMeV,constEmitN[1],axis='y')
    zEmitG=EmitN2G(constEnergyInMeV,constEmitN[2],axis='z')
    constEmitG=tf.concat([xEmitG,yEmitG,zEmitG],0)
    return constEmitG



