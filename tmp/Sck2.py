#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tushare as ts


dayUse=30
dayPre=10
flagUpdate=1


dayCut=dayUse+dayPre
if flagUpdate==1:
    allToday=ts.get_today_all()

codes=allToday.code.values


iCodeCount=0
iLineCount=0
iFid=0

fML='dataML_0'
fid=open(fML,'w+')
for iCode in codes:
    try:
        codeData=ts.get_hist_data(iCode)
    except:
        continue
    codeLen,codeWidth=codeData.shape
    
    if codeLen<dayCut:
        continue
    if codeWidth!=14:
        continue
        
    codeOpen=codeData.open.values
    codeClose=codeData.close.values
    codeHigh=codeData.high.values
    codeLow=codeData.low.values
    codeTurnover=codeData.turnover.values
    
    
    for iDayCut in xrange(codeLen-dayCut):
        for iDayUse in xrange(dayUse):
            idDayUse=iDayCut+iDayUse
            
            fid.writelines('%.2f ' %codeOpen[idDayUse])
            fid.writelines('%.2f ' %codeClose[idDayUse])
            fid.writelines('%.2f ' %codeHigh[idDayUse])
            fid.writelines('%.2f ' %codeLow[idDayUse])
            fid.writelines('%.2f ' %codeTurnover[idDayUse])
        
        for iDayPre in xrange(dayPre):
            idDayPre=iDayCut+iDayUse+iDayPre
            fid.writelines('%.2f ' %codeHigh[idDayPre])
            
        fid.writelines('\n')
        iLineCount+=1
        if iLineCount % 50000 ==0:
            fid.close()
            iFid+=1
            fML_N=fML.replace('0',str(iFid))
            fid=open(fML_N,'w+')
            
            

    iCodeCount+=1
    
    print iCodeCount,iLineCount

fid.close()






