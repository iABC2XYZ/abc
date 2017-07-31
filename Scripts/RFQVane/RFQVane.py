# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 11:11:22 2017

@author: A
"""


import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from scipy.special import iv
import scipy.interpolate as itp

plt.close('all')

zStart=0.
zEnd=230.
zStep=0.01

Freq=162.5
cLight=299792458
lambda_m=cLight/Freq/1.e6

Cell_V_Wsyn_Beta_E0_A10_Phi_a_m_r0_Rho_B_L_Z_ImaxT_ImaxL=np.loadtxt('Cell_V_Wsyn_Beta_E0_A10_Phi_a_m_r0_Rho_B_L_Z_ImaxT_ImaxL.txt')

cell=Cell_V_Wsyn_Beta_E0_A10_Phi_a_m_r0_Rho_B_L_Z_ImaxT_ImaxL[:,0]
Beta=Cell_V_Wsyn_Beta_E0_A10_Phi_a_m_r0_Rho_B_L_Z_ImaxT_ImaxL[:,3]
A=Cell_V_Wsyn_Beta_E0_A10_Phi_a_m_r0_Rho_B_L_Z_ImaxT_ImaxL[:,5]
a=Cell_V_Wsyn_Beta_E0_A10_Phi_a_m_r0_Rho_B_L_Z_ImaxT_ImaxL[:,7]
m=Cell_V_Wsyn_Beta_E0_A10_Phi_a_m_r0_Rho_B_L_Z_ImaxT_ImaxL[:,8]
Z=Cell_V_Wsyn_Beta_E0_A10_Phi_a_m_r0_Rho_B_L_Z_ImaxT_ImaxL[:,13]
L=Cell_V_Wsyn_Beta_E0_A10_Phi_a_m_r0_Rho_B_L_Z_ImaxT_ImaxL[:,12]

numCell=len(cell)

nREC=int((zEnd-zStart)/zStep)+1
xREC=np.zeros((nREC,2))
zREC=np.zeros(nREC)
cellREC=np.zeros(nREC)
cellFlagREC=np.zeros(nREC)


iCellFlag=1

zRec=zStart


def RFQVane(x,a,k,kz,m):
    A=(m**2-1)/(m**2*iv(0,k*a)+iv(0,m*k*a))
    #return x**2/a**2-(1-A*iv(0,k*x)*np.cos(k*z))/(1-A*iv(0,k*a))
    return x**2/a**2-(1-A*iv(0,k*x)*np.cos(kz))/(1-A*iv(0,k*a))

iREC=0;
kzCal=0
while (zRec<zEnd):
    diff_RecCell=zRec-Z
    iCell=len(diff_RecCell[diff_RecCell>0])-1  #~~~
    if (iCell<0):
        iCell=0
    
    
    iCellFlag=(-1)**iCell
            

    #k=np.pi/L[iCell]
    #betaK=np.interp(zRec,Z,Beta)
    betaK=itp.spline(Z,Beta,zRec)
    
    k=np.pi/betaK/lambda_m/100*2
    
    
    if (iCell>4):
        xRecTmp_Est=-0.3
    elif(iCell>3):
        xRecTmp_Est=-0.4
    elif(iCell>2):
        xRecTmp_Est=-0.5
    elif(iCell>1):
        xRecTmp_Est=-0.7
    elif(iCell>0):
        xRecTmp_Est=-0.9
    else:
        xRecTmp_Est=-1.2
    
    aInterP=np.interp(zRec,Z,a)
    mInterP=np.interp(zRec,Z,m)
    kzCal+=k*zStep
    xRecTmp = fsolve(RFQVane,[-0.3],args=(aInterP,k,kzCal,mInterP))
    

    xREC[iREC,:]=xRecTmp
    zREC[iREC]=zRec
    cellREC[iREC]=iCell
    cellFlagREC[iREC]=iCellFlag
    
    iREC+=1
    zRec+=zStep
    
    print zRec
    
plt.figure(1)
plt.plot(zREC,xREC[:,0],'b')
plt.hold 
plt.plot(zREC,xREC[:,1],'r')





#######################

z_HV_REF=np.loadtxt('Zc_Yc_Rpath_N_Zv_Yv_Rho.txt')
Z_REF=z_HV_REF[:,4]*2.54
X_REF=z_HV_REF[:,5]*2.54
              


plt.figure('Comp')
plt.plot(zREC,xREC,'b')
plt.hold
plt.plot(Z_REF,X_REF,'r')


xRECInterP=np.interp(Z_REF,zREC,xREC[:,0])

plt.figure('Diff')
plt.plot(Z_REF,X_REF-xRECInterP,'r')
plt.hold 
plt.plot(zREC,cellFlagREC,'g')

##

def Smooth(x):
    x[0]=x[0]
    x[1]=np.average(x[0:3])
    x[2:-3]=(x[0:-5]+x[1:-4]+x[2:-3]+x[3:-2]+x[4:-1])/5.
    x[-2]=np.average(x[-3:-1])
    x[-1]=x[-1]
    return x


indexPeak=((Z_REF>4.) * (Z_REF<228.))
ZREFPeak=Z_REF[indexPeak]
xREFPeak=X_REF[indexPeak]

xREFPeak=Smooth(xREFPeak)
xREFPeak=Smooth(xREFPeak)
xREFPeak=Smooth(xREFPeak)

xRECPeak=xRECInterP[indexPeak]
ZRECPeak=ZREFPeak

xRECPeak=Smooth(xRECPeak)
xRECPeak=Smooth(xRECPeak)
xRECPeak=Smooth(xRECPeak)


def FindPeaks(x):
    xLeft=x[1:-2]> x[0:-3]
    xRight=x[1:-2]> x[2:-1]
    '''
    xLeft_1=x[3:-4]> x[2:-5]
    xLeft_2=x[3:-4]> x[1:-6]
    xLeft_3=x[3:-4]> x[0:-7]
    
    xRight_1=x[3:-4]< x[4:-3]
    xRight_2=x[3:-4]< x[5:-2]
    xRight_3=x[3:-4]< x[6:-1]	
    '''
    xFlag=xLeft*xRight
    indexX=np.where(xFlag==1)
    return indexX
    

index_xRECPeakTuple=FindPeaks(xRECPeak)
index_xREFPeakTuple=FindPeaks(xREFPeak)

index_xRECPeak=index_xRECPeakTuple[0]
index_xREFPeak=index_xREFPeakTuple[0]


print((len(index_xRECPeak),len(index_xREFPeak)))




plt.figure('Peak')
plt.plot(ZRECPeak,xRECPeak,'b')
plt.hold
plt.plot(ZRECPeak,xREFPeak,'r')
plt.plot(ZRECPeak[index_xRECPeak],xRECPeak[index_xRECPeak],'bo')
plt.plot(ZRECPeak[index_xREFPeak],xREFPeak[index_xREFPeak],'r*')

plt.show()


print(zREC.shape)
