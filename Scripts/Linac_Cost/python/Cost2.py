# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 09:28:26 2017

@author: A
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
    
def Energy2Beta(energyMeV):
    gammaC=1.+energyMeV/938.272
    betaC=np.sqrt(1.-1./gammaC**2)
    return betaC

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


def ReadFieldFile(cavityType):
    if (cavityType=='062'):
        fieldFile='062.txt'
    elif(cavityType=='082'):
        fieldFile='082.txt'
    
    dataRead=np.loadtxt(fieldFile)
    zReadM=dataRead[:,0]
    EzReadMV=dataRead[:,1]
    lCavityM=zReadM[-1]
    
    EzReadSmooth=Smooth(abs(EzReadMV))
    indexPeaks=FindPeaks(EzReadSmooth)
    nCell=len(indexPeaks[0])
    return zReadM,EzReadMV,lCavityM,nCell



###############

def Discrete(eAcc,lCell,phiSynDeg,betaOpt,nCell,energyStart,energyEnd):
    betaStart=Energy2Beta(energyStart)

    betaEnd=Energy2Beta(energyEnd+eAcc*lCell*3)
    
    betaStep=0.002
    
    betaArray,TTFArray=BetaOptTTFGen(nCell,betaOpt,betaStart,betaEnd,betaStep)
    
    TTFFunc=interp1d(betaArray, TTFArray, kind='cubic')
    
    numCell=int((energyEnd-energyStart)/(eAcc*lCell**np.cos(phiSynDeg/180.*np.pi)*np.min(TTFArray)))
    cellEnergyStart=np.zeros(numCell)
    cellEnergyEnd=np.zeros(numCell)
    cellEnergyCenter=np.zeros(numCell)
    
    nCell=0
    energyCellStart=energyStart
    while(energyCellStart<energyEnd):
        betaCellStart=Energy2Beta(energyCellStart)
        betaCellCenter=betaCellStart
        
        deltaBetaCellCenter=1.
        deltaBetaCellCenterRef=1.1
        
        while(deltaBetaCellCenter<deltaBetaCellCenterRef):
            TTFCenter=TTFFunc(betaCellCenter)
            energyCellEnd=energyCellStart+eAcc*lCell*TTFCenter*np.cos(phiSynDeg/180.*np.pi)
            energyCellCenter=(energyCellEnd+energyCellStart)/2.
            deltaBetaCellCenterRef=deltaBetaCellCenter
            deltaBetaCellCenter=Energy2Beta(energyCellCenter)
        energyCellStart=energyCellEnd
        
        cellEnergyStart[nCell]=energyCellStart
        cellEnergyEnd[nCell]=energyCellEnd
        cellEnergyCenter[nCell]=energyCellCenter
        nCell+=1
    
    cellEnergyStartRec=cellEnergyStart[:nCell:]
    cellEnergyEndRec=cellEnergyEnd[:nCell:]
    cellEnergyCenterRec=cellEnergyCenter[:nCell:]

    numCell=nCell

    return numCell,cellEnergyStartRec,cellEnergyCenterRec,cellEnergyEndRec
            

"""
def ReadFieldFile(fieldFile):
    dataRead=np.loadtxt(fieldFile)
    zRead=dataRead[:,0]
    EzRead=dataRead[:,3]
    lCavity=zRead[-1]
    zStep=zRead[1::]-zRead[0:-1:]
    EzReadAveABS=(np.abs(EzRead[1::])+np.abs(EzRead[0:-1:]))/2.
    uCavity=np.sum(EzReadAveABS*zStep)
    eAverage=uCavity/lCavity
    EzReadSmooth=Smooth(abs(EzRead))
    indexPeaks=FindPeaks(EzReadSmooth)
    print(indexPeaks)
    nCell=len(indexPeaks[0])
    eAcc=np.max(abs(EzRead))
    return eAverage,lCavity,nCell,eAcc

def ReadFieldFileGetOriginData(fieldFile):
    dataRead=np.loadtxt(fieldFile)
    zRead=dataRead[:,0]
    EzRead=dataRead[:,3]
    return zRead,EzRead
"""

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

