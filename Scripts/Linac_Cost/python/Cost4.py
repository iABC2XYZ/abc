#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 11:18:00 2017

@author: a
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

plt.close('all')



def TTFC(nCell,betaC,betaG):
    if (np.abs(betaC-betaG)<1.0e-6):
        return np.pi/4.
    else:
        return (betaC/betaG)**2*np.cos(np.pi*nCell/(2*betaC/betaG))*(-1)**((nCell-1)/2)/(nCell*((betaC/betaG)**2-1))

        
def TTFS(nCell,betaC,betaG):
    if (np.abs(betaC-betaG)<1.0e-6):
        return np.pi/4.
    else:
        return (betaC/betaG)**2*np.sin(np.pi*nCell/(2*betaC/betaG))*(-1)**((nCell+2)/2)/(nCell*((betaC/betaG)**2-1))

        

def TTF(nCell,betaC,betaG):
    if (np.mod(nCell,2)==0):
        return TTFS(nCell,betaC,betaG)
    elif (np.mod(nCell,2)==1):
        return TTFC(nCell,betaC,betaG)
    else:
        pass
    
def TTFGen(nCell,betaG,betaStart,betaEnd,betaStep):
    betaArray=np.arange(betaStart,betaEnd,betaStep)
    TTFArray=np.zeros_like(betaArray)
    nBetaC=0
    for iBetaC in betaArray:
        TTFArray[nBetaC]=TTF(nCell,iBetaC,betaG)
        nBetaC+=1
    return betaArray,TTFArray
    
def TTFOptGet(betaArray,TTFArray):
    indexOpt=np.argmax(TTFArray)
    betaOpt=betaArray[indexOpt]
    return betaOpt

def BetaOptTTFGen(nCell,betaOpt,betaStart,betaEnd,betaStep):
    if betaOpt<0.1:
        betaGStart=0
    else:
        betaGStart=betaOpt-0.1
    betaGEnd=betaOpt+0.05
    betaOptNum=100
    betaGArray=np.linspace(betaGStart,betaGEnd,betaOptNum)
    betaOptArray=np.zeros_like(betaGArray)
    
    betaEndUse=betaGEnd+0.15
    if (betaEndUse>1.):
        betaEndUse=1.
    betaStepUse=0.001
    iRec=0
    for betaG in betaGArray:
        betaArray,TTFArray=TTFGen(nCell,betaG,betaGStart,betaEndUse,betaStepUse)
        betaOptArray[iRec]= TTFOptGet(betaArray,TTFArray)
        iRec+=1
    
    TTFOptFunc=interp1d(betaOptArray,betaGArray, kind='cubic')
    betaG=TTFOptFunc(betaOpt)
    betaArray,TTFArray=TTFGen(nCell,betaG,betaStart,betaEnd,betaStep)
    return betaArray,TTFArray

def TTFBetaOptCST(nCell,betaOpt,betaStart,betaEnd,betaStep,TTFCST):
    betaArray,TTFArray=BetaOptTTFGen(nCell,betaOpt,betaStart,betaEnd,betaStep)
    TTFArray=TTFArray/np.max(TTFArray)*TTFCST
    return betaArray,TTFArray


def Energy2Beta(energyMeV):
    gammaC=1.+energyMeV/938.272
    betaC=np.sqrt(1.-1./gammaC**2)
    return betaC

def Smooth(x):
    x[0]=x[0]
    x[1]=np.average(x[0:3])
    x[2:-3]=(x[0:-5]+x[1:-4]+x[2:-3]+x[3:-2]+x[4:-1])/5.
    x[-2]=np.average(x[-3:-1])
    x[-1]=x[-1]
    return x

def FindPeaks(x):
    xLeft=x[1:-2]> x[0:-3]
    xRight=x[1:-2]>= x[2:-1]
    xFlag=xLeft*xRight
    indexX=np.where(xFlag==1)
    return indexX



def ReadEz(EzFile):
    EzFileData=np.loadtxt(EzFile)
    zm=EzFileData[:,0]/1000.
    EzMVm=EzFileData[:,1]/1.e6
    return zm,EzMVm

def InterVoltage(zm,EzMVm):
    dz=zm[1::]-zm[0:-1]
    meanEzMVm=(EzMVm[1::]+EzMVm[0:-1])/2.
    return np.sum(dz*meanEzMVm)

