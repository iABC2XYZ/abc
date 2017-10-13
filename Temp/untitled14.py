#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 17:39:17 2017

@author: A
"""

import numpy as np
import matplotlib.pyplot as plt

def ReconstructionFFT(s):
    from scipy.fftpack import fft
    fs=1
    N=len(s)
    #fs=N
    n=np.linspace(0,N-1,N)
    f=n*fs/N
    t=n/fs

    
    sFFT=fft(s,N)
    magSFFT=np.abs(sFFT)
    ASFFT=magSFFT/N
    angleSFFT=np.angle(sFFT)
    
    s0=np.zeros(N)
    for iS in xrange(N):
        s0+=ASFFT[iS]*np.cos(2*np.pi*f[iS]*t+angleSFFT[iS])
    return s0

def  ReconstructionANDPrediction(dataOrigin,lenPredict):
    from scipy.fftpack import fft
    fs=1
    N=len(dataOrigin)
    n=np.linspace(0,N-1+lenPredict,N+lenPredict)
    f=n*fs/N
    t=n/fs

    
    sFFT=fft(dataOrigin,N)
    magSFFT=np.abs(sFFT)
    ASFFT=magSFFT/N
    angleSFFT=np.angle(sFFT)
    
    s0=np.zeros(N+lenPredict)
    for iS in xrange(N):
        s0+=ASFFT[iS]*np.cos(2*np.pi*f[iS]*t+angleSFFT[iS])
    return s0


def  ReconstructionANDPredictionNew(dataOrigin,lenPredict):
    from scipy.fftpack import fft
    fs=1
    N=len(dataOrigin)+lenPredict
    n=np.linspace(0,N-1,N)
    f=n*fs/N
    t=n/fs

    
    sFFT=fft(dataOrigin,N)
    magSFFT=np.abs(sFFT)
    ASFFT=magSFFT/N
    angleSFFT=np.angle(sFFT)
    
    s0=np.zeros(N/2)
    for iS in xrange(N):
        s0+=ASFFT[iS]*np.cos(2*np.pi*f[iS]*t+angleSFFT[iS])
    return 2*s0



x=np.random.rand(1024)

fs=1024
N=1024
n=np.linspace(0,N-1,N)
t=n/fs

x=2+3*np.cos(2*np.pi*50.*t+np.pi*30./180.)+1.5*np.cos(2*np.pi*175.*t+np.pi*70./180.)




plt.close('all')
plt.figure('R')
plt.plot(x,'.')

x0=ReconstructionFFT(x)

plt.figure('R2')
plt.plot(x,'b.')
plt.plot(x0,'.r')


xPredict= ReconstructionANDPrediction(x,1024)

plt.figure('Predict')
plt.plot(np.arange(1024),x,'b*')
plt.plot(np.arange(1024,2048,1),x,'b*')

plt.plot(xPredict,'ro')







