#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:19:01 2017

@author: p
"""

import matplotlib.pyplot as plt
import numpy as np


plt.close('all')

cHV=np.round(np.random.random((14))*300-150)/10.
cHV_BK=cHV


plt.figure('cHV')
plt.plot(cHV,'-r')

flagHV=np.ones((14))

Amp=3.5
nFresh=30
for iTotal in xrange(200):
    
    if iTotal==0:
        cHV=np.round(np.random.random((14))*300-150)/10.
        flagHV=np.ones((14))*np.sign(np.random.random((14))-0.5)
    else:
        if iTotal % np.round(nFresh/4)==nFresh/8:
            flagHV=np.ones((14))*np.sign(np.random.random((14))-0.5)
        
        cHV+=(np.random.random((14)))*Amp*flagHV
        flagHV[cHV>15]=-1
        flagHV[cHV<-15]=1
        cHV[cHV>15]=30-cHV[cHV>15]
        cHV[cHV<-15]=-30-cHV[cHV<-15]
    
    


    flagHV[cHV>15]=-1
    flagHV[cHV<-15]=1
    cHV[cHV>15]=30-cHV[cHV>15]
    cHV[cHV<-15]=-30-cHV[cHV<-15]


    plt.figure('cHV_update')
    plt.clf()
    #plt.hold
    plt.plot(cHV_BK,'-r')
    plt.plot(cHV,'-b')
    
    plt.pause(0.1)
    

plt.plot(cHV_BK,'-r')

