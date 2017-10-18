# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:17:47 2017

@author: A
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

plt.close('all')

numPart=np.int64(1e5)

xGridLog,yGridLog,zGridLog=4,4,6
xGrid,yGrid,zGrid=2**xGridLog,2**yGridLog,2**zGridLog

xMin=-14.
xMax=14.
yMin=-18.
yMax=18.

xyMean=np.array([0.,0.,0.,0.])

xEmit,yEmit=2.,2.
xBeta,yBeta=3.,3.
xAlpha,yAlpha=1.,1.

def GammaT(alphaT,betaT):
    gammaT=(1.+alphaT**2)/betaT
    return gammaT

def SigmaT(alphaT,betaT):
    gammaT=GammaT(alphaT,betaT)
    sigmaT=np.array([[betaT,-alphaT],[-alphaT,gammaT]])
    return sigmaT
    
xSigmaT,ySigmaT= SigmaT(xAlpha,xBeta), SigmaT(yAlpha,yBeta)
O2=np.zeros((2,2))

xySigmaT=np.append(np.append(xSigmaT,O2,axis=0),np.append(O2,ySigmaT,axis=0),axis=1)


x,xp,y,yp=np.random.multivariate_normal(xyMean,xySigmaT,numPart).T

'''
plt.figure(1)
plt.plot(x,xp,'.')

plt.figure(2)
plt.plot(y,yp,'.')
'''

'''
dX=(xMax-xMin)/(xGrid-1.)
dY=(yMax-yMin)/(yGrid-1.)

partFlag=(x>=xMin) * (y>=yMin) * (x<xMax) * (y<yMax) 
xUse=x[partFlag]
xpUse=xp[partFlag]
yUse=y[partFlag]
ypUse=yp[partFlag]

def InfXY(x,xMin,dX):

    infX=(x-xMin)/dX
    intX=np.floor(infX)
    fracX=infX-intX
    return intX,fracX

intX,fracX=InfXY(xUse,xMin,dX)
intY,fracY=InfXY(yUse,yMin,dY)

partGrid=np.zeros((xGrid,yGrid))
for iPart in range(len(intX)):
    partGrid[intX,int

'''

rhoGrid,xArray,yArray=np.histogram2d(x,y,bins=(xGrid,yGrid),range=[[xMin,xMax],[yMin,yMax]])
dx=xArray[1]-xArray[0]
dy=yArray[1]-yArray[0]

rhoGrid/=(dx*dy)

xMid=(xArray[0:-1:]+xArray[1::])/2.
yMid=(yArray[0:-1:]+yArray[1::])/2.

yMidGrid,xMidGrid=np.meshgrid(yMid,xMid)

fig3=plt.figure(3)
ax = fig3.gca(projection='3d')
surf = ax.plot_surface(xMidGrid,yMidGrid,rhoGrid, cmap=cm.coolwarm,linewidth=0, antialiased=False)

plt.figure(4)
plt.plot(x,y,'.')

plt.show()




def SinK(N):
    k=np.linspace(1,N,N)
    m=k
    K,M=np.meshgrid(k,m)
    KM=K*M
    sinKM=np.sin(np.pi*KM/(N+1))
    sinKM*=np.sqrt(2./N)
    return sinKM




def EigDirichlet(N,dx):
    K=np.linspace(1,N,N)[:,np.newaxis]
    Ek=-((2.*np.sin(np.pi*K/(2.*(N+1))))/dx)**2
    return Ek


def ExpK(N):
    k=np.linspace(0,N-1,N)
    m=k
    K,M=np.meshgrid(k,m)
    KM=K*M
    
    cosKM=np.cos(2.*np.pi*KM/N)
    sinKM=np.sin(2.*np.pi*KM/N)
    
    cosKM/=np.sqrt(N)
    sinKM/=np.sqrt(N)
    return cosKM,sinKM

def EigPeriodic(N,dx):
    K=np.linspace(0,N-1,N)[:,np.newaxis]
    Ek=-((2.*np.sin(np.pi*K/N))/dx)**2
    return Ek


sinKX=SinK(xGrid)
sinKY=SinK(yGrid)

Kx=EigDirichlet(xGrid,dx)
Ky=EigDirichlet(yGrid,dy)

kxGrid,kyGrid=np.meshgrid(Ky,Kx)

kXYGrid=kxGrid+kyGrid


rhoDst=np.matmul(sinKX,rhoGrid)
rhoDstDst=np.matmul(sinKY,rhoDst.T).T

uDstDst=rhoDstDst/kXYGrid

uDst=np.matmul(sinKY,uDstDst.T).T
u=np.matmul(sinKX,uDst)

u22=np.gradient(np.gradient(u,axis=0),axis=0)+np.gradient(np.gradient(u,axis=1),axis=1)
u22/=(dx*dy)

fig3=plt.figure(20)
ax = fig3.gca(projection='3d')
surf = ax.plot_surface(xMidGrid,yMidGrid,u, cmap=cm.coolwarm,linewidth=0, antialiased=False)

fig3=plt.figure(31)
ax = fig3.gca(projection='3d')
surf = ax.plot_surface(xMidGrid,yMidGrid,u22, cmap=cm.coolwarm,linewidth=0, antialiased=False)

print np.sum(u22),np.sum(rhoGrid),(np.sum(u22)-np.sum(rhoGrid))/np.sum(rhoGrid)

#_______________________________________________________________________________




sinKX=SinK(xGrid)
cosKY,sinKY=ExpK(yGrid)

Kx=EigDirichlet(xGrid,dx)
Ky=EigPeriodic(yGrid,dy)

kxGrid,kyGrid=np.meshgrid(Ky,Kx)

kXYGrid=kxGrid+kyGrid


rhoDst=np.matmul(sinKX,rhoGrid)

rhoDstC=np.matmul(cosKY,rhoDst.T).T
rhoDstS=np.matmul(sinKY,rhoDst.T).T

uDstC=rhoDstC/kXYGrid
uDstS=rhoDstS/kXYGrid

uDst=np.matmul(cosKY,uDstC.T).T+np.matmul(sinKY,uDstS.T).T

u=np.matmul(sinKX,uDst)

u22=np.gradient(np.gradient(u,axis=0),axis=0)+np.gradient(np.gradient(u,axis=1),axis=1)
u22/=(dx*dy)

fig3=plt.figure(3)
ax = fig3.gca(projection='3d')
surf = ax.plot_surface(xMidGrid,yMidGrid,rhoGrid, cmap=cm.coolwarm,linewidth=0, antialiased=False)


fig3=plt.figure(20)
ax = fig3.gca(projection='3d')
surf = ax.plot_surface(xMidGrid,yMidGrid,u, cmap=cm.coolwarm,linewidth=0, antialiased=False)

fig3=plt.figure(31)
ax = fig3.gca(projection='3d')
surf = ax.plot_surface(xMidGrid,yMidGrid,u22, cmap=cm.coolwarm,linewidth=0, antialiased=False)

print np.sum(u22),np.sum(rhoGrid),(np.sum(u22)-np.sum(rhoGrid))/np.sum(rhoGrid)


