def GetNumCavity(betaOpt,energyStart,energyEnd,phiSynDeg):
    #betaOpt=0.62
    #energyStart=168
    #energyEnd=361
    #phiSynDeg=-22
    EfieldFile='0'+np.str(betaOpt)[2::]+'.txt'
    eAverageRef,lCavity,nCell,eAccRef=ReadFieldFile(EfieldFile)
    
    eAccStart=0   # MeV
    eAccEnd=20  #MeV
    eAccSweepNumber=10  # sweep 100 points
    eAccArray=np.linspace(eAccStart,eAccEnd,eAccSweepNumber)
    numCavityArray=np.zeros_like(eAccArray)
    
    iEAcc=0
    for eAcc in eAccArray:
        eAverage=eAverageRef*eAcc/eAccRef
        numCavity,cellEnergyStartRec,cellEnergyCenterRec,cellEnergyEndRec=Discrete(eAverage,lCavity,phiSynDeg,betaOpt,nCell,energyStart,energyEnd)
        numCavityArray[iEAcc]=numCavity
        iEAcc+=1
   
    #plt.figure('eAcc-numCavity')
    #plt.plot(eAccArray,numCavityArray)
    return eAccArray,numCavityArray
    

def GetNumCavityANDPower(betaOpt,energyStart,energyEnd,phiSynDeg,frequencyRFMHz,yearOperation):
    #betaOpt=0.62
    #energyStart=168
    #energyEnd=361
    #phiSynDeg=-22
    
    if(betaOpt==0.62):
        Rs=10e-9      #10 n ohm
        R_Q0_G=1
    elif (betaOpt==0.82):
        Rs=10e-9      #10 n ohm
        R_Q0_G=1
    else:
        pass
    
    EfieldFile='0'+np.str(betaOpt)[2::]+'.txt'
    eAverageRef,lCavity,nCell,eAccRef=ReadFieldFile(EfieldFile)
    zRead,EzRead=ReadFieldFileGetOriginData(EfieldFile)
    deltaZRead=zRead[2]-zRead[1]
    lambdaM=299792458./frequencyRFMHz/1.e6
    
    eAccStart=1   # MeV
    eAccEnd=20  #MeV
    eAccSweepNumber=100  # sweep 100 points
    eAccArray=np.linspace(eAccStart,eAccEnd,eAccSweepNumber)
    numCavityArray=np.zeros_like(eAccArray)
    powerCavityArray=np.zeros_like(eAccArray)
    
    iEAcc=0
    for eAcc in eAccArray:
        eAverage=eAverageRef*eAcc/eAccRef
        numCavity,cellEnergyStartRec,cellEnergyCenterRec,cellEnergyEndRec=Discrete(eAverage,lCavity,phiSynDeg,betaOpt,nCell,energyStart,energyEnd)
        numCavityArray[iEAcc]=numCavity
        
        '''
        cellBetaCenter=Energy2Beta(cellEnergyCenterRec)
        for iBeta in cellBetaCenter:
            kWaveNum=2*np.pi/(iBeta*lambdaM)
            vCavity=np.sum(EzRead*eAcc/eAccRef*np.cos(kWaveNum*zRead+np.pi/2))*deltaZRead

            powerCavity=(vCavity**2)*Rs/R_Q0_G
            powerCavityArray[iEAcc]+=powerCavity
        '''
        
        if(betaOpt==0.62):
            powerCavityArray[iEAcc]=numCavity*9.88*1.5*(eAcc/10)**2
        elif(betaOpt==0.82):
            powerCavityArray[iEAcc]=numCavity*15.69*1.5*(eAcc/12)**2
        else:
            pass
        
        iEAcc+=1
   
    powerCavityYearsArray=powerCavityArray*yearOperation*260*24
    #plt.figure('eAcc-numCavity')
    #plt.plot(eAccArray,numCavityArray)
    return eAccArray,numCavityArray,powerCavityArray,powerCavityYearsArray
    