def LEffCST(BetaOpt):
    if (BetaOpt==0.62):
        lEff=(66.9*10+2*2.68)/1000.
    elif (BetaOpt==0.82):
        lEff=(89.9*10+2*0.66)/1000.
    return lEff

def DealEzData(EzFile,BetaOpt,RFFreMHz):
    zm,EzMVm=ReadEz(EzFile)
    lambdaM=299792458./RFFreMHz/1.e6
    K=2*np.pi/(BetaOpt*lambdaM)
    KZ=K*zm
    EzMVmExp=EzMVm*np.cos(KZ)
    VInteger=InterVoltage(zm,np.abs(EzMVm))
    VExp=InterVoltage(zm,EzMVmExp)
    
    TTFOpt=VExp/VInteger
    lEff=LEffCST(BetaOpt)
    EaccNorm=TTFOpt/lEff
    EzMVmNorm=EzMVm/VInteger
    
    return zm,EzMVmNorm,lEff,TTFOpt,EaccNorm,VInteger


def Discrete(Eacc,phiSynDeg,betaOpt,nCell,energyStart,energyEnd,RFFreMHz):
    EzFile='Ez-0'+np.str(betaOpt)[2::]+'.txt'
    zm,EzMVmNorm,lEff,TTFOpt,EaccNorm,VInteger=DealEzData(EzFile,betaOpt,RFFreMHz)
    
    betaStart=Energy2Beta(energyStart)
    betaEnd=Energy2Beta(energyEnd+Eacc*lEff*3)
    betaStep=0.001
    betaArray,TTFArray=TTFBetaOptCST(nCell,betaOpt,betaStart,betaEnd,betaStep,TTFOpt)
    TTFFunc=interp1d(betaArray, TTFArray, kind='cubic')
    
    TTFMean=np.mean(TTFArray)
    EnergyMean=Eacc/TTFOpt*TTFMean*lEff*np.cos(np.deg2rad(phiSynDeg))
    numCavity=int((energyEnd-energyStart)/EnergyMean*1.2)
    
    CavityEnergyStart=np.zeros(numCavity)
    CavityEnergyEnd=np.zeros(numCavity)
    CavityEnergyCenter=np.zeros(numCavity)
    
    nCavity=0
    energyCavityStart=energyStart
    while(energyCavityStart<energyEnd):
        betaCavityStart=Energy2Beta(energyCavityStart)
        betaCavityCenter=betaCavityStart
        
        deltaBetaCavityCenter=1.
        deltaBetaCavityCenterRef=1.1
        
        while(deltaBetaCavityCenter<deltaBetaCavityCenterRef):
            TTFCenter=TTFFunc(betaCavityCenter)
            
            energyCavityIncrease=Eacc*lEff*(TTFCenter/TTFOpt)*np.cos(np.deg2rad(phiSynDeg))
            
            energyCavityEnd=energyCavityStart+energyCavityIncrease
            energyCavityCenter=(energyCavityEnd+energyCavityStart)/2.
            deltaBetaCavityCenterRef=deltaBetaCavityCenter
            deltaBetaCavityCenter=Energy2Beta(energyCavityCenter)
        
        
        CavityEnergyStart[nCavity]=energyCavityStart
        CavityEnergyEnd[nCavity]=energyCavityEnd
        CavityEnergyCenter[nCavity]=energyCavityCenter
                          
        energyCavityStart=energyCavityEnd
        nCavity+=1
    
    CavityEnergyStartRec=CavityEnergyStart[:nCavity:]
    CavityEnergyEndRec=CavityEnergyEnd[:nCavity:]
    CavityEnergyCenterRec=CavityEnergyCenter[:nCavity:]

    numCavity=nCavity

    return numCavity,CavityEnergyStartRec,CavityEnergyCenterRec,CavityEnergyEndRec

