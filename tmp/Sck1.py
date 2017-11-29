#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""


import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import tushare as ts
import shutil

plt.close('all')

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
        
        

    

def ReadHistDataIndex(indexCode,kindCode):
    
    fileName='./data/'+kindCode.lower()+'/'+indexCode+'.'+kindCode.lower()
    if(kindCode.lower()=='date'):
        if  not (os.path.exists(fileName)):
            return '3000-01-01'
        with open(fileName,'r') as fid:
            dataCodeTmp=fid.readlines()
        nDataCodeTmp=len(dataCodeTmp)
        dataCode=np.copy(dataCodeTmp)
        for nLine in xrange(nDataCodeTmp):
            dataCode[nLine]=dataCodeTmp[nDataCodeTmp-nLine-1]
    else:
        if  not (os.path.exists(fileName)):
            return [0]
        dataCode= np.loadtxt(fileName)
        if np.shape(dataCode)==():
            return [0]
        
        dataCode=np.flip(np.loadtxt(fileName),0)
              
    return dataCode
    

def ChooseOpen():
    idCode=ReadCodeIndex()
    n=0
    
    plt.figure('open')

    with open('chooseOpen','w') as fid:
        for indexCode in idCode:
            n+=1
            print(n)
            openCode=ReadHistDataIndex(indexCode,'open')
            meanOpenCode=np.mean(openCode)
            if len(openCode)<30:
                continue
            if openCode[-1]<meanOpenCode:
                continue
            if openCode[0]>openCode[-1]:
                continue
            
            if not os.path.exists('./figures'):
                os.mkdir('./figures')
            if not os.path.exists('./figures/open'):
                os.mkdir('./figures/open')
            
            figName='./figures/open/'+indexCode+'.jpg'
            plt.clf()
            plt.title(np.str(n)+' :  '+indexCode)
            plt.plot(openCode)
            plt.pause(0.1)
            plt.savefig(figName)
            
            fid.writelines(indexCode+'\n')
            

def GetIndexFromChoose(kindCode):
    fileName='choose'+kindCode[0].upper()+kindCode[1::].lower()
    with open(fileName,'r') as fid:
        idChoose=fid.readlines()
        for nIDChoose in xrange(len(idChoose)):
            idChoose[nIDChoose]=idChoose[nIDChoose].strip('\n')
        return idChoose

def ConfigDir(dirName):
    if not os.path.exists('./figures'):
        os.mkdir('./figures')

    if  os.path.exists('./figures/'+dirName):
        shutil.rmtree('./figures/'+dirName)
    os.mkdir('./figures/'+dirName)

def FigName(dirName,indexCode):
    fileName='./figures/'+dirName+'/'+indexCode+'.jpg'
    return fileName


###
def ChooseOpenLast():
    idOpenChosen=GetIndexFromChoose('open')
    with open('chooseOpenlast','w') as fid:
        for iIDOpenChosen in idOpenChosen:
            openCode=ReadHistDataIndex(iIDOpenChosen,'open')
            flagStay=0
            if len(openCode)<200:
                flagStay=1
            else:
                if openCode[-1]<np.mean(openCode[-1:-201:-1]):
                    continue
                else:
                    flagStay=1
            if flagStay==1:
                fid.writelines(iIDOpenChosen+'\n')
                    
            

def PlotInforD1(kindChoose,figureDir,contentDataCode='open',colorPlot='b'):
    idOpenChosen=GetIndexFromChoose(kindChoose)

    ConfigDir(figureDir)
    
    plt.figure(figureDir)
    for iIDOpenChosen in idOpenChosen:
        
        plt.clf()
        arg=ReadHistDataIndex(iIDOpenChosen,contentDataCode)
        
        plt.plot(arg,colorPlot)
        plt.title(iIDOpenChosen)
        
        figName=FigName(figureDir,iIDOpenChosen)
        plt.savefig(figName)
        
        plt.pause(0.1)

def PlotInforD2(kindChoose,figureDir,contentDataCode=['open','close'],colorPlot=['b','r']):
    idOpenChosen=GetIndexFromChoose(kindChoose)

    ConfigDir(figureDir)
    
    plt.figure(figureDir)
    for iIDOpenChosen in idOpenChosen:
        
        plt.clf()
        arg0=ReadHistDataIndex(iIDOpenChosen,contentDataCode[0])
        arg1=ReadHistDataIndex(iIDOpenChosen,contentDataCode[1])
        
        plt.hold
        plt.plot(arg0,colorPlot[0])
        plt.plot(arg1,colorPlot[1])
        
        plt.title(iIDOpenChosen)
        
        figName=FigName(figureDir,iIDOpenChosen)
        plt.savefig(figName)
        
        plt.pause(0.1)
        
        
def PlotInforD3(kindChoose,figureDir,contentDataCode=['ma5','ma10','ma20'],colorPlot=['b','r','g']):
    idOpenChosen=GetIndexFromChoose(kindChoose)

    ConfigDir(figureDir)
    
    plt.figure(figureDir)
    for iIDOpenChosen in idOpenChosen:
        
        plt.clf()
        arg0=ReadHistDataIndex(iIDOpenChosen,contentDataCode[0])
        arg1=ReadHistDataIndex(iIDOpenChosen,contentDataCode[1])
        arg2=ReadHistDataIndex(iIDOpenChosen,contentDataCode[2])
        
        plt.hold
        plt.plot(arg0,colorPlot[0])
        plt.plot(arg1,colorPlot[1])
        plt.plot(arg2,colorPlot[2])
        
        plt.title(iIDOpenChosen)
        
        figName=FigName(figureDir,iIDOpenChosen)
        plt.savefig(figName)
        
        plt.pause(0.1)

