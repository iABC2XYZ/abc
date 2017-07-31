# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 11:11:22 2017

@author: A
"""


import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from scipy.special import iv
#from scipy.signal import find_peaks_cwt

plt.close('all')

zStart=0+0.67
zEnd=230.045+0.67
zStep=0.005#########################################步长不要小于0.005，否则贝塞尔函数求解会出错

Freq=162.5
cLight=299792458
lambda_m=cLight/Freq/1.e6

cell_Beta_A_a_m_Z_L=np.loadtxt('pariout_python.txt')

cell=cell_Beta_A_a_m_Z_L[:,0]
Beta=cell_Beta_A_a_m_Z_L[:,3]
A=cell_Beta_A_a_m_Z_L[:,5]
a=cell_Beta_A_a_m_Z_L[:,7]
m=cell_Beta_A_a_m_Z_L[:,8]
Z=cell_Beta_A_a_m_Z_L[:,-3]
L=cell_Beta_A_a_m_Z_L[:,-4]
numCell=len(cell)

nREC=int((zEnd-zStart)/zStep)+1
xREC=np.zeros((nREC,2))
xREC_2=np.zeros((nREC,2))
zREC=np.zeros(nREC)
cellREC=np.zeros(nREC)
cellFlagREC=np.zeros(nREC)
RhoREC=np.zeros(nREC)

LREC=np.zeros(nREC)
Lcal=np.zeros(nREC)
    
    
    
    
    

iCellFlag=1

zRec=zStart


def RFQVane(x,a,k,z,m):########################################################定义RFQ极头函数
    A=(m**2-1)/(m**2*iv(0,k*a)+iv(0,m*k*a))
    return x**2/a**2-(1-A*iv(0,k*x)*np.cos(k*z))/(1-A*iv(0,k*a))



def Rho(a,k,m):
    A=(m**2-1)/(m**2*iv(0,k*a)+iv(0,m*k*a))
    Rho=0.75*a/np.sqrt(1-A*iv(0,k*a))
    return Rho



iREC=0;
while (zRec<zEnd):
    print(zRec)
    diff_RecCell=zRec-Z
    iCell=len(diff_RecCell[diff_RecCell>0]) -1  ###############################判断所取点在第几个Cell
    
    
    iCellFlag=(-1)**iCell
    if (iCellFlag>0):
        zCal=zRec-Z[iCell]
        zCal_2=Z[iCell]-zRec
        
    else:
        zCal=Z[iCell+1]-zRec
        zCal_2=zRec-Z[iCell-1]
        
      # zCal=zRec-Z[iCell]       
              
              
    #k=np.pi/L[iCell]
    betaK=np.interp(zRec,Z,Beta)
    
    k=np.pi/betaK/lambda_m/100*2
    #k=np.pi/np.interp(zRec,Z,L)##############################用L数据计算对比发现和用beta计算CELL长度并没有区别

    aInterP=np.interp(zRec,Z,a)
    mInterP=np.interp(zRec,Z,m)
    xRecTmp = fsolve(RFQVane,[-0.3],args=(aInterP,k,zCal,mInterP))
    xRecTmp_2 = fsolve(RFQVane,[-0.3],args=(aInterP,k,zCal_2,mInterP))
    
    RhoREC[iREC]=Rho(aInterP,k,mInterP)
    xREC[iREC,:]=xRecTmp
    xREC_2[iREC,:]=xRecTmp_2
    zREC[iREC]=zRec
    cellREC[iREC]=iCell
    cellFlagREC[iREC]=iCellFlag
    LREC[iREC]=np.interp(zRec,Z,L)
    Lcal[iREC]=betaK*lambda_m/2*100
    
    
    
    
    iREC+=1
    zRec+=zStep
    
plt.figure('calculating result')
plt.plot(zREC,xREC[:,0],'b')
plt.hold 
plt.savefig('result.png') 
#plt.plot(zREC,xREC_2[:,0],'r')


######################################对比####################################

z_HV_REF=np.loadtxt('RFQ H DATA.txt')
Z_REF=z_HV_REF[:,0]/10.
X_REF=z_HV_REF[:,1]/10
Rho_REF=z_HV_REF[:,2]/10



plt.figure('Comp')
plt.plot(zREC-0.67,xREC,'b')
plt.hold
#plt.plot(zREC,xREC_2[:,0],'g')
plt.hold
plt.plot(Z_REF,X_REF,'r')


xRECInterP=np.interp(Z_REF,zREC-0.67,xREC[:,0])

plt.figure('Diff')
plt.plot(Z_REF,X_REF-xRECInterP,'r')
plt.hold
#plt.savefig('comp.png') 
#plt.plot(zREC,cellFlagREC,'g')

########################对比Rho函数##################################################


'''
plt.figure('Rho')

plt.plot(zREC,RhoREC,'b')
plt.hold
plt.plot(Z_REF,Rho_REF,'r')
plt.hold
plt.plot(Z_REF,Rho_REF-np.interp(Z_REF,zREC,RhoREC),'g')

plt.plot(zREC,np.interp(zREC,Z_REF,Rho_REF),'g')
'''



###########################对比Cell长度读取和计算函数################################

'''
plt.figure('L_COMP')
plt.plot(zREC,LREC,'r')
plt.hold
plt.plot(zREC,Lcal,'b')
plt.hold

plt.figure('L_Ratio')
plt.plot(zREC,((LREC-Lcal)/LREC))
'''

########################分析Cell数################################################

              
def Smooth(x):
    x[0]=x[0]
    x[1]=np.average(x[0:2])
    x[2:-3]=(x[0:-5]+x[1:-4]+x[2:-3]+x[3:-2]+x[4:-1])/5.
    x[-2]=np.average(x[-3:-1])
    x[-1]=x[-1]
    return x
    
    
def FindPeaks(x):
    xLeft=x[1:-2]> x[0:-3]
    xRight=x[1:-2]> x[2:-1]
    xFlag=xLeft*xRight
    indexX=np.where(xFlag==1)
    return indexX
    

def FindValley(x):
    xLeft=x[1:-2]< x[0:-3]
    xRight=x[1:-2]< x[2:-1]
    xFlag=xLeft*xRight
    indexX=np.where(xFlag==1)
    return indexX


indexPeak=((Z_REF>4.) * (Z_REF<221.5))######################定义寻峰范围
ZREFPeak=Z_REF[indexPeak]
xREFPeak=X_REF[indexPeak]


xREFPeak=Smooth(xREFPeak)
xREFPeak=Smooth(xREFPeak)


xRECPeak=xRECInterP[indexPeak]
ZRECPeak=ZREFPeak


xRECPeak=Smooth(xRECPeak)
xRECPeak=Smooth(xRECPeak)


index_xRECPeakTuple=FindPeaks(xRECPeak)
index_xREFPeakTuple=FindPeaks(xREFPeak)


index_xRECPeak=index_xRECPeakTuple[0]
index_xREFPeak=index_xREFPeakTuple[0]


print(' xRECPeak:',len(index_xRECPeak),'\n','xREFPeak:',len(index_xREFPeak))

index_xREFValleyTuple=FindValley(xREFPeak)
index_xREFValley=index_xREFValleyTuple[0]



if len(index_xREFPeak)==len(index_xREFValley):
    if ((Z_REF[index_xREFPeak[0]])<(Z_REF[index_xREFValley[0]])):
        Lcell_HV=Z_REF[index_xREFValley]-Z_REF[index_xREFPeak]
        P_cell_PV=Z_REF[index_xREFValley]
    else:
        Lcell_HV=Z_REF[index_xREFPeak]-Z_REF[index_xREFValley]
        P_cell_PV=Z_REF[index_xREFPeak]
elif len(index_xREFPeak)<len(index_xREFValley):
    Lcell_HV=Z_REF[index_xREFPeak]-Z_REF[index_xREFValley[:-1]]
    P_cell_PV=Z_REF[index_xREFPeak]
else:
    Lcell_HV=Z_REF[index_xREFValley]-Z_REF[index_xREFPeak[-1]]
    P_cell_PV=Z_REF[index_xREFValley]



pariout=np.loadtxt('pariout_python.txt')
Cell_pariout=pariout[:,0]
Z_pariout=pariout[:,-3]
L_pariout=pariout[:,-4]
r0_pariout=pariout[:,9]
ncell_pariout=len(Z_pariout[(Z_pariout>4.)*(Z_pariout<221.5)])




'''
plt.figure('Length(HV_P-V)_comp_priout')
plt.plot(Z_REF[indexPeak],np.interp(Z_REF[indexPeak],P_cell_PV,Lcell_HV),'b')
plt.hold
plt.plot(Z_REF[indexPeak],np.interp(Z_REF[indexPeak],Z_pariout,L_pariout),'r')

print(' HV:',((len(index_xREFPeak))+len(index_xREFValley)),'\n','parioutcell:',ncell_pariout)
'''





'''
plt.figure('Peak')
plt.plot(ZRECPeak,xRECPeak,'b')
plt.hold
plt.plot(ZRECPeak,xREFPeak,'r')
plt.plot(ZRECPeak[index_xRECPeak],xRECPeak[index_xRECPeak],'bo')
plt.plot(ZRECPeak[index_xREFPeak],xREFPeak[index_xREFPeak],'r*')
plt.plot(ZRECPeak[index_xREFValley],xREFPeak[index_xREFValley],'r*')
'''
##############################计算固定极头半径######################################


r0_cal_rho=r0_pariout[4:]
L_cal_rho=L_pariout[4:]
r0_sum=0
for i in range(0,len(L_cal_rho)):
    r0_sum=r0_sum+r0_cal_rho[i]*L_cal_rho[i]
r0_rho=r0_sum/Z_pariout[-1]
rho_constant=0.75*r0_rho
print(' CST_RHO_constant=',rho_constant,'cm')


##############################################################################
plt.show()





























