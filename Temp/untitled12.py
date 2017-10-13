#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 15:29:59 2017

@author: A
"""

from scipy import signal
xs = np.arange(0, np.pi*5, 0.05)
data = np.sin(xs)
peakind = signal.find_peaks_cwt(data, np.arange(1,100))
print peakind, xs[peakind], data[peakind]

plt.close('all')
plt.figure('T')
plt.clf()
plt.hold('on')
plt.plot(xs,data)
plt.plot(xs[peakind],data[peakind],'ro')



