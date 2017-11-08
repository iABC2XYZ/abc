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
import time
plt.close('all')

numCorrect=4

def GetBPM():
    xBpm=np.zeros((1,5))
    yBpm=np.zeros((1,5))
    for iBPM in range(5):
        nameXBPM='BPM:'+str(iBPM+1)+'-X11'
        nameYBPM='BPM:'+str(iBPM+1)+'-Y11'
        
        #xBpm[0,iBPM]+=caget(nameXBPM)                ##   !
        #yBpm[0,iBPM]+=caget(nameYBPM)                ##   !
        xBpm[0,iBPM]=np.random.random()
        yBpm[0,iBPM]=np.random.random()
    return xBpm,yBpm


def GetCHV():
    xCHV=np.zeros((1,7))
    yCHV=np.zeros((1,7))
    for iCHV in range(7):
        nameXCHV='MEBT_PS:DCV_0'+str(iCHV+1)+':ISet'
        nameYCHV='MEBT_PS:DCV_0'+str(iCHV+1)+':ISet'
        
        #xCHV[0,iCHV]+=caget(nameXCHV)                ##   !
        #yCHV[0,iCHV]+=caget(nameYCHV)                ##   !
        xCHV[0,iCHV]=np.random.random()
        yCHV[0,iCHV]=np.random.random()
    return xCHV,yCHV




def GetBPMChange():
    xBpm,yBpm=GetBPM()
    xBpmChange,yBpmChange=-xBpm,-yBpm
    xBpmChange[0,0]=0.
    yBpmChange[0,0]=0.
    changeBPM=np.hstack((xBpmChange,yBpmChange))
    return changeBPM

def PrePutCHV(d_CHV):
    xCHV,yCHV=GetCHV()
    oriCHV=np.hstack((xCHV,yCHV))
    iCHV=oriCHV+d_CHV
    return iCHV
    
def PutCHV(iCHV):
    xCHV=iCHV[0:7]
    yCHV=iCHV[7::]
    for iCHV in range(7):
        nameXCHV='MEBT_PS:DCV_0'+str(iCHV+1)+':ISet'
        nameYCHV='MEBT_PS:DCV_0'+str(iCHV+1)+':ISet'
        #caput(nameXCHV,xCHV[iCHV])                ##   !
        #caput(nameYCHV,yCHV[iCHV])                ##   !
        

def GetMatRes():
    M=np.loadtxt('w.dat')
    return M

def CheckCHV(yCHV):
    yCHV[np.where(yCHV>15)]=15.
    yCHV[np.where(yCHV<-15)]=-15.
    return yCHV





for iCorrect in xrange(numCorrect):
    d_xBPM=GetBPMChange()
    M=GetMatRes()
    d_CHV=np.matmul(d_xBPM,M)
    yCHVPre=PrePutCHV(d_CHV)
    yCHV=CheckCHV(yCHVPre)
    PutCHV(yCHV)
    
    time.sleep(0.12)                           ##    !
    d_xBPM_After=GetBPMChange()
    
    


    plt.figure('d: BPM')
    plt.plot(d_xBPM.T,'-*')
    
    plt.figure('R: ISET')
    plt.plot(yCHV.T,'-*')

    plt.figure('d After: BPM')
    plt.plot(d_xBPM_After.T,'-*')
    plt.pause(0.1)




