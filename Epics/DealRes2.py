#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 16:16:53 2017

@author: p
"""


import numpy as np
import matplotlib.pyplot as plt

nameFile='RecScan_1031_1609.dat'
exData=np.loadtxt(nameFile)

[mEx,nEx]=np.shape(exData)

nStep=mEx/14.

dI=30./(nStep-1.)

matRes=np.zeros([14,10])
x=np.linspace(-15,15,np.int32(nStep))
for i in xrange(14):
    nStart,nFinish=np.int32(i*nStep),np.int32((i+1)*nStep)
    for iBpm in xrange(14,24):
        y=exData[nStart:nFinish,iBpm]-exData[np.int32(nStart+nFinish+1)/2,iBpm]
        plt.figure(1)
        plt.clf()
        plt.plot(x,y,'.')
        plt.title((str(i+1)+' '+str(iBpm-13)))
        plt.pause(1)

        











