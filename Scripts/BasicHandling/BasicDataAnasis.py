# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


A=np.loadtxt("wang.txt")
L=len(A)
G1=A[:,0]
G2=A[:,1]
Ex=A[:,2]
Ey=A[:,3]
Eff=A[:,4]

fig = plt.figure(1)
ax = fig.gca(projection='3d')
plt.plot(G1, G2, Ex,'.')
plt.title('Ex')
plt.xlabel('G1')
plt.ylabel('G2')


fig = plt.figure(2)
ax = fig.gca(projection='3d')
plt.plot(G1, G2, Ey,'.')
plt.title('Ey')
plt.xlabel('G1')
plt.ylabel('G2')


dG1=np.diff(G1);
dG2=np.diff(G2);

dG1Flag=dG1>0

M=sum(dG1Flag)+1
N=int(L/M)



G1Mesh=np.reshape(G1,(M,N))
G2Mesh=np.reshape(G2,(M,N))
ExMesh=np.reshape(Ex,(M,N))


fig = plt.figure(10)
ax = fig.gca(projection='3d')
ax.plot_surface(G1Mesh, G2Mesh, ExMesh)

##

ExMeshNoise=ExMesh+np.random.rand(M,N)*(max(Ex)-min(Ex))*0.2;
fig = plt.figure(11)
ax = fig.gca(projection='3d')
ax.plot_surface(G1Mesh, G2Mesh, ExMeshNoise, rstride=1, cstride=1)


##
ExMeshNoiseFFT2=np.fft.fft2(ExMeshNoise)

ExMeshNoiseFFT2_ABS=abs(ExMeshNoiseFFT2)

fig = plt.figure(20)
ax = fig.gca(projection='3d')
ax.plot_surface(G1Mesh, G2Mesh, ExMeshNoiseFFT2_ABS, rstride=1, cstride=1)


ExMeshNoiseFFT2_Shift=np.fft.fftshift(ExMeshNoiseFFT2)

ExMeshNoiseFFT2_Shift_ABS=abs(ExMeshNoiseFFT2_Shift)

fig = plt.figure(21)
ax = fig.gca(projection='3d')
ax.plot_surface(G1Mesh, G2Mesh, ExMeshNoiseFFT2_Shift_ABS, rstride=1, cstride=1)

fig = plt.figure(22)
ax = fig.gca(projection='3d')
ax.plot_surface(G1Mesh, G2Mesh, np.log2(ExMeshNoiseFFT2_Shift_ABS), rstride=1, cstride=1)


ExMeshNoiseFFT2_ShiftCopy=np.copy(ExMeshNoiseFFT2_Shift)
R=5;
meanM=(1+M)/2
meanN=(1+N)/2
for iG1 in range(M):
    for iG2 in range(N):
        if ((iG1-meanM)**2+(iG2-meanN)**2>R**2):
            ExMeshNoiseFFT2_ShiftCopy[iG1,iG2]=0

ExMeshNoiseFFT2_ShiftCopy_ABS=abs(ExMeshNoiseFFT2_ShiftCopy)
fig = plt.figure(31)
ax = fig.gca(projection='3d')
ax.plot_surface(G1Mesh, G2Mesh, ExMeshNoiseFFT2_ShiftCopy_ABS, rstride=1, cstride=1)

fig = plt.figure(32)
ax = fig.gca(projection='3d')
ax.plot_surface(G1Mesh, G2Mesh, np.log2(ExMeshNoiseFFT2_ShiftCopy_ABS), rstride=1, cstride=1)


ExMeshNoiseFFT2_iShift=np.fft.ifftshift(ExMeshNoiseFFT2_ShiftCopy)

ExMeshNoiseFFT2_iShift_Abs=abs(ExMeshNoiseFFT2_iShift)

fig = plt.figure(41)
ax = fig.gca(projection='3d')
ax.plot_surface(G1Mesh, G2Mesh, ExMeshNoiseFFT2_iShift_Abs, rstride=1, cstride=1)

fig = plt.figure(42)
ax = fig.gca(projection='3d')
ax.plot_surface(G1Mesh, G2Mesh, np.log2(ExMeshNoiseFFT2_iShift_Abs), rstride=1, cstride=1)



ExMeshNoiseMove=np.fft.ifft2(ExMeshNoiseFFT2_iShift)
ExMeshNoiseMoveReal=np.real(ExMeshNoiseMove)
ExMeshNoiseMoveImag=np.imag(ExMeshNoiseMove)

fig = plt.figure(51)
ax = fig.gca(projection='3d')
ax.plot_surface(G1Mesh, G2Mesh, ExMeshNoiseMoveReal, rstride=1, cstride=1)

fig = plt.figure(52)
ax = fig.gca(projection='3d')
ax.plot_surface(G1Mesh, G2Mesh, ExMeshNoiseMoveImag, rstride=1, cstride=1)


##

numPart=int(1e5)
#oMU=np.array([2.,3.])
#oSIGMA=np.array([[2.,3.],[3.,4.]])

oMU=[2.,3.]
oSIGMA=[[2.,1.],[1.,4.]]

xDist,xpDist=np.random.multivariate_normal(oMU,oSIGMA,numPart).T

fig = plt.figure(60)
plt.plot(xDist,xpDist,'.')

xBin=50
yBin=55
H, xedges, yedges =np.histogram2d(xDist,xpDist,bins=[xBin,yBin])

xMid=(xedges[0:xBin]+xedges[1:xBin+1])/2.
yMid=(yedges[0:yBin]+yedges[1:yBin+1])/2.

[yMesh,xMesh]=np.meshgrid(yMid,xMid)
      
 
fig = plt.figure(101)
ax = fig.gca(projection='3d')
ax.plot_surface(xMesh, yMesh, H, rstride=1, cstride=1)


dx=xMid[1]-xMid[0]
dy=yMid[1]-yMid[0]

hEmitTh=H
hEmitEx=np.reshape(hEmitTh,[xBin*yBin,1])
xEmitEx=np.reshape(xMesh,[xBin*yBin,1])
yEmitEx=np.reshape(yMesh,[xBin*yBin,1])

rho=hEmitEx/np.sum(hEmitEx)/(dx*dy)

xMean=sum(xEmitEx*rho*dx*dy)
yMean=sum(yEmitEx*rho*dx*dy)  
      

xxMean=sum((xEmitEx-xMean)**2*rho*dx*dy)
xpxpMean=sum((yEmitEx-yMean)**2*rho*dx*dy)
xxpMean=sum((xEmitEx-xMean)*(yEmitEx-yMean)*rho*dx*dy)

sigmaEx=np.array([[xxMean,xpxpMean],[xpxpMean,xxpMean]]).reshape((2,2))

emitX=np.sqrt(np.linalg.matrix_rank(sigmaEx))
betaX=xxMean/emitX
GammaX=xpxpMean/emitX
alphaX=-xxpMean/emitX

print("X Emit: ",emitX)
print("X Beta: ",betaX)
print("X Gamma: ",GammaX)
print("X Alpha: ",alphaX)
