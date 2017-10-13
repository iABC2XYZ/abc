#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:47:44 2017

@author: A
"""

from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt


fs=256
N=256
n=np.linspace(0,N-1,N)
t=n/fs

s=2+3*np.cos(2*np.pi*50.*t-np.pi*30./180.)+1.5*np.cos(2*np.pi*75.*t+np.pi*90./180.)

plt.close('all')

plt.figure(1)
plt.clf()
plt.plot(t,s,'.')


y=fft(s,N)

mag=np.abs(y)

f=n*fs/N

plt.figure(2)
plt.clf()
plt.plot(f,mag)


plt.figure(3)
plt.plot(f,np.angle(y))



def Findpeaks(x):
    xFindpeaks=np.zeros(len(x)/2,dtype=np.int)
    ix=0
    for nX in xrange(len(x)):
        if nX==0:
            if x[0]>=x[1]:
                xFindpeaks[ix]=nX
                ix+=1
        elif nX==len(x)-1:
            if x[-1]>=x[-2]:
                xFindpeaks[ix]=nX
                ix+=1
        elif x[nX]>x[nX-1]+1e-6 and x[nX] >x[nX+1]+1e-6:
            xFindpeaks[ix]=nX
            ix+=1
        else:
            continue
                
    return xFindpeaks[0:ix]

bb=Findpeaks(mag)


plt.figure(20)
plt.clf()
plt.plot(f,mag)
plt.hold
plt.plot(f[bb],mag[bb],'ro')


A=mag/(N/2.)
A[0]/=2.

A=mag/N

plt.figure(10)
plt.clf()
plt.plot(f,A)


Angle=np.angle(y)
plt.figure(11)
plt.clf()
plt.plot(f,Angle/np.pi*180)
plt.hold
plt.plot(f[bb],Angle[bb]/np.pi*180)
plt.grid('on')


x0=np.zeros(N)
for iX in xrange(N):
    x0+=A[iX]*np.cos(2*np.pi*f[iX]*t+Angle[iX])
    

plt.figure(100)
plt.clf()
plt.plot(t,x0,'.')




def ReconstructionFFT(s):
    from scipy.fftpack import fft
    fs=1
    N=len(s)
    n=np.range(N)
    f=n*fs/N
    
    sFFT=fft(s,N)
    magSFFT=np.abs(sFFT)
    ASFFT=magSFFT/N
    angleSFFT=np.angle(sTTF)
    
    s0=np.zeros(N)
    for iS in xrange(N):
        s0+=ASFFT[iS]*np.cos(2*np.pi*f[iS]*t+angleSFFT[iS])
    return s0