def PlotInforD4(kindChoose,figureDir,contentDataCode=['open','close','high','low'],colorPlot=['b','r','g','k']):
    idOpenChosen=GetIndexFromChoose(kindChoose)

    ConfigDir(figureDir)
    
    plt.figure(figureDir)
    for iIDOpenChosen in idOpenChosen:
        
        plt.clf()
        arg0=ReadHistDataIndex(iIDOpenChosen,contentDataCode[0])
        arg1=ReadHistDataIndex(iIDOpenChosen,contentDataCode[1])
        arg2=ReadHistDataIndex(iIDOpenChosen,contentDataCode[2])
        arg3=ReadHistDataIndex(iIDOpenChosen,contentDataCode[3])
        
        plt.hold
        plt.plot(arg0,colorPlot[0])
        plt.plot(arg1,colorPlot[1])
        plt.plot(arg2,colorPlot[2])
        plt.plot(arg3,colorPlot[3])
        
        plt.title(iIDOpenChosen)
        
        figName=FigName(figureDir,iIDOpenChosen)
        plt.savefig(figName)
        
        plt.pause(0.1)

def PlotInforDn(kindChoose,figureDir,contentDataCode=['open','close','high','low'],colorPlot=['b','r','g','k']):
    idOpenChosen=GetIndexFromChoose(kindChoose)

    ConfigDir(figureDir)
    
    plt.figure(figureDir)
    for iIDOpenChosen in idOpenChosen:
        
        plt.clf()
        plt.hold
        
        arg0=ReadHistDataIndex(iIDOpenChosen,contentDataCode[0])
        mArg0=len(arg0)
        nArg0=len(contentDataCode)
        
        arg=np.zeros([mArg0,nArg0])
        
        arg[:,0]=arg0
        for iArg  in xrange(1,nArg0):
            arg[:,iArg]=ReadHistDataIndex(iIDOpenChosen,contentDataCode[iArg])
              
        for iArg  in xrange(nArg0):
            plt.plot(arg[:,iArg],colorPlot[iArg])
            
        plt.title(iIDOpenChosen)
        
        figName=FigName(figureDir,iIDOpenChosen)
        plt.savefig(figName)
        
        plt.pause(0.1)

def ChooseTurnover():

    indexOpenLast= GetIndexFromChoose("openLast")
    meanTurnover=np.zeros(len(indexOpenLast))
    
    
    nIndecOpenLast=-1
    for iIndecOpenLast in indexOpenLast:
        nIndecOpenLast+=1
        turnoverCode=ReadHistDataIndex(iIndecOpenLast,'turnover')
        
        meanTurnover[nIndecOpenLast]=np.mean(turnoverCode)
        
    for iTurnover in xrange(len(meanTurnover)-1,0,-1):
        if meanTurnover[iTurnover]<3:
            indexOpenLast.pop(iTurnover)
            
    with open('chooseTurnover','w') as fid:
        for iIndecOpenLast in indexOpenLast:
            fid.writelines(iIndecOpenLast+'\n')
    

'''
def UpdateCodeIndex():    Get the index of all codes.
    
def ReadCodeIndex():      Read code index from "idCode.txt".

def UpdateHistDataCode():        Update all data ~~~

def ReadHistDataIndex(indexCode,kindCode):     Read history data from local disk.

def ChooseOpen():      choose code from open(all data)

def GetIndexFromChoose(kindCode):       Get code index form a choose file

def ConfigDir(dirName):         configure a dir

def FigName(dirName,indexCode):     Get a Fig name

def ChooseOpenLast():     Choose code from open(last 200 days)
                    
def PlotInforD1(kindChoose,figureDir,contentDataCode='open',colorPlot='b'):   Plot 1D

def PlotInforD2(kindChoose,figureDir,contentDataCode=['open','close'],colorPlot=['b','r']):     Plot 2D
        
def PlotInforD3(kindChoose,figureDir,contentDataCode=['ma5','ma10','ma20'],colorPlot=['b','r','g']):     Plot 3D

def PlotInforD4(kindChoose,figureDir,contentDataCode=['open','close','high','low'],colorPlot=['b','r','g','k']):    Plot 4D

def PlotInforDn(kindChoose,figureDir,contentDataCode=['open','close','high','low'],colorPlot=['b','r','g','k']):    Plot ND

def ChooseTurnover() : Choose codes from turnover

'''





flagUpdateHistDataCode=0

UpdateCodeIndex()
idCode=ReadCodeIndex()

if flagUpdateHistDataCode==1:
    UpdateHistDataCode()



'''
def ReadHistDataIndex(indexCode,kindCode):     Read history data from local disk.

def ChooseOpen():      choose code from open(all data)

def GetIndexFromChoose(kindCode):       Get code index form a choose file

def ConfigDir(dirName):         configure a dir

def FigName(dirName,indexCode):     Get a Fig name

def ChooseOpenLast():     Choose code from open(last 200 days)
                    
def PlotInforD1(kindChoose,figureDir,contentDataCode='open',colorPlot='b'):   Plot 1D

def PlotInforD2(kindChoose,figureDir,contentDataCode=['open','close'],colorPlot=['b','r']):     Plot 2D
        
def PlotInforD3(kindChoose,figureDir,contentDataCode=['ma5','ma10','ma20'],colorPlot=['b','r','g']):     Plot 3D

def PlotInforD4(kindChoose,figureDir,contentDataCode=['open','close','high','low'],colorPlot=['b','r','g','k']):    Plot 4D

def PlotInforDn(kindChoose,figureDir,contentDataCode=['open','close','high','low'],colorPlot=['b','r','g','k']):    Plot ND

def ChooseTurnover() : Choose codes from turnover

'''















