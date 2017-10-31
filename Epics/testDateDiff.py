#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:37:20 2017

@author: p
"""

import numpy as np

import matplotlib.pyplot as plt


plt.close('all')

exData=np.loadtxt('/home/p/ABC/abc/Epics/Rec.dat')

for i in xrange(14):
    plt.figure(i)
    plt.subplot(1,2,1)
    plt.plot(exData[:,i],'.')
    plt.subplot(1,2,2)
    plt.hist(exData[:,i],100)

plt.close('all')
for i in xrange(14,25):
    plt.figure(i)
    plt.subplot(1,2,1)
    plt.plot(exData[:,i],'.')
    plt.subplot(1,2,2)
    plt.hist(exData[:,i],100)


plt.close('all')

I=exData[:,-1]















