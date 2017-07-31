#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:56:22 2017

@author: a
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

plt.close('all')

xkW=[0.002,30]
yCost=[0.022,20]

pkWCost=np.polyfit(np.log10(xkW),np.log10(yCost),1)
numPoint=10000
xkWArray=np.linspace(xkW[0],xkW[-1],numPoint)
yCostArray=10**np.polyval(pkWCost,np.log10(xkWArray))

plt.figure('kW-Cost')
plt.loglog(xkWArray,yCostArray)
plt.grid(1)
plt.axis([0.0001,100,0.01,100])

print(yCostArray[np.argmin(np.abs(xkWArray-10))])
