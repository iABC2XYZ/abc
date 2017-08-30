#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:18:39 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:


"""


import numpy as np

def PartGen(numPart):
    x=np.random.randn(numPart)
    xp=np.random.randn(numPart)
    y=np.random.randn(numPart)
    yp=np.random.randn(numPart)
    z=np.random.randn(numPart)
    zp=np.random.randn(numPart)
    
    x=x[:,np.newaxis]
    xp=xp[:,np.newaxis]
    y=y[:,np.newaxis]
    yp=yp[:,np.newaxis]
    z=z[:,np.newaxis]
    zp=zp[:,np.newaxis]
    
    
    return x,xp,y,yp,z,zp



















