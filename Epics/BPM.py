# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

from epics import caget, caput

import time


'''
MEBT_PS:DCH_01:ISet
BPM:1-X11
BPM:1-Y11
'''


NTotal=1e4
iTotal=0
nFresh=30
Amp=3.5

with open('Rec.dat','a+') as fid:
    while True:
        acct1=caget('ADS_SLIT_VALUE.CHAN4_VAL_M')
        if acct1<1.:
            print iTotal
            time.sleep(10)
            continue

        iTotal+=1
        if iTotal>NTotal:
            break
        print iTotal
        
	


        if iTotal % nFresh==1:
            cHV=np.round(np.random.random((14))*300-150)/10.
            flagHV=np.ones((14))*np.sign(np.random.random((14))-0.5)
        else:
            if iTotal % np.round(nFresh/4)==nFresh/8:
                flagHV=np.ones((14))*np.sign(np.random.random((14))-0.5)
            
            cHV+=np.random.random((14))*Amp*flagHV
            flagHV[cHV>15]=-1
            flagHV[cHV<-15]=1
            cHV[cHV>15]=30-cHV[cHV>15]
            cHV[cHV<-15]=-30-cHV[cHV<-15]
        
        cHV=np.round(cHV*100)/100
        
        for iCH in range(7):
            nameCH='MEBT_PS:DCH_0'+str(iCH+1)+':ISet'
            caput(nameCH,cHV[iCH])
            
        for iCV in range(7):
            nameCV='MEBT_PS:DCV_0'+str(iCV+1)+':ISet'
            caput(nameCV,cHV[iCV+7])    
        
        
        time.sleep(2)
        
        
        nAve=5
        xBpm=np.zeros((5))
        yBpm=np.zeros((5))
        
        for iAve in range(nAve):
            for iBPM in range(5):
                nameXBPM='BPM:'+str(iBPM+1)+'-X11'
                nameYBPM='BPM:'+str(iBPM+1)+'-Y11'
                
                xBpm[iBPM]+=caget(nameXBPM)
                yBpm[iBPM]+=caget(nameYBPM)
                
            time.sleep(.1)
            
        xBpm/=nAve
        yBpm/=nAve
    
    
        fid.writelines(str(cHV[::])[1:-1:]+'  '+str(np.round(xBpm*100.)/100)[1:-1:]+'  '+str(np.round(yBpm*100.)/100)[1:-1:]+'\n')
    
















