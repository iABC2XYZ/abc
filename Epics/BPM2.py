#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:00:15 2017

@author: p
"""


import numpy as np

from epics import caget, caput

import time

now = int(time.time())
timeArray = time.localtime(now)
nowClock= time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
nameNowClock=nowClock[5:7]+nowClock[8:10]+'_'+nowClock[11:13]+nowClock[14:16]

# 设置随机数
    
numISet=21
ISet=np.linspace(-15,15,numISet)

RecName='RecScan_'+nameNowClock+'.dat'
with open(RecName,'w+') as fid:
    for iQ in range(14):
        iPut=np.zeros((14))
        for iI in xrange(numISet):
            iPut[iQ]=ISet[iI]
            
            for jQ in range(14):        
                if iQ<7:
                    name='MEBT_PS:DCH_0'+str(iQ+1)+':ISet'
                else:
                    name='MEBT_PS:DCV_0'+str(iQ+1-7)+':ISet'
                caput(name,iPut[jQ])
                #print name,iPut[jQ]
                #fid.writelines(str((name,iPut[jQ]))+'\n')
            time.sleep(2.8)
            
            xBpm=np.zeros((5))
            yBpm=np.zeros((5))
            
            for iBPM in range(5):
                nameXBPM='BPM:'+str(iBPM+1)+'-X11'
                nameYBPM='BPM:'+str(iBPM+1)+'-Y11'
                
                xBpm[iBPM]=caget(nameXBPM)
                yBpm[iBPM]=caget(nameYBPM)
            
                #xBpm[iBPM]=np.random.random()
                #yBpm[iBPM]=np.random.random()  
    
            iPutStr=str(iPut).replace("\n",' ')[1:-1:]+' '
            xBpmStr=str(xBpm).replace("\n",' ')[1:-1:]+' '
            yBpmStr=str(yBpm).replace("\n",' ')[1:-1:]+' '
            
            fid.writelines(iPutStr+xBpmStr+yBpmStr)
            fid.writelines('\n')
    
    
    
    