def GetLength(betaOpt,numCavity):
    '''
        as for 062:  4 cavities per cromodule
        the field length is 1014
        the cavity length is 114+1014+114
        the interval length between two cavity is 130
        and the synchronous phase is about -22 deg
        
        the interval between two cromodule is 400+ 130+500 + 130+400+350
        
        SO:
            the length of one cromodule is (114+1014+114)*4+130*3=5358
            the length between two cromodules is 400+ 130+500 + 130+400+350=1910
            So: 
                Every Cromodule length is 7268 (every 4 Cavities)
                
        
    as for 082:  5 cavities per cromodule
        the field length is 1234
        the cavity length is 114+1234+114
        the interval length between two cavity is 100
        and the synchronous phase is about -17 deg
        
        the interval between two cromodule is 400+ 100+500 + 100+400+350
    
        SO:
            the length of one cromodule is (114+1234+114)*5+100*4=7710
            the length between two cromodules is 400+ 100+500 + 100+400+350=1850
            So: 
                Every Cromodule length is 9560 (every 5 Cavities)
    '''
    if (betaOpt==0.62):
        #return np.ceil(numCavity/4)*7.268
        return numCavity/4*7.268
    elif (betaOpt==0.82):
        #return np.ceil(numCavity/5)*9.560
        return numCavity/4*7.268
    else:
        pass

def GetPower(betaOpt,Eacc,numCavity):
    '''
            低温站：
        4.5k-> 2K   3.6倍的钱   功率转化 （总功率=静态+动态）
        漏热：静态：5W/腔        
        	动态：我算那个： 9.88*1.5*(Eacc/10)^2   +  ARG(场知发射)
        			ARG:     10MV/m   0      
        					12     2W
        					15: 		15W
        					： exp(Eacc-10)/20    [w]
        
        先用总功率算建设成本
        再用总功率算运行成本
    '''
    
    powerStatic=5*numCavity   # w
    if (Eacc<10):
        powerARG=0.
    else:
        powerARG=np.exp((Eacc-10.)/20.)
    if(betaOpt==0.62):
        powerEacc=numCavity*9.88*1.5*(Eacc/10.)**2
    elif(betaOpt==0.82):
        powerEacc=numCavity*15.69*1.5*(Eacc/12.)**2
    powerDynamic=powerARG+powerEacc
    powerSum=powerStatic+powerDynamic
    return powerSum
    

def GetLengthANDPower(Eacc,phiSynDeg,betaOpt,nCell,energyStart,energyEnd,RFFreMHz):
    '''
        2K heat load
    '''
    numCavity,CavityEnergyStartRec,CavityEnergyCenterRec,CavityEnergyEndRec=Discrete(Eacc,phiSynDeg,betaOpt,nCell,energyStart,energyEnd,RFFreMHz)
    AcceleratorLength=GetLength(betaOpt,numCavity)
    powerSum=GetPower(betaOpt,Eacc,numCavity)
    return numCavity,AcceleratorLength,powerSum

def GetAcceleratorConstructionCost(AcceleratorLength):
    '''
        腔：170 w/m   (算module)      ：
        现在一个module 300w壳   
        腔体：30万材料  38加工 +20w磁屏蔽 + coupler 24万 + 调谐器 10w+（ 磁铁 20w）+=122W 
        长度：1230 mm
        Module价格 50W/m   （6m）
        4-Cavity cro： 300+ 122*4=788w，长度是4.92m，隧道4.92*30w/m=147.6W，合计935.6W，合190.2W/m
        附属设备（真空计3W/set+温度、arc（打火）、水流量（一路5000）+微波管道（1500/m*10m）+低电平（10w/套）+）
        所以所有加起来  220W/m    (其中隧道定为50w/m)
    '''
    return 220*AcceleratorLength

def RefrigerationCapacityVSCapitalCost(valueCapacityKW,exchangeRate):
    xkW=[0.002,30]
    yCost=[0.022,20]

    pkWCost=np.polyfit(np.log10(xkW),np.log10(yCost),1)
    numPoint=1000
    xkWArray=np.linspace(xkW[0],xkW[-1],numPoint)
    yCostArray=10**np.polyval(pkWCost,np.log10(xkWArray))
    
    CostRefrigerationFunc=interp1d(xkWArray,yCostArray, kind='cubic')
    return CostRefrigerationFunc(valueCapacityKW)*1e6*exchangeRate/1e4

def GetRefrigeratorCapitalCost(powerSum2K):
    '''
        2k->4.5K     3.5 or 3.6 times power
        Cost of Refrigerator : Cost of the byside fancility =3:1 ; so all cost = Refrigerator cost *4/3
    '''
    powerSum2K_KW=powerSum2K/1e3
    powerSum4_5K_KW=powerSum2K_KW*3.6
    exchangeRate=7.0
    return  RefrigerationCapacityVSCapitalCost(powerSum4_5K_KW,exchangeRate)*4/3
    

