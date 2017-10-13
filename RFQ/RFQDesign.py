#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 11:52:20 2017

@author: Peiyong Jiang jiangpeiyong@impcas.ac.cn
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

V=4
L=10
A10=3
numZ=100
z=np.linspace(0,L,numZ)
Ez0=np.pi*A10*V/(2.*L)*np.sin(np.pi/L*z)

plt.figure('Ez0')
plt.plot(z,Ez0)


tf.r

''''
global q, m
q=1
m=1

def RFQcell(V,r0,A10,m,L,ThetaS,Type,Rho,A01):
    global q, m
    Ez=np.pi*A10*V/(2.*L)*sin(np.pi/L*z)*sin(omega*t)


print("a")
'''



