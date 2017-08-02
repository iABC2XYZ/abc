#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 17:52:19 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
______________________________________________________


"""
from  numpy.random import multivariate_normal as npmvn
from numpy import diag


def PartGen(emitT,numPart):
    meanPart=[0.,0.,0.,0.,0.,0.]
    covPart=diag([emitT[0],emitT[0],emitT[1],emitT[1],emitT[2],emitT[2]])
    
    x,xp,y,yp,z,zp=npmvn(meanPart,covPart,numPart).T
    return  x,xp,y,yp,z,zp








