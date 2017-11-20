#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:46:48 2017

@author: p
"""

from epics import caget,caput
import time
import numpy as np
import csv

import matplotlib.pyplot as plt

plt.close('all')

filenRec='log_'+time.asctime().replace(' __','_').replace(' ','_')[4:]
fid=open(filenRec,'a+')

fName='LIST.csv'

def CSV(fName):

    listCSV=csv.reader(file(fName,'rb'))
    
    iRec=0
    bpmListLib=[]
    
    mainMonListLib=[]
    
    psSetListLib=[]
    psMonListLib=[]
    
    psSetMaxLib=[]
    psSetMinLib=[]
    psSetAmpLib=[]
    
    #---#---#---#---
    bpmList=[]
    
    mainMonList=[]
    
    psSetList=[]
    psMonList=[]
    
    psSetMax=[]
    psSetMin=[]
    psSetAmp=[]
    
    #---#---#---#---
    
    for line in listCSV:
        if iRec==0:
            iRec+=1
            continue
        bpmListLib.append(line[1])
        if line[4][0] !='#':
            mainMonListLib.append(line[4])
        psSetListLib.append(line[7])
        psMonListLib.append(line[7].replace('Set','Mon'))
        psSetMaxLib.append(np.float32( line[8]))
        psSetMinLib.append(np.float32( line[9]))
        psSetAmpLib.append(np.float32( line[10]))
        
        if line[2]=='1':
            bpmList.append(line[1])
        if line[5]=='1':
            if line[4][0] !='#':
                mainMonList.append(line[4])
        if line[11]=='1':
            psSetList.append(line[7])
            psMonList.append(line[7].replace('Set','Mon'))
            psSetMax.append(np.float32( line[8]))
            psSetMin.append(np.float32( line[9]))
            psSetAmp.append(np.float32( line[10]))

    return bpmListLib, mainMonListLib, psSetListLib, psMonListLib, psSetMaxLib, psSetMinLib, psSetAmpLib,\
 bpmList, mainMonList, psSetList, psMonList, psSetMax, psSetMin, psSetAmp

bpmListLib, mainMonListLib, psSetListLib, psMonListLib, psSetMaxLib, psSetMinLib, psSetAmpLib,\
 bpmList, mainMonList, psSetList, psMonList, psSetMax, psSetMin, psSetAmp= CSV(fName)

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
    


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
iRec=-1
LogTitleWrite(fid,(bpmList,psSetList))

bpmCheck=GetBPM(bpmList)
CheckPS(iRec,psSetList,psMonList)
ReadWrite_ALL(fid,bpmList,psSetList,psMonList,mainMonList,psSetListLib,psMonListLib,mainMonListLib)



##
numFresh=30

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


































