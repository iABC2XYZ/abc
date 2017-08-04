#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:03:50 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    Emittance change between Norm and Geo~

"""
import tensorflow as tf
from BetaGammaC import Energy2BetaC_GammaC

def EmitN2G(emitN,energySyn,Axis='x'):
    betaSyn,gammaSyn=Energy2BetaC_GammaC(energySyn)
    if Axis.lower()=='z':
        emitG=emitN/(gammaSyn**3*betaSyn)
    else:
        emitG=emitN/(gammaSyn*betaSyn)
    return emitG


def EmitG2N(emitG,energySyn,Axis='x'):
    betaSyn,gammaSyn=Energy2BetaC_GammaC(energySyn)
    if Axis.lower()=='z':
        emitN=emitG*(gammaSyn**3*betaSyn)
    else:
        emitN=emitG*(gammaSyn*betaSyn)
    return emitN


def EmitG2N3D(emitG,energySyn):
    xEmitN=EmitG2N(energySyn,emitG[0],Axis='x')
    yEmitN=EmitG2N(energySyn,emitG[1],Axis='y')
    zEmitN=EmitG2N(energySyn,emitG[2],Axis='z')
    emitN=tf.concat([xEmitN,yEmitN,zEmitN],0)
    return emitN

def EmitN2G3D(emitN,energySyn):
    xEmitG=EmitN2G(energySyn,emitN[0],Axis='x')
    yEmitG=EmitN2G(energySyn,emitN[1],Axis='y')
    zEmitG=EmitN2G(energySyn,emitN[2],Axis='z')
    emitG=tf.concat([xEmitG,yEmitG,zEmitG],0)
    return emitG