def CostConstruction(betaOpt,numCavity):
    if(betaOpt==0.62):
        if (np.mod(numCavity,4)==0):
            nCro=numCavity/4
        else:
            nCro=int(numCavity/4)+1
        lAcceleratorM=nCro*7.268
        costAcceleratorWan=lAcceleratorM*200    # 170 W for Accelerator    & 30 W for Tunnel
        return costAcceleratorWan
    elif(betaOpt==0.82):
        if (np.mod(numCavity,5)==0):
            nCro=numCavity/5
        else:
            nCro=numCavity/5+1
        lAcceleratorM=nCro*9.560
        costAcceleratorWan=lAcceleratorM*200    # 170 W for Accelerator    & 30 W for Tunnel
        return costAcceleratorWan
    else:
        pass

def CostConstructionArray(betaOpt,numCavityArray):
    costAcceleratorWanArray=np.zeros_like(numCavityArray)
    iNumCavity=0
    for numCavity in numCavityArray:
        costAcceleratorWanArray[iNumCavity]=CostConstruction(betaOpt,numCavity)
        iNumCavity+=1
        print(iNumCavity)
    return costAcceleratorWanArray

def CostOperation(powerCavityArray):
    return powerCavityArray*1e3/1e3*0.9/1e4    # *1e3 cro-> elec   /1e3  wh ->kwh




'''
betaOpt=0.62
energyStart=168
energyEnd=361
phiSynDeg=-22

eAccArray,numCavityArray=GetNumCavity(betaOpt,energyStart,energyEnd,phiSynDeg)
costConstructionArray=CostConstructionArray(betaOpt,numCavityArray)

plt.figure('eAcc-numCavity')
plt.plot(eAccArray,numCavityArray)

plt.figure('eAcc-costConstructionArray')
plt.plot(eAccArray,costConstructionArray)
'''
cavityType='082'

if (cavityType=='062'):
    betaOpt=0.62
    energyStart=168
    energyEnd=361
    phiSynDeg=-22
    frequencyRFMHz=650
    yearOperation=10
elif (cavityType=='082'):
    betaOpt=0.82
    energyStart=361
    energyEnd=645
    phiSynDeg=-17
    frequencyRFMHz=650
    yearOperation=10
else:
    pass

'''
eAccArray,numCavityArray,powerCavityArray,powerCavityYearsArray=GetNumCavityANDPower(betaOpt,energyStart,energyEnd,phiSynDeg,frequencyRFMHz,yearOperation)

costConstructionArray=CostConstructionArray(betaOpt,numCavityArray)
costOperationArray=CostOperation(powerCavityYearsArray)

costAllArray=costConstructionArray+costOperationArray

costAllFit=np.poly1d(np.polyfit(eAccArray,costAllArray,15))
costAllFitValue=costAllFit(eAccArray)

indexCostMin=np.argmin(costAllFitValue)
print('Cavity type:  ', betaOpt)
print('Energy start MeV:  ', energyStart)
print('Energy end MeV:  ', energyEnd)
print('Synch phase  deg: ',phiSynDeg)
print('Cost Min  WRMB:',costAllFitValue[indexCostMin])
print('Eacc MV/m :  ',eAccArray[indexCostMin] )
print('Cro power / W : ', powerCavityArray[indexCostMin])
print('cavity number : ', numCavityArray[indexCostMin])
print('Cost Construction / WRMB :', costConstructionArray[indexCostMin])
print('Cost operation with in '+np.str(yearOperation)+' years  / WRMB :', costOperationArray[indexCostMin])

plt.figure('Eacc - COST')
plt.hold
plt.plot(eAccArray,costConstructionArray,'b')
plt.plot(eAccArray,costOperationArray,'m')
plt.plot(eAccArray,costAllArray,'r')
plt.plot(eAccArray,costAllFitValue,'k')
plt.xlabel('Eacc / MV/m')
plt.ylabel('COST / WRMB')
plt.title(cavityType+'   b: Construction  m:Operation('+np.str(yearOperation)+'Y)    r:All  k: Fit')

plt.savefig(cavityType+'.jpg')

'''

