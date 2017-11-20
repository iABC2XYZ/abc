#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：
    1.需要判断是否有束流。因为这里是CM1，因此只用acct3即可，当acct3没有束流时候，显示“acct3”没有束流。
    2.需要判断螺线管能不能加，如果某个螺线管不能加，直接显示该螺线管的名称
    3.需要判断bpm能不能动。如果bpm不动，那么提示那个bpm不动
    4.需要知道螺线管的电流上下值
    5.前面MEBT一定要调好，可以在很小的范围内浮动。
    6. BPM数据：BPM5-BPM10，x11和y11
    7. 螺线管电流：s1-s5
"""
import time
import numpy as np
import os
import matplotlib.pyplot as plt
plt.close('all')

def GetACCT3():
    acct3=np.random.random()  # acct3=caget('ADS_SLIT_VALUE.CHAN6_VAL_M')
    return acct3

def GetBeamCurrent():
    acct1=np.random.random()  # acct1=caget('ADS_SLIT_VALUE.CHAN4_VAL_M')
    acct2=np.random.random()  # acct2=caget('ADS_SLIT_VALUE.CHAN5_VAL_M')
    acct3=np.random.random()  # acct3=caget('ADS_SLIT_VALUE.CHAN6_VAL_M')
    fc2=np.random.random()  # fc2=caget('ADS_SLIT_VALUE.CHAN2_VAL')
    return acct1,acct2,acct3,fc2
    
def CheckBeamCurrent(acct1,acct2,acct3,fc2,acct1Check=1,acct2Check=1,acct3Check=1,fc2Check=1):
    flagCheckCurrent=0   
    if acct1<acct1Check:
        print "Current:acct1"
        print iRec
        flagCheckCurrent=1
    if acct2<acct2Check:
        print "Current:acct2"
        print iRec
        flagCheckCurrent=1
    if acct3<acct3Check:
        print "Current:acct3"
        print iRec
        flagCheckCurrent=1
    if fc2>fc2Check:
        print "Current:fc2"
        print iRec
        flagCheckCurrent=1
    return flagCheckCurrent

def GetDCCurrent(numDC,numCM=1):    
    iDCH=[]
    iDCV=[]
    for i in xrange(numDC):
        nameDC_H=nameDC.replace('H_99','H_0'+str(i+1)).replace('X',str(numCM))
        nameDC_V=nameDC.replace('H_99','V_0'+str(i+1)).replace('X',str(numCM))
        
        iDCHTmp=np.random.random()  #    iDCHTmp=caget(nameDC_H)  
        iDCVTmp=np.random.random()  #    iDCVTmp=caget(nameDC_V)  
        
        iDCH.append(iDCHTmp)
        iDCV.append(iDCVTmp)
                
    return iDCH,iDCV


    
def CheckDCCurrent(iRec,numDC,numCM=1):
    if iRec==0:
        iDCH_0,iDCV_0=[argMax+1]*5,[argMax+1]*5
    else:
        iDCH_0,iDCV_0=iDCH,iDCV
    iDCH,iDCV=GetDCCurrent(numDC)  
    flagCheckDCCurrent=0
    for i in range(numDC):
        if np.abs(iDCH[i]-iDCH_0[i])<1e-3:
            print 'DC: H: '+str(i+1) 
            print iRec
            flagCheckDCCurrent=1
        if np.abs(iDCV[i]-iDCV_0[i])<1e-3:
            print 'DC: V: '+str(i+1)   
            print iRec
            flagCheckDCCurrent=1
    return flagCheckDCCurrent

    
def GetBPM(idStart=5,idEnd=10):
    xBPM=[]
    yBPM=[]
    for i in range(idStart,idEnd+1):
        xNameBPM=nameBPM.replace('0-X',str(i)+'-X')
        yNameBPM=nameBPM.replace('0-X',str(i)+'-Y')
        xBPMTmp=np.random.random()   # xBPMTmp=caget(xNameBPM)
        yBPMTmp=np.random.random()   # yBPMTmp=caget(yNameBPM)
        xBPM.append(xBPMTmp)
        yBPM.append(yBPMTmp)
    return xBPM,yBPM
            

def CheckBPM(iRec,idStart=5,idEnd=10):
    if iRec==0:
        xBPM_0,yBPM_0=[100.]*(idEnd+1-idStart),[100.]*(idEnd+1-idStart)
    else:
        xBPM_0,yBPM_0=xBPM,yBPM
    xBPM,yBPM=GetBPM(idStart,idEnd)
    
    flagCheckBPM=0
    for i in range(idEnd+1-idStart):
        if np.abs(xBPM[i]-xBPM_0[i])<1e-3:
            print 'BPM: X: '+str(i+idStart) 
            print iRec
            flagCheckBPM=1
        if np.abs(yBPM[i]-yBPM_0[i])<1e-3:
            print 'BPM: Y: '+str(i+idStart) 
            print iRec
            flagCheckBPM=1
    return flagCheckBPM      
    
def GenRandDCCurrent(numDC,argMin,argMax):
    iDCH=np.random.random((numDC))*(argMax-argMin)+argMin
    iDCV=np.random.random((numDC))*(argMax-argMin)+argMin
    iDCHFlag=np.sign(np.random.random((numDC))-0.5)
    iDCVFlag=np.sign(np.random.random((numDC))-0.5)
    return iDCH,iDCV,iDCHFlag,iDCVFlag
    
def Reflect(iDCH,argMin,argMax,iDCHFlag):
    print iDCHFlag
    
    iDCHFlag[iDCH>argMax]=-iDCHFlag[iDCH>argMax]
    iDCHFlag[iDCH<argMin]=-iDCHFlag[iDCH<argMin]
    
    print iDCHFlag 
    print '-'*15
    
    iDCH[iDCH>argMax]=argMax*2-iDCH[iDCH>argMax]
    iDCH[iDCH<argMin]=argMin*2-iDCH[iDCH<argMin]
    return iDCH,iDCHFlag

def UpdateRandDCCurrent(iDCH,iDCV,argMin,argMax,argAmp,iDCHFlag,iDCVFlag):
    numDC=len(iDCH)
    dDCH=(np.random.random((numDC)))*argAmp*iDCHFlag
    dDCV=(np.random.random((numDC)))*argAmp*iDCVFlag
    iDCH+=dDCH
    iDCV+=dDCV
    iDCH,iDCHFlag=Reflect(iDCH,argMin,argMax,iDCHFlag)
    iDCV,iDCVFlag=Reflect(iDCV,argMin,argMax,iDCVFlag)
    return iDCH,iDCV,iDCHFlag,iDCVFlag
    
def GenDCHCrruent(iRec,stepFreshGen,numDC,argMin,argMax,argAmp):          
    if iRec % stepFreshGen==0:
        iDCH,iDCV,iDCHFlag,iDCVFlag=GenRandDCCurrent(numDC,argMin,argMax)
    else:
        iDCH,iDCV,iDCHFlag,iDCVFlag=UpdateRandDCCurrent(iDCH,iDCV,argMin,argMax,argAmp,iDCHFlag,iDCVFlag)
    iDCH,iDCV=np.round(iDCH*100)/100,np.round(iDCV*100)/100
    return iDCH,iDCV    

def PutDCH(iDCH,iDCV,numDC,numCM=1):
    nameDC='HCMX_PS:DCH_99:IMon'
    for i in range(0,numDC):
        nameDCH=nameDC.replace('X',str(numCM)).replace('H_99','H_0'+str(i+1)).replace('Mon','Set')
        nameDCV=nameDC.replace('X',str(numCM)).replace('H_99','V_0'+str(i+1)).replace('Mon','Set')
        #caput(nameDCH,iDCH[i-idBPMStart])
        #caput(nameDCV,iDCH[i-idBPMStart])
        print nameDCH
        print nameDCV
        

def TimeSleep(iRec,stepFreshGen,timeSleep,timeDead=15):
    if iRec % stepFreshGen==0:
        time.sleep(timeDead)
        time.sleep(timeSleep)

def GetSolenoidCurren(numDC,numCM=1):
    iSolen=[]
    for i in range(numDC):
        nameSol=nameS.replace('X',str(numCM)).replace('99','0'+str(i+1))
        iSolenTmp=np.random.random()   # iSolenTmp=caget(nameSol)
        iSolen.append(iSolenTmp)
    return iSolen
    
    
def CheckSolenoid(iSolen,numDC,numCM=1):
    if iRec==0:
        iSolen_0=GetSolenoidCurren(numDC,numCM)
    else:
        iSolen_0=iSolen
    iSolen=GetSolenoidCurren(numDC,numCM)
    
    flagSolen=0
    for i in range(numDC):
        if np.abs(iSolen[i]-iSolen_0[i])>3:
            print "Sol: "+str(i+1)
            print iRec
            flagSolen=1 
    return flagSolen

def STR(iDCHPut):
    str_iDCHPut=str(np.round(np.array(iDCHPut)*100.)/100.)[1:-1].strip().replace('\n',' ').replace(',',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ')+' '
    return str_iDCHPut

argMin=-65
argMax=65
argAmp=10

numDC=5
numCM=1
idBPMStart=5
idBPMEnd=10

stepFreshGen=50
timeSleep=0.5

testFlagCheckBeamCurrent=1
testFlagSolen=1
testFlagCheckDCCurrent=1
testFlagCheckBPM=1
testGetACCT3=1

nameS='HCMX_PS:SOL_99:IMon'
nameDC='HCMX_PS:DCH_99:IMon'
nameBPM='BPM:0-X11'


now2Write=time.asctime().replace('  ',' ').replace(' ','_')[4::]
nameRec='Rec_'+now2Write+'.dat'

iRec=0
with open(nameRec,'a+') as fid:
    while True:


        acct1,acct2,acct3,fc2=GetBeamCurrent()
        flagCheckBeamCurrent=CheckBeamCurrent(acct1,acct2,acct3,fc2)
        if flagCheckBeamCurrent==1 and testFlagCheckBeamCurrent==1:
            pass            #continue

        iSolen=GetSolenoidCurren(numDC,numCM)
        flagSolen=CheckSolenoid(iSolen,numDC,numCM)
        if flagSolen==1 and testFlagSolen==1:
            pass            #continue
                
        
        

        flagCheckDCCurrent=CheckDCCurrent(iRec,numDC)
        if flagCheckDCCurrent==1 and testFlagCheckDCCurrent==1:
            iDCH,iDCV = GenDCHCrruent(iRec,stepFreshGen,numDC,argMin,argMax,argAmp)
            PutDCH(iDCH,iDCV,idBPMStart=5,idBPMEnd=10,numCM=1)
            TimeSleep(iRec,stepFreshGen,timeSleep)
            #continue

        flagCheckBPM=CheckBPM(iRec,idBPMStart,idBPMEnd)
        if flagCheckBPM==1 and testFlagCheckBPM==1:
            iDCH,iDCV = GenDCHCrruent(iRec,stepFreshGen,numDC,argMin,argMax,argAmp)
            PutDCH(iDCH,iDCV,idBPMStart=5,idBPMEnd=10,numCM=1)
            TimeSleep(iRec,stepFreshGen,timeSleep)
            #continue
        
        
        iDCH,iDCV = GenDCHCrruent(iRec,stepFreshGen,numDC,argMin,argMax,argAmp)
        PutDCH(iDCH,iDCV,numDC,numCM=1)
        TimeSleep(iRec,stepFreshGen,timeSleep)
        
        if testGetACCT3==1:
            while GetACCT3()<1.:
                print "ACCT 3"
                time.sleep(0.55)
        
        
        acct3=GetACCT3()
        xBPM,yBPM =GetBPM(idBPMStart,idBPMEnd)
        iDCHPut,iDCVPut=iDCH,iDCV 
        iDCHGet,iDCVGet=GetDCCurrent(numDC,numCM=1)
        iSolenGet=GetSolenoidCurren(numDC,numCM)

        str_acct3,str_xBPM,str_yBPM,str_iDCHPut,str_iDCVPut, str_iDCHGet, str_iDCVGet, str_iSolenGet \
        =STR(acct3),STR(xBPM),STR(yBPM),STR(iDCHPut),STR(iDCVPut),STR(iDCHGet),STR(iDCVGet),STR(iSolenGet)

        strWrite=str_iDCHPut+str_iDCVPut+str_xBPM+str_yBPM+str_acct3+str_iDCHGet+str_iDCVGet+str_iSolenGet
        
        fid.writelines(strWrite+'\n')


        iRec+=1
        
        print iRec
        break




    
    














