#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:46:48 2017

@author: p
"""

from epics import caget,caput
import time
import numpy as np

import matplotlib.pyplot as plt

plt.close('all')

filenRec='log_'+time.asctime().replace(' __','_').replace(' ','_')[4:]
fid=open(filenRec,'a+')

#  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,


useBPM=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]      #   32
usePS=[11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]   #  28


useMain=[1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]      # 18

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-


psSetListLib=['MEBT_PS:DCH_01:ISet','MEBT_PS:DCV_01:ISet', \
           'MEBT_PS:DCH_02:ISet','MEBT_PS:DCV_02:ISet', \
           'MEBT_PS:DCH_03:ISet','MEBT_PS:DCV_03:ISet', \
           'MEBT_PS:DCH_04:ISet','MEBT_PS:DCV_04:ISet', \
           'MEBT_PS:DCH_05:ISet','MEBT_PS:DCV_05:ISet', \
           'MEBT_PS:DCH_06:ISet','MEBT_PS:DCV_06:ISet', \
           'MEBT_PS:DCH_07:ISet','MEBT_PS:DCV_07:ISet', \
           'HCM1_PS:DCH_01:ISet','HCM1_PS:DCV_01:ISet', \
           'HCM1_PS:DCH_02:ISet','HCM1_PS:DCV_02:ISet', \
           'HCM1_PS:DCH_03:ISet','HCM1_PS:DCV_03:ISet', \
           'HCM1_PS:DCH_04:ISet','HCM1_PS:DCV_04:ISet', \
           'HCM1_PS:DCH_05:ISet','HCM1_PS:DCV_05:ISet', \
           'HCM1_PS:DCH_06:ISet','HCM1_PS:DCV_06:ISet', \
           'HCM2_PS:DCH_01:ISet','HCM2_PS:DCV_01:ISet', \
           'HCM2_PS:DCH_02:ISet','HCM2_PS:DCV_02:ISet', \
           'HCM2_PS:DCH_03:ISet','HCM2_PS:DCV_03:ISet', \
           'HCM2_PS:DCH_04:ISet','HCM2_PS:DCV_04:ISet', \
           'HCM2_PS:DCH_05:ISet','HCM2_PS:DCV_05:ISet', \
           'HCM2_PS:DCH_06:ISet','HCM2_PS:DCV_06:ISet', \
        ]

psMonListLib=[]
for iSet in psSetListLib:
    psMonListLib.append(iSet.replace('Set','Mon'))

bpmListLib=['BPM:1-X11','BPM:1-Y11',\
          'BPM:2-X11', 'BPM:2-Y11',\
         'BPM:3-X11','BPM:3-Y11',\
         'BPM:4-X11','BPM:4-Y11',\
         'BPM:5-X11','BPM:5-Y11',\
         'BPM:6-X11', 'BPM:6-Y11',\
         'BPM:7-X11','BPM:7-Y11',\
         'BPM:8-X11','BPM:8-Y11',\
         'BPM:9-X11','BPM:9-Y11',\
         'BPM:10-X11','BPM:10-Y11',\
         'BPM:11-X11','BPM:11-Y11',\
         'BPM:12-X11', 'BPM:12-Y11',\
         'BPM:13-X11','BPM:13-Y11',\
         'BPM:14-X11','BPM:14-Y11',\
         'BPM:15-X11','BPM:15-Y11',\
         'BPM:16-X11','BPM:16-Y11',\
         'BPM:17-X11','BPM:17-Y11',\
         ]

psSetMaxLib=[12,12,\
         12 ,12,\
         12 ,12,\
         12 ,12,\
         12 ,12,\
         12 ,12,\
         12 ,12,\
         35,50,\
         50,50,\
         50,50,\
         50,50,\
         50,50,\
         50,50,\
         50,50,\
         50,50,\
         50,50,\
         50,50,\
         50,50,\
         50,50,\
         ]

psSetMinLib=[-12,-12,\
         -12 ,-12,\
         -12 ,-12,\
         -12 ,-12,\
         -12 ,-12,\
         -12 ,-12,\
         -12 ,-12,\
         -35,-50,\
         -50,-50,\
         -50,-50,\
         -50,-50,\
         -50,-50,\
         -50,-50,\
         -50,-50,\
         -50,-50,\
         -50,-50,\
         -50,-50,\
         -50,-50,\
         -50,-50,\
         ]

psSetAmpLib=[7,7,\
         7 ,7,\
         7 ,7,\
         7 ,7,\
         7 ,7,\
         7 ,7,\
         7 ,7,\
         4,4,\
         4,4,\
         4,4,\
         4,4,\
         4,4,\
         4,4,\
         4,4,\
         4,4,\
         4,4,\
         4,4,\
         4,4,\
         4,4,\
         ]

####----

mainMonListLib=[\
           'MEBT_PS:QUAD_01:IMon',\
           'MEBT_PS:QUAD_02:IMon', \
           'MEBT_PS:QUAD_03:IMon', \
           'MEBT_PS:QUAD_04:IMon', \
           'MEBT_PS:QUAD_05:IMon', \
           'MEBT_PS:QUAD_06:IMon', \
           'MEBT_PS:QUAD_07:IMon', \
           'HCM1_PS:SOL_01:IMon', \
           'HCM1_PS:SOL_02:IMon', \
           'HCM1_PS:SOL_03:IMon', \
           'HCM1_PS:SOL_04:IMon', \
           'HCM1_PS:SOL_05:IMon', \
           'HCM1_PS:SOL_06:IMon', \
           'HCM2_PS:SOL_01:IMon', \
           'HCM2_PS:SOL_02:IMon', \
           'HCM2_PS:SOL_03:IMon', \
           'HCM2_PS:SOL_04:IMon', \
           'HCM2_PS:SOL_05:IMon', \
           'HCM2_PS:SOL_06:IMon' ,\
        ]

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-


def LogWrite(fid,(X)):
    for iX in X:
        try:
            for jX in iX:
                fid.writelines('%.2f ' %jX)
        except:
            fid.writelines('%.2f ' %iX)
    fid.writelines('\n')    
    
def LogTitleWrite(fid,(X)):
    for iX in X:
        for jX in iX:
            fid.writelines(jX+' ')
    fid.writelines('\n')    
    

## ----------------
def GetBPM(bpmList):
    bpmNow=[]
    for iBPM in bpmList:
        bpmNow.append(caget(iBPM))
    bpmNow=np.array(bpmNow)
    return bpmNow

def GetPS(psSetList):
    psNow=[]
    for iPS in psSetList:
        psNow.append(caget(iPS))
    psNow=np.array(psNow)
    return psNow

def Get_Check_Main_PS(mainMonList):
    psMainSet=GetPS(mainMonList)
    mainSetList=[]
    for i in mainMonList:
        mainSetList.append(i.replace('Mon','Set'))
    psMainMon=GetPS(mainSetList)
    
    d_Main=np.abs(psMainSet-psMainMon)
    idFalse=np.where(d_Main>5)[0]
    
    return psMainSet,psMainMon,idFalse

def CheckPS(iRec,psSetList,psMonList):
    while True:
        psSetNow=GetPS(psSetList)
        psMonNow=GetPS(psMonList)
        d_PS=np.abs(psSetNow-psMonNow)
        idFalse=np.where(d_PS>2)[0]
        if len(idFalse)>0:
            print  iRec
            for i in idFalse:
                print psSetList[i]
            time.sleep(1)
        if len(idFalse)==0:
            break
            
def CheckBPM(iRec,bpmCheck,bpmList):
    while True:
        bpmNow=GetBPM(bpmList)
        d_bpm=np.abs(bpmCheck-bpmNow)
        idFalse=np.where(d_bpm<1e-6)[0]
    
        print 'bpmNow'
        print bpmNow
        print 'd_bpm'
        print d_bpm
        print 'idFalse'
        print idFalse
        
        if len(idFalse)>0:
            print  iRec
            for i in idFalse:
                print '*'
                print i
                print psSetList[i]
            time.sleep(1)
        if len(idFalse)==0:
            break

    

def PutPS(psSetList,psSetNow):
    for i in range(len(psSetList)):
        iStr,iVal=psSetList[i],psSetNow[i]
        caput(iStr,iVal)

def Sleep(iRec,psSetList,psMonList):
    psSetNow=GetPS(psSetList)
    iPrint =0
    while True:
        iPrint+=1
        psMonNow= GetPS(psMonList)
        d_PS=np.abs(psSetNow-psMonNow)
    
        flag_PS=d_PS<2
        flag_PS_All=np.prod(flag_PS)
        time.sleep(1)
        
        if flag_PS_All==0:   #  With False
            idFalse=np.where( flag_PS==False)[0]
            if iPrint>=3:
                print iRec
                for i in idFalse:
                    print psMonList[i]
        if flag_PS_All==1:   # no False
            break
            

def PSGen(psSetMax,psSetMin):
    numPS=len(psSetMax)
    psCurrent=np.random.random((numPS))*(np.array(psSetMax)-np.array(psSetMin))+np.array(psSetMin)
    psCurrent=np.round(psCurrent*100)/100
    psFlag=np.sign(np.random.random((numPS))-0.5)
    return psCurrent,psFlag
    
def PSUpdate(psCurrent,psFlag,psSetAmp,psSetMax,psSetMin):
    numPS=len(psSetMax)
    psCurrentChange=np.random.random((numPS))*psSetAmp*psFlag
    psCurrentChange=np.round(psCurrentChange*100)/100
    
    psCurrent+=psCurrentChange
    
    arrPSSetMin=np.array(psSetMin)
    arrPSSetMax=np.array(psSetMax)
    
    psFlag[psCurrent<arrPSSetMin]=1
    psFlag[psCurrent>arrPSSetMax]=-1
    
    psCurrent[psCurrent<arrPSSetMin]=arrPSSetMin[psCurrent<arrPSSetMin]*2-psCurrent[psCurrent<arrPSSetMin]
    psCurrent[psCurrent>arrPSSetMax]=arrPSSetMax[psCurrent>arrPSSetMax]*2-psCurrent[psCurrent>arrPSSetMax]
    
    return psCurrent,psFlag


def CheckACCT3(iCut=1.):    #--------------------
    iACCT3=caget('ADS_SLIT_VALUE.CHAN6_VAL_M')
    acct3False=0
    if iACCT3<iCut:
        acct3False=1
    return iACCT3,acct3False


def ReadWrite(fid,bpmList,psSetList,psMonList,mainMonList):
    iACCT3,flagACCT3= CheckACCT3()
    psMainSet,psMainMon,idFalse=Get_Check_Main_PS(mainMonList)
    bpmNow=GetBPM(bpmList)
    psSetNow=GetPS(psSetList)
    psMonNow=GetPS(psMonList)
    
    LogWrite(fid,(bpmNow,psSetNow,psMonNow,psMainSet,psMainMon,iACCT3))
    

def GetPV(xList,xListLib):
    xNow=[]
    for i in xListLib:
        if i in xList:
            xNow.append(caget(i))
        else:
            xNow.append(0.00)
    xNow=np.array(xNow)
    return xNow

def ReadWrite_ALL(fid,bpmList,psSetList,psMonList,mainMonList,psSetListLib,psMonListLib,mainMonListLib):
    iACCT3,flagACCT3= CheckACCT3()
    psMainSet,psMainMon,idFalse=Get_Check_Main_PS(mainMonList)

    bpmNow4W=GetPV(bpmList,bpmListLib)
    psSetNow4W=GetPV(psSetList,psSetListLib)
    psMonNow4W=GetPV(psMonList,psMonListLib)
    psMainSet4W=GetPV(mainMonList,mainMonListLib)
    
    LogWrite(fid,(bpmNow4W,psSetNow4W,psMonNow4W,psMainSet4W,iACCT3))
    

mainMonList=[]
for iMain in useMain:
    mainMonList.append(mainMonListLib[iMain-1])

bpmList=[]
for iBPM in useBPM:
    bpmList.append(bpmListLib[iBPM-1])

psSetList=[]
psMonList=[]
psSetMax=[]
psSetMin=[]
psSetAmp=[]
for iPS in usePS:
    psSetList.append(psSetListLib[iPS-1])
    psMonList.append(psMonListLib[iPS-1])
    psSetMax.append(psSetMaxLib[iPS-1])
    psSetMin.append(psSetMinLib[iPS-1])
    psSetAmp.append(psSetAmpLib[iPS-1])

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
iRec=-1
LogTitleWrite(fid,(bpmList,psSetList))

bpmCheck=GetBPM(bpmList)
CheckPS(iRec,psSetList,psMonList)
ReadWrite_ALL(fid,bpmList,psSetList,psMonList,mainMonList,psSetListLib,psMonListLib,mainMonListLib)



##
numFresh=50

iRec=0
flagPut=1
while True:
    print iRec
    if iRec % numFresh==0:
         psSetNow,psFlag= PSGen(psSetMax,psSetMin)
    else:
         psSetNow,psFlag=PSUpdate(psSetNow,psFlag,psSetAmp,psSetMax,psSetMin)
    
    if flagPut==1:
        PutPS(psSetList,psSetNow)
    
    ##---
    psMainSet,psMainMon,idFalse=Get_Check_Main_PS(mainMonList)
    iACCT3,acct3False= CheckACCT3()
    if len(idFalse)>0:
        for i in idFalse:
            print mainMonList[i]
            flagPut=0
            time.sleep(1)
            continue
    if len(idFalse)==0:
        flagPut=1
        
    if acct3False==1:
        print 'ACCT3'
        flagPut=0
        time.sleep(1)
        continue        
    else:
        flagPut=1
    

    #CheckBPM(iRec,bpmCheck,bpmList)    WRONG !!!!!!
    
    
    ##--
    Sleep(iRec,psSetList,psMonList)
    CheckPS(iRec,psSetList,psMonList)
    
    ReadWrite_ALL(fid,bpmList,psSetList,psMonList,mainMonList,psSetListLib,psMonListLib,mainMonListLib)
    bpmCheck=GetBPM(bpmList)
    iRec+=1
    




fid.close()


































