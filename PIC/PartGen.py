#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:01:24 2017

@author: e
"""

import matplotlib.pyplot as plt

from Input2Sys import *
from BetaGammaC import NP_Energy2BetaGammaC


muT=muT6D
sigmaT=sigmaT6D

x,xp,y,yp,z,zp=np.random.multivariate_normal(muT6D,sigmaT6D,numPart).T

x/=1000.  #m
y/=1000.  #m
z/=1000.  #m
xp/=1000. #rad
yp/=1000. #rad
zp/=1000. #rad

p0=NP_Energy2BetaGammaC(energyMeV)
pz=p0*(1.+zp)
px=xp/pz
py=yp/pz


'''
plt.close('all')
plt.figure(1)
plt.subplot(121)
plt.plot(x,xp,'.')
plt.xlabel('x / m')
plt.ylabel('xp / rad')
plt.subplot(122)
plt.plot(x,px,'r.')
plt.xlabel('x / m')
plt.ylabel('px (betaGamma)')

plt.figure(2)
plt.subplot(121)
plt.plot(y,yp,'.')
plt.xlabel('y / m')
plt.ylabel('yp / rad')
plt.subplot(122)
plt.plot(x,px,'r.')
plt.xlabel('y / m')
plt.ylabel('py (betaGamma)')

plt.figure(3)
plt.subplot(121)
plt.plot(y,yp,'.')
plt.xlabel('z / m')
plt.ylabel('zp / rad')
plt.subplot(122)
plt.plot(x,px,'r.')
plt.xlabel('z / m')
plt.ylabel('pz (betaGamma)')
'''













