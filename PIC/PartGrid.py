#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 17:10:11 2017

@author: e
"""

import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


from Input2Sys import x,y,z,xGridLog,yGridLog,zGridLog



plt.close('all')
fig=plt.figure(1)
ax = fig.gca(projection='3d')
ax.scatter(x,y,z)
ax.view_init(elev=90., azim=0)



if bunchFlag==True:   #3D   SSP
    
    
    
    pass

if bunchFlag==False:   #2D   SS
    
    
    
    pass
    
    




'''
plt.figure(11)
plt.plot(x,'.')
plt.figure(12)
plt.plot(y,'.')
plt.figure(13)
plt.plot(z,'.')


plt.figure(21)
plt.scatter(y,z)
'''














