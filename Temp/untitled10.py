#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:42:03 2017

@author: A
"""


from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt

fs=100
N=128
n=np.linspace(0,N-1,N)
t=n/fs

x=0.5*np.sin(2*np.pi*15.*t)+2*np.cos(2*np.pi*40.*t)

plt.close('all')

plt.figure(1)
plt.clf()
plt.plot(t,x,'.')


y=fft(x,N)

mag=np.abs(y)

'''
plt.figure(2)
plt.clf()
plt.plot(mag)
'''

f=n*fs/N

'''
plt.figure(3)
plt.clf()
plt.plot(f,mag)
'''

print len(f), len(mag),len(n)




import scipy.signal as signal
peakind = signal.find_peaks_cwt(mag, np.arange(0.1,0.2))

plt.figure(30)
plt.clf()
plt.hold('on')
plt.plot(f,mag)
plt.plot(f[peakind],mag[peakind],'ro')

print '**********************'
#print mag[peakind[0]]/(N/2.), mag[peakind[1]]/(N/2.),np.arctan2(y[peakind[0]].imag,y[peakind[0]].real) ,np.arctan2(y[peakind[1]].imag,y[peakind[1]].real) 
print mag[peakind[0]]/(N/2.), mag[peakind[1]]/(N/2.),np.angle(y[peakind[0]]),np.angle(y[peakind[1]])


plt.figure(4)
plt.plot(f,np.angle(y))
plt.hold('on')
plt.plot(f[peakind],np.angle(y[peakind]),'r.')



x0=np.zeros(N)
for i in xrange(N):
    x0+=mag[i]*np.sin(2*np.pi*f[i]*t-np.angle(y))/(N/2.)

    
plt.figure('x0')
plt.plot(t,x0,'.')












