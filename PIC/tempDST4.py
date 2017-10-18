# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:09:40 2017

@author: A
"""



import numpy as np
from scipy.fftpack import dst, dct


N=4
x=np.random.random([N,1])
#x=np.float32([1,2,3,4])[:,np.newaxis]/np.pi

def SinKM(N):
    k=np.linspace(1,N,N)
    m=k
    K,M=np.meshgrid(k,m)
    KM=K*M
    sinKM=np.sin(np.pi*KM/(N+1.))
    sinKM*=np.sqrt(2./(N+1))
    return sinKM

sinKM=SinKM(N)

xDst=np.matmul(sinKM,x)

xDstDst=np.matmul(sinKM,xDst)

#tf.placeholder(shpae=[N,1],)

print x.T
print '=========='
print sinKM
print "____________"
print xDst

print "____________"
print xDstDst

#_____________________________________________
print "++++++++++++++++++++++++++"

N=4
x=np.random.random([N,1])
#x=np.float32([1,2,3,4])[:,np.newaxis]/np.pi

def CosKM4(N):
    k=np.linspace(0.5,N-0.5,N)
    m=k
    K,M=np.meshgrid(k,m)
    KM=K*M
    cosKM=np.cos(np.pi*KM/N)
    cosKM*=np.sqrt(2./N)
    return cosKM

cosKM=CosKM4(N)

xDct=np.matmul(cosKM,x)

xDctDct=np.matmul(cosKM,xDct)

#tf.placeholder(shpae=[N,1],)

print x.T
print '=========='
print cosKM
print "____________"
print xDct

print "____________"
print xDctDct

print "#"*60


x=np.random.random([N,2])

cosKM=CosKM4(N)

xDct=np.matmul(cosKM,x)

xDctDct=np.matmul(cosKM,xDct)

print x
print '=========='
print cosKM
print "____________"
print xDct

print "____________"
print xDctDct












