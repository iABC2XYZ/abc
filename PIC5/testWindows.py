#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""

import matplotlib.pyplot as plt
import numpy as np


pSection=np.array([0,5,10,15])
sSection=pSection[0:-1]
eSection=pSection[1::]
N=len(sSection)

sWindows=np.array(0.5)
eWindows=np.array(1.7)
sBase=6

sWindows+=sBase
eWindows+=sBase

plt.close('all')
plt.figure(1)
plt.plot(sSection,eSection,'-*')

plt.figure(2)
plt.plot(sSection,np.ones(N),'b*')
plt.hold
plt.plot(np.array(eSection)+0.3,np.ones(N),'ro')
plt.axis([-1,18,0,2])

plt.plot(sWindows,1,'g^')
plt.plot(eWindows,1,'g^')






