#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 08:48:30 2017

@author: A
"""

import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import tushare as ts
import shutil



def ReadDataCode(indexCode,fileKind):
    fileName=indexCode+'.'+fileKind+'.txt'
    fileName='./HAHA/Parallel-Get-master/'+fileName     #
    if os.path.exists(fileName):
        return np.flip(np.loadtxt(fileName),0)
    else:
        return 0

def UpdateCodeIndex():
    basicStock=ts.get_stock_basics()
    indexBasicStock=basicStock.index
    with open('idCode.txt','w') as fid:
        for iIndexBasicStock in indexBasicStock:
            fid.writelines([iIndexBasicStock,'\n'])
    
def ReadCodeIndex():
    with open('idCode.txt','r') as fid:
        idCode=fid.readlines()
        for nIdCode in xrange(len(idCode)):
            idCode[nIdCode]=idCode[nIdCode].strip('\n')

    return idCode


def UpdateHistDataCode():
    idCode=ReadCodeIndex()
    if os.path.exists('data'):
        shutil.rmtree('data')
   
    os.mkdir('data')
    os.mkdir('data/date')
    os.mkdir('data/open')
    os.mkdir('data/high')
    os.mkdir('data/close')
    os.mkdir('data/low')
    os.mkdir('data/volume')
    os.mkdir('data/price_change')
    os.mkdir('data/p_change')
    os.mkdir('data/ma5')
    os.mkdir('data/ma10')
    os.mkdir('data/ma20')
    os.mkdir('data/v_ma10')
    os.mkdir('data/v_ma20')
    os.mkdir('data/turnover')

    nCount=1
    for iIdCode in idCode:
        nCount+=1
        print nCount
        dataCode=ts.get_hist_data(iIdCode)
        if dataCode is None:
            print "******************"
            continue

        fileDate='data/date/'+iIdCode+'.date'
        fileOpen='data/open/'+iIdCode+'.open'
        fileHigh='data/high/'+iIdCode+'.high'
        fileClose='data/close/'+iIdCode+'.close'
        fileLow='data/low/'+iIdCode+'.low'
        fileVolume='data/volume/'+iIdCode+'.volume'
        filePrice_change='data/price_change/'+iIdCode+'.price_change'
        fileP_change='data/p_change/'+iIdCode+'.p_change'
        fileMa5='data/ma5/'+iIdCode+'.ma5'
        fileMa10='data/ma10/'+iIdCode+'.ma10'
        fileV_ma10='data/v_ma10/'+iIdCode+'.v_ma10'
        fileV_ma20='data/v_ma20/'+iIdCode+'.v_ma20'
        fileMa20='data/ma20/'+iIdCode+'.ma20'
        fileTurnover='data/turnover/'+iIdCode+'.turnover'
        
        with open(fileDate,'w') as fid:
            for iDate in dataCode.index:
                fid.writelines(iDate)
                fid.writelines('\n')
        
        dataCode.open.to_csv(fileOpen,index=False)
        dataCode.high.to_csv(fileHigh,index=False)
        dataCode.close.to_csv(fileClose,index=False)
        dataCode.low.to_csv(fileLow,index=False)
        dataCode.volume.to_csv(fileVolume,index=False)
        dataCode.price_change.to_csv(filePrice_change,index=False)
        dataCode.p_change.to_csv(fileP_change,index=False)
        dataCode.ma5.to_csv(fileMa5,index=False)
        dataCode.ma10.to_csv(fileMa10,index=False)
        dataCode.ma20.to_csv(fileMa20,index=False)
        dataCode.v_ma10.to_csv(fileV_ma10,index=False)
        dataCode.v_ma20.to_csv(fileV_ma20,index=False)
        dataCode.turnover.to_csv(fileTurnover,index=False)
        
        
flagUpdateHist=0
if (flagUpdateHist==1):
    UpdateHistDataCode()
    

def ReadHistDataCode(indexCode,kindCode):
    
    fileName='./data/'+kindCode.lower()+'/'+indexCode+'.'+kindCode.lower()
    if(kindCode.lower()=='date'):
        with open(fileName,'r') as fid:
            dataCodeTmp=fid.readlines()
        nDataCodeTmp=len(dataCodeTmp)
        dataCode=np.copy(dataCodeTmp)
        for nLine in xrange(nDataCodeTmp):
            dataCode[nLine]=dataCodeTmp[nDataCodeTmp-nLine-1]
    else:   
    	dataCode=np.flip(np.loadtxt(fileName),0)
    
    return dataCode
    
idCode=ReadCodeIndex()

#print(idCode)

aa=ReadHistDataCode('300014','date')

print aa



