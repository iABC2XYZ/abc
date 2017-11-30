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

fML_pre='ml.pre'
fidP=open(fML_pre,'w+')

fML_code='ml.code'
fidC=open(fML_code,'w+')



fML_train='ml_0.train'
fidT=open(fML_train,'w+')

fML_label='ml_0.label'
fidL=open(fML_label,'w+')

for iCode in codes:
    try:
        codeData=ts.get_hist_data(iCode)
    except:
        continue
    try:
        codeLen,codeWidth=codeData.shape
    except:
        continue
            
    
    if codeLen<dayCut:
        continue
    if codeWidth!=14:
        continue
    
    
    codeOpen=codeData.open.values
    codeClose=codeData.close.values
    codeHigh=codeData.high.values
    codeLow=codeData.low.values
    codeTurnover=codeData.turnover.values
    
    
    for iDayCut in xrange(codeLen-1,dayCut-2,-1):        
        
        for iDayUse in xrange(dayUse):
            idDayUse=iDayCut-iDayUse
            
            fidT.writelines('%.2f ' %codeOpen[idDayUse])
            fidT.writelines('%.2f ' %codeClose[idDayUse])
            fidT.writelines('%.2f ' %codeHigh[idDayUse])
            fidT.writelines('%.2f ' %codeLow[idDayUse])
            fidT.writelines('%.2f ' %codeTurnover[idDayUse])                
        
        for iDayPre in xrange(dayPre):
            idDayPre=iDayCut-dayUse-iDayPre
            fidL.writelines('%.2f ' %codeHigh[idDayPre])
        
        fidT.writelines('\n')
        fidL.writelines('\n')
        
        iLineCount+=1
        if iLineCount % 50000 ==0:
            fidT.close()
            fidL.close()
            
            iFid+=1
            
            fML_train_N=fML_train.replace('0',str(iFid))
            fML_label_N=fML_label.replace('0',str(iFid))
            
            fidT=open(fML_train_N,'w+')
            fidL=open(fML_label_N,'w+')
            
    
    
    for iPre in xrange(-dayUse,0):
        fidP.writelines('%.2f ' %codeOpen[iPre])
        fidP.writelines('%.2f ' %codeClose[iPre])
        fidP.writelines('%.2f ' %codeHigh[iPre])
        fidP.writelines('%.2f ' %codeLow[iPre])
        fidP.writelines('%.2f ' %codeTurnover[iPre])           
        
    fidP.writelines('\n')
    
    fidC.writelines(iCode+'\n')

    iCodeCount+=1
    
    
    print iCodeCount,iLineCount

fidT.close()
fidL.close()
fidP.close()
fidC.close()



