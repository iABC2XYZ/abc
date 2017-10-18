#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:19:48 2017

@author: e
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

plt.close('all')

def CosK(N):
    k=np.linspace(0.5,N-0.5,N)
    m=k
    K,M=np.meshgrid(k,m)
    KM=K*M
    cosKM=np.cos(np.pi*KM/N)
    cosKM*=np.sqrt(2./N)
    return cosKM

def SinK(N):
    k=np.linspace(0.5,N-0.5,N)
    m=k
    K,M=np.meshgrid(k,m)
    KM=K*M
    cosKM=np.sin(np.pi*KM/N)
    cosKM*=np.sqrt(2./N)
    return cosKM


def EigDirichlet(N,dx):
    K=np.linspace(1,N,N)[:,np.newaxis]
    Ek=-((2.*np.sin(np.pi*K/(2.*N)))/dx)**2
    return Ek

def EigNeumann(N,dx):
    K=np.linspace(0,N-1,N)[:,np.newaxis]
    Ek=-((2.*np.sin(np.pi*K/(2.*N)))/dx)**2
    return Ek

M=128
N=1
x=np.random.random([M,N])

SinKM=SinK(M)
xDst=np.matmul(SinKM,x)
xDstDst=np.matmul(SinKM,xDst)

CosKN=CosK(N)
xDct=np.matmul(CosKN,x.T).T
xDctDct=np.matmul(CosKN,xDct.T).T

print x
print "-"*20
print xDst
print "-"*20
print xDstDst

print "-"*20
print xDct
print "-"*20
print xDctDct


Kx=EigDirichlet(M,0.0123)
Ky=EigDirichlet(N,0.0123)

kxGrid,kyGrid=np.meshgrid(Ky,Kx)

kXYGrid=kxGrid+kyGrid


print "="*20
print Kx
print "-"*20
print Ky
print "-"*20
print kxGrid
print "-"*20
print kyGrid
print "-"*20
print kXYGrid

xDst=np.matmul(SinKM,x)
xDstDct=np.matmul(CosKN,xDst.T).T

yDstDct=xDstDct/kXYGrid
yDst=np.matmul(CosKN,yDstDct.T).T
y=np.matmul(SinKM,yDst)

#kxGrid,kyGrid=np.meshgrid(Ky,Kx)

fig3=plt.figure(10)
ax = fig3.gca(projection='3d')

xPlot,yPlot=np.linspace(0,M-1,M),np.linspace(0,N-1,N)
yPlot3D, xPlot3D=np.meshgrid(yPlot,xPlot)
surf = ax.plot_surface(xPlot3D,yPlot3D,y, cmap=cm.coolwarm,linewidth=0, antialiased=False)

#____________________________


sinKN=SinK(N)

xDst=np.matmul(SinKM,x)
xDstDst=np.matmul(sinKN,xDst.T).T

yDstDst=xDstDst/kXYGrid
yDst=np.matmul(sinKN,yDstDst.T).T
y=np.matmul(SinKM,yDst)

#kxGrid,kyGrid=np.meshgrid(Ky,Kx)

fig3=plt.figure(20)
ax = fig3.gca(projection='3d')

xPlot,yPlot=np.linspace(0,M-1,M),np.linspace(0,N-1,N)
yPlot3D, xPlot3D=np.meshgrid(yPlot,xPlot)
surf = ax.plot_surface(xPlot3D,yPlot3D,y, cmap=cm.coolwarm,linewidth=0, antialiased=False)



fig3=plt.figure(21)
plt.plot(x)
fig3=plt.figure(22)
plt.plot(y)





