# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:17:47 2017

@author: A
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

numPart=np.int64(1e4)

xGridLog,yGridLog,zGridLog=4,5,6
xGrid,yGrid,zGrid=2**xGridLog,2**yGridLog,2**zGridLog

xMin=-4.
xMax=4.
yMin=-8.
yMax=8.

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

xMid=(xArray[0:-1:]+xArray[1::])/2.
yMid=(yArray[0:-1:]+yArray[1::])/2.

yMidGrid,xMidGrid=np.meshgrid(yMid,xMid)

fig3=plt.figure(3)
ax = fig3.gca(projection='3d')
surf = ax.plot_surface(xMidGrid,yMidGrid,rhoGrid, cmap=cm.coolwarm,linewidth=0, antialiased=False)

plt.figure(4)
plt.plot(x,y,'.')

plt.show()



def SinKM(N):
    k=np.linspace(1,N,N)
    m=k
    K,M=np.meshgrid(k,m)
    KM=K*M
    sinKM=np.sin(np.pi*KM/(N+1.))
    sinKM*=np.sqrt(2./(N+1))
    return sinKM

sinX=SinKM(xGrid)
sinY=SinKM(yGrid)


rhoDst=np.matmul(sinY,np.matmul(sinX,rhoGrid).T).T

fig3=plt.figure(10)
ax = fig3.gca(projection='3d')
surf = ax.plot_surface(xMidGrid,yMidGrid,rhoDst, cmap=cm.coolwarm,linewidth=0, antialiased=False)








