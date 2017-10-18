# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:09:40 2017

@author: A
"""



import numpy as np
from scipy.fftpack import dst, dct

M=3
N=4
x=np.random.random([M,N])
#x=np.float32([1,2,3,4])[:,np.newaxis]/np.pi

print x

m=np.linspace(0.5,M-0.5,M)
n=np.linspace(0.5,N-0.5,N)

KN,KM=np.meshgrid(n,m)
MN=KN*KM

sinK=np.sqrt(2./M)*np.sin(np.pi*MN/M)
cosK=np.sqrt(2./N)*np.cos(np.pi*MN/N)

print "_"*40
print KM
print "_"*40
print sinK
print "_"*40
print cosK







y=np.random.random([N,M])

z=np.matmul(x,y).T
zT=np.matmul(y.T,x.T)

print "_"*40
print z
print "---"*40
print zT



"""
KM=K*M
sinKM=np.sqrt(2./N)*np.sin(np.pi*KM/N)
cosKM=np.sqrt(2./N)*np.cos(np.pi*KM/N)



def MN(M,N):
    m=np.linspace(0.5,M-0.5,M)
    n=np.linspace(0.5,N-0.5,N)
    
    KM,KN=np.meshgrid(k,m)
    KM=K*M
    sinKM=np.sqrt(2./N)*np.sin(np.pi*KM/N)
    cosKM=np.sqrt(2./N)*np.cos(np.pi*KM/N)
    return sinKM,cosKM

sinKM,cosKM=KM(N)

xDst=np.matmul(sinKM,x)
xDstDst=np.matmul(sinKM,xDst)

xDct=np.matmul(cosKM,x)
xDctDct=np.matmul(cosKM,xDct)


print x
print "-"*20
print xDst
print "-"*20
print xDstDst
print "-"*20

print xDct
print "-"*20
print xDctDct
print "-"*20

#_________________________________________________________

"""













