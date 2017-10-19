#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:29:10 2017

@author: e
"""

import Input2Sys
import matplotlib.pyplot as plt

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
plt.plot(y,py,'r.')
plt.xlabel('y / m')
plt.ylabel('py (betaGamma)')

plt.figure(3)
plt.subplot(121)
plt.plot(z,zp,'.')
plt.xlabel('z / m')
plt.ylabel('zp / rad')
plt.subplot(122)
plt.plot(z,pz,'r.')
plt.xlabel('z / m')
plt.ylabel('pz (betaGamma)')



