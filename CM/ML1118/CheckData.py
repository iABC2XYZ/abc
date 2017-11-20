#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 18:08:57 2017

@author: p
"""

import numpy as np
import matplotlib.pyplot as plt

fName='data1~2000'
data=np.loadtxt(fName)

print np.shape(data)


bpmData=data[:,0:12]
dcData=data[:,80:94]
q1Data=data[:,140:143]
q2Data=data[:,144:147]
psData=np.hstack((dcData,q1Data,q2Data))

print np.shape(bpmData),np.shape(psData),np.shape(q2Data)
plt.close(plt.figure(1))
numBPM=np.shape(bpmData)[1]
for iBPM in range(numBPM):
    
    plt.figure(1)
    plt.clf()
    plt.hist(bpmData[:,iBPM],100)
    plt.title(iBPM)
    plt.pause(2)



numPS=np.shape(psData)[1]
plt.close(plt.figure(2))
for iPS in range(numPS):
    plt.figure(2)
    plt.clf()
    plt.hist(psData[:,iPS],100)
    plt.title(iPS)
    plt.pause(2)
    








