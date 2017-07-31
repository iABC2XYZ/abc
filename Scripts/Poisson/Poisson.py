# -*- coding: utf-8 -*-
"""
Created on Sat May 21 18:16:33 2016

@author: shine
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import math
from matplotlib import cm  

from scipy.fftpack import dst
from scipy.fftpack import idst
from scipy.fftpack import dct
from scipy.fftpack import idct

# Particles definition:
meanX=0
meanY=0


stdX=4
stdY=4


numberParticle=int(1e6)

meanXY=[meanX,meanY]
covXY=[[stdX**2,0],[0,stdY**2]]
particleDistribution=np.random.multivariate_normal(meanXY,covXY,numberParticle)

xParticle=particleDistribution[:,0]
yParticle=particleDistribution[:,1]

qParticle=np.ones(numberParticle,dtype=float)

fig1=plt.figure(1)
plt.clf
ax = fig1.gca()  
ax.plot(xParticle,yParticle,'.')
plt.show

# Domain area:
xDomainMin=-8
xDomainMax=8
yDomainMin=-8
yDomainMax=8

# Grid number:
xNumberGridLog=5
yNumberGridLog=6


xNumberGrid=2**xNumberGridLog
yNumberGrid=2**yNumberGridLog


# Domain step:
xDomainDiff=xDomainMax-xDomainMin
yDomainDiff=yDomainMax-yDomainMin
xDomainStep=xDomainDiff/(xNumberGrid-1.)
yDomainStep=yDomainDiff/(yNumberGrid-1.)


#  Particle Weighting
xRatioParticleGrid=(xParticle-xDomainMin)/xDomainStep
yRatioParticleGrid=(yParticle-yDomainMin)/yDomainStep

qParticle[xRatioParticleGrid<0]=0
qParticle[yRatioParticleGrid<0]=0
qParticle[xRatioParticleGrid>=xNumberGrid-1]=0
qParticle[yRatioParticleGrid>=yNumberGrid-1]=0



xIntRatioParticleGrid=xRatioParticleGrid.astype(np.int)
xLowFraRatioParticleGrid=xRatioParticleGrid-xIntRatioParticleGrid.astype(np.float);
xHighFraRatioParticleGrid=1.-xLowFraRatioParticleGrid

yIntRatioParticleGrid=yRatioParticleGrid.astype(np.int)
yLowFraRatioParticleGrid=yRatioParticleGrid-yIntRatioParticleGrid.astype(np.float);
yHighFraRatioParticleGrid=1.-yLowFraRatioParticleGrid

xIntRatioParticleGrid[qParticle==0]=0
yIntRatioParticleGrid[qParticle==0]=0

print(np.sum(qParticle))

qGrid=np.zeros([xNumberGrid,yNumberGrid],dtype=float)

for iNumberParticle in xrange(0,numberParticle):
    iXNumberParticle=xIntRatioParticleGrid[iNumberParticle]
    iYNumberParticle=yIntRatioParticleGrid[iNumberParticle]
    
    iX2NumberParticle=iXNumberParticle+1
    iY2NumberParticle=iYNumberParticle+1

    qGrid[iXNumberParticle,iYNumberParticle]= qGrid[iXNumberParticle,iYNumberParticle]+xHighFraRatioParticleGrid[iNumberParticle]*yHighFraRatioParticleGrid[iNumberParticle]*qParticle[iNumberParticle]
    qGrid[iXNumberParticle,iY2NumberParticle]= qGrid[iXNumberParticle,iY2NumberParticle]+xHighFraRatioParticleGrid[iNumberParticle]*yLowFraRatioParticleGrid[iNumberParticle]*qParticle[iNumberParticle]
    qGrid[iX2NumberParticle,iYNumberParticle]= qGrid[iX2NumberParticle,iYNumberParticle]+xLowFraRatioParticleGrid[iNumberParticle]*yHighFraRatioParticleGrid[iNumberParticle]*qParticle[iNumberParticle]
    qGrid[iX2NumberParticle,iY2NumberParticle]= qGrid[iX2NumberParticle,iY2NumberParticle]+xLowFraRatioParticleGrid[iNumberParticle]*yLowFraRatioParticleGrid[iNumberParticle]*qParticle[iNumberParticle]

print(np.sum(qGrid))

#fft
ssQGrid=dst(dst(qGrid).T).T
for mXNumberGrid in xrange(0,xNumberGrid):
    for mYNumberGrid in xrange(0,yNumberGrid):
        KX2=((mXNumberGrid+1)*math.pi/xDomainDiff)**2
        KY2=((mYNumberGrid+1)*math.pi/yDomainDiff)**2
        K2=KX2+KY2
        ssUGrid=ssQGrid/K2
uQgrid=idst(idst(ssUGrid.T).T)

#
xGrid=np.arange(xDomainMin,xDomainMax+xDomainStep,xDomainStep)
yGrid=np.arange(yDomainMin,yDomainMax+yDomainStep,yDomainStep)
[XGrid,YGrid]=np.meshgrid(yGrid,xGrid);
fig=plt.figure(2)
plt.clf
ax=fig.gca(projection='3d')
surf = ax.plot_surface(XGrid, YGrid, uQgrid , rstride=1, cstride=1, cmap=cm.jet,linewidth=0, antialiased=False)  
plt.show() 

# Efield:
[ExTemp,EyTemp]=np.gradient(uQgrid)
Ex=ExTemp/xDomainStep
Ey=EyTemp/yDomainStep

fig=plt.figure(3)
plt.clf
ax=fig.gca(projection='3d')
surf = ax.plot_surface(XGrid, YGrid, Ex , rstride=1, cstride=1, cmap=cm.jet,linewidth=0, antialiased=False)  
plt.show() 

fig=plt.figure(4)
plt.clf
ax=fig.gca(projection='3d')
surf = ax.plot_surface(XGrid, YGrid, Ey , rstride=1, cstride=1, cmap=cm.jet,linewidth=0, antialiased=False)  
plt.show() 

























































