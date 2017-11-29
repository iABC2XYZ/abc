#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:46:45 2017

@author: p
"""


import numpy as np

import matplotlib.pyplot as plt

plt.close('all')

data=np.loadtxt('dataML')

x=np.array(range(np.shape(data)[1]))
plt.figure(1)
for i in xrange(np.shape(data)[0]):
    plt.plot(x,data[i,:],'.')
    plt.pause(1)
    x+=5




