#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:19:19 2017

@author: p   正确  和MATLAB一样
"""

import numpy as np
from scipy.fftpack import dst, dct

'''
N=4
x=np.random.random([N,1])
#x=np.float32([1,2,3,4])[:,np.newaxis]/np.pi

def SinKM(N):
    k=np.linspace(1,N,N)
    m=k
    K,M=np.meshgrid(k,m)
    KM=K*M
    sinKM=np.sin(np.pi*KM/(N+1.))
    return sinKM

sinKM=SinKM(N)

xDst=np.matmul(sinKM,x)

xDstDst=2./(N+1)*np.matmul(sinKM,xDst)

#tf.placeholder(shpae=[N,1],)

print x.T
print '=========='
print sinKM
print "____________"
print xDst

print "____________"
print xDstDst
'''

"""

##
N=4
x=np.random.random([N,1])
#x=np.float32([1,2,3,4])[:,np.newaxis]/np.pi

def CosKU(N):
    k=np.linspace(0.5,N-0.5,N)
    u=np.linspace(0.,N-1.,N)
    K,U=np.meshgrid(k,u)
    KU=K*U
    cosKU=np.cos(np.pi*KU/N)
    return cosKU
cosKU=CosKU(N)
xDct=np.sqrt(2./N)*np.matmul(cosKU,x)
xDct[0]=xDct[0]/np.sqrt(2.)



print K
print U
print cosKM
print '_'*20
print x.T
print '_'*20
print xDct
"""


N=4
x=np.random.random([N,1])
#x=np.float32([1,2,3,4])[:,np.newaxis]/np.pi

def CosKM4(N):
    k=np.linspace(0.5,N-0.5,N)
    m=k
    K,M=np.meshgrid(k,m)
    KM=K*M
    cosKM=np.cos(np.pi*KM/N)
    return cosKM

cosKM=CosKM4(N)

xDct=np.matmul(cosKM,x)

xDctDct=2./N*np.matmul(cosKM,xDct)

#tf.placeholder(shpae=[N,1],)

print x.T
print '=========='
print cosKM
print "____________"
print xDct

print "____________"
print xDctDct





