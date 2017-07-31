# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

plt.close('all')

x=np.log10([0.003,30])
y=np.log10([0.03,20])


k=(y[1]-y[0])/(x[1]-x[0])
b=y[0]-k*x[0]

xList=np.linspace(x[0],x[1],1000)
yList=k*xList+b


plt.figure(1)
plt.plot(xList,yList)

plt.figure(2)
plt.loglog(xList,yList)
