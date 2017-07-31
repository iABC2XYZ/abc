#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 10:23:06 2017

@author: a
"""

import numpy as np
import matplotlib.pyplot  as plt

plt.close('all')
dataRead=np.loadtxt('062.txt')
zRead=dataRead[:,0]
EzRead=dataRead[:,3]

betaC=0.62
frequencyRFMHz=650e6
lambdaMM=299792458./frequencyRFMHz
kWaveNum=2.*np.pi/(betaC*lambdaMM)
EzExp=EzRead*np.cos(kWaveNum*zRead+np.pi/2)

import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(zRead,EzExp,'b')
plt.hold
plt.plot(zRead,EzRead,'r')

Vacc=np.sum(EzExp)*(zRead[1]-zRead[0])
Eacc=Vacc/(zRead[-1])

print(Eacc)
print(np.max(abs(EzRead)))

