#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 17:05:41 2017

@author: a
"""

import numpy as np
import matplotlib.pyplot  as plt

data062=np.loadtxt('082.txt')
z=data062[:,0]
Ez=data062[:,3]

plt.figure('Test Ez')
plt.plot(z,Ez)

EzAbs=np.abs(Ez)

plt.figure('Test absEz')
plt.plot(z,EzAbs)

deltaZ=z[1::]-z[0:-1:]
EzAve=(EzAbs[1::]+EzAbs[0:-1:])/2.
      
EzInteg=np.sum(deltaZ[0]*EzAve)
print(EzInteg)







