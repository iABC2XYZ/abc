#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 16:16:53 2017

@author: p
"""


import numpy as np

nameFile='RecScan_1031_1609.dat'
exData=np.loadtxt(nameFile)

[mEx,nEx]=np.shape(exData)

nStep=mEx/14.

dI=30./(nStep-1.)

matRes=np.zeros([14,10])
y=np.linspace(-15,15,np.int32(nStep))
for i in xrange(14):
    nStart,nFinish=np.int32(i*nStep),np.int32((i+1)*nStep)
    for iBpm in xrange(14,24):
        x=exData[nStart:nFinish,iBpm]-exData[np.int32(nStart+nFinish+1)/2,iBpm]
        polyFit = np.polyfit(x, y, 1)
        if np.abs(polyFit[0])>=8:
            matRes[i,iBpm-14] = 0.
        else:
            matRes[i,iBpm-14] = polyFit[0]
        

xBpm=np.zeros((5,1))
yBpm=np.zeros((5,1))
            
for iBPM in range(5):
    nameXBPM='BPM:'+str(iBPM+1)+'-X11'
    nameYBPM='BPM:'+str(iBPM+1)+'-Y11'

    #xBpm[iBPM]=caget(nameXBPM)
    #yBpm[iBPM]=caget(nameYBPM)

    xBpm[iBPM]=np.random.random()
    yBpm[iBPM]=np.random.random()


flagBPM1=1

if flagBPM1==1:
    xBpm[0]=0.
    yBpm[0]=0.

xyBPM=-np.vstack((xBpm,yBpm))


    


iSet=np.matmul(matRes,xyBPM)

iSet=(iSet*100.)/100.

print iSet


for iQ in range(14):        
    if iQ<7:
        name='MEBT_PS:DCH_0'+str(iQ+1)+':ISet'
    else:
        name='MEBT_PS:DCV_0'+str(iQ+1-7)+':ISet'
    #caput(name,iSet[0,iQ])