def GetRefrigeratorOperationCost(powerSum2K,yearOperation):
    '''
        2k->4.5K     3.5 or 3.6 times power
      
        elec:
        2K ~~~  heat load : city electicity = 1:745
        4.5K  ~~~  heat load : city electicity = 1:280
        
        water:
        20% of Elec
        
        Price of Elec: 0.9
        260 days one year AND 24 hours one day.
    '''
    powerSum2K_KW=powerSum2K/1e3
    powerSum4_5K_KW=powerSum2K_KW*3.6
    powerCityElec=powerSum4_5K_KW*280
    AllElec=yearOperation*260*24*powerCityElec
    CostElec=AllElec*0.9
    CostWater=CostElec*0.2
    CostALL=(CostElec+CostWater)/1e4
    return CostALL

def CostCalculation(Eacc,phiSynDeg,betaOpt,nCell,energyStart,energyEnd,RFFreMHz):
    numCavity,AcceleratorLength,powerSum2K=GetLengthANDPower(Eacc,phiSynDeg,betaOpt,nCell,energyStart,energyEnd,RFFreMHz)

    costAcceleratorConstruction=GetAcceleratorConstructionCost(AcceleratorLength)
    costRefrigeratorConstruction= GetRefrigeratorCapitalCost(powerSum2K)
    costRefrigeratorOperation=GetRefrigeratorOperationCost(powerSum2K,yearOperation)
    return costAcceleratorConstruction,costRefrigeratorConstruction,costRefrigeratorOperation,numCavity

#######################
cavityType='082'


if (cavityType=='062'):
    betaOpt=0.62
    energyStart=168
    energyEnd=361
    phiSynDeg=-22
    RFFreMHz=650
    yearOperation=10
    nCell=5
elif (cavityType=='082'):
    betaOpt=0.82
    energyStart=361
    energyEnd=645
    phiSynDeg=-17
    RFFreMHz=650
    yearOperation=10
    nCell=5
else:
    pass

'''
Eacc=9
numCavity,AcceleratorLength,powerSum2K=GetLengthANDPower(Eacc,phiSynDeg,betaOpt,nCell,energyStart,energyEnd,RFFreMHz)

costAcceleratorConstruction=GetAcceleratorConstructionCost(AcceleratorLength)
costRefrigeratorConstruction= GetRefrigeratorCapitalCost(powerSum2K)
costRefrigeratorOperation=GetRefrigeratorOperationCost(powerSum2K,yearOperation)


print(numCavity,AcceleratorLength,powerSum2K)
print(costAcceleratorConstruction,costRefrigeratorConstruction,costRefrigeratorOperation)
'''

EaccArray=np.arange(10,25,0.5)

costAcceleratorConstructionArray=np.zeros_like(EaccArray)
costRefrigeratorConstructionArray=np.zeros_like(EaccArray)
costRefrigeratorOperationArray=np.zeros_like(EaccArray)
numCavityArray=np.zeros_like(EaccArray)

nCal=0
for Eacc in EaccArray:
    costAcceleratorConstruction,costRefrigeratorConstruction,costRefrigeratorOperation,numCavity=CostCalculation(Eacc,phiSynDeg,betaOpt,nCell,energyStart,energyEnd,RFFreMHz)
    costAcceleratorConstructionArray[nCal]=costAcceleratorConstruction
    costRefrigeratorConstructionArray[nCal]=costRefrigeratorConstruction
    costRefrigeratorOperationArray[nCal]=costRefrigeratorOperation
    numCavityArray[nCal]=numCavity
    nCal+=1
    print(Eacc)

CostADS=costAcceleratorConstructionArray+costRefrigeratorConstructionArray+costRefrigeratorOperationArray

plt.figure('COST')
plt.plot(EaccArray,costAcceleratorConstructionArray,'k')
plt.plot(EaccArray,costRefrigeratorConstructionArray,'m')
plt.plot(EaccArray,costRefrigeratorOperationArray,'b')
plt.plot(EaccArray,CostADS,'r')
plt.xlabel('Eacc    (MV/m)')
plt.ylabel('COST   / W')
plt.title('Black: Accelerator   Pink: Refrigerator  Blue: RefrigeratorOperation  Red:All')

plt.figure('NUMCAVITY')
plt.plot(EaccArray,numCavityArray,'k')

plt.xlabel('Eacc    (MV/m)')
plt.ylabel('numCavity')

