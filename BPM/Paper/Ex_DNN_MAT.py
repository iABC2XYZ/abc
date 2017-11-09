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

bpm_x11_aim=[0,0,0,0,0]
bpm_y11_aim=[0,0,0,0,0]

flagAuto=2   # 如果　flagAuto=1，自动矫正到０；　
             #如果flagAuto=０,矫正的最后状态是　bpm_x11_aim　和　　bpm_y11_aim
             # 如果flagAuto=２,矫正的最后状态是　bpm_x11_aim　和　　bpm_y11_aim,但第一个ＢＰＭ不矫正。
             #　建议选择　０　或则　２

flagMethod='NN'  # DNN

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


def GetNow():
    xBpm,yBpm=GetBPM()
    xCHV,yCHV=GetCHV()
    return xBpm,yBpm,xCHV,yCHV


def GetMatRes(nameFile):
    M=np.loadtxt(nameFile)
    return M

def PreX(flagMethod,flagAuto,bpm_x11_aim,bpm_y11_aim):
    xBpm,yBpm=GetBPM()
    if flagAuto==1:
        d_bpm_x11_aim=-xBpm
        d_bpm_y11_aim=-yBpm
        d_bpm_x11_aim[0,0]=0
        d_bpm_y11_aim[0,0]=0
    elif flagAuto==0:
        d_bpm_x11_aim=bpm_x11_aim-xBpm
        d_bpm_y11_aim=bpm_y11_aim-yBpm
    elif flagAuto==2:
        d_bpm_x11_aim=bpm_x11_aim-xBpm
        d_bpm_y11_aim=bpm_y11_aim-yBpm
        d_bpm_x11_aim[0,0]=0
        d_bpm_y11_aim[0,0]=0
                
    
    if flagMethod.lower()=='nn':
        X=np.hstack((d_bpm_x11_aim,d_bpm_y11_aim))
        nameFile_M='w_NN.dat'
    elif flagMethod.lower()=='dnn':
        X1=np.hstack((xBpm,yBpm))
        X2=np.hstack((d_bpm_x11_aim,d_bpm_y11_aim))
        X=np.hstack((X1,X2))
        nameFile_M='w_DNN.dat'
    M=GetMatRes(nameFile_M)

    return X,M
##

def CalCHV(X,M):
    d_CHV=np.matmul(X,M)
    d_xCHV=d_CHV[0,0:7]
    d_yCHV=d_CHV[0,7::]
    return d_xCHV,d_yCHV

def CheckCHV(d_xCHV,d_yCHV,boundMin=-15,boundMax=15):
    d_xCHV[np.where(d_xCHV>boundMax)]=boundMax
    d_xCHV[np.where(d_xCHV<boundMin)]=boundMin
    d_yCHV[np.where(d_yCHV>boundMax)]=boundMax
    d_yCHV[np.where(d_yCHV<boundMin)]=boundMin
    return d_xCHV,d_yCHV

def PreY(X,M):
    d_xCHV,d_yCHV=CalCHV(X,M)
    d_xCHV,d_yCHV=CheckCHV(d_xCHV,d_yCHV)
    xCHV,yCHV=GetCHV()
    xCHV+=d_xCHV
    yCHV+=d_yCHV
    return xCHV,yCHV

##

def PutY(xCHV,yCHV):
    for iCHV in range(7):
        nameXCHV='MEBT_PS:DCV_0'+str(iCHV+1)+':ISet'
        nameYCHV='MEBT_PS:DCV_0'+str(iCHV+1)+':ISet'
        #caput(nameXCHV,xCHV[iCHV])                ##   !
        #caput(nameYCHV,yCHV[iCHV])                ##   !

    

def Run():
    X,M=PreX(flagMethod,flagAuto,bpm_x11_aim,bpm_y11_aim)
    xCHV,yCHV=PreY(X,M)
    PutY(xCHV,yCHV)
    

def Write(fid):
    now2Write=time.asctime()
    fid.writelines('#'+now2Write+' xBpm,yBpm,xCHV,yCHV '+'\n')
    
    xBpm,yBpm,xCHV,yCHV=GetNow()
    fid.writelines(str(np.round(xBpm*100)/100)[2:-2]+'\n')
    fid.writelines(str(np.round(yBpm*100)/100)[2:-2]+'\n')
    fid.writelines(str(np.round(xCHV*100)/100)[2:-2]+'\n')
    fid.writelines(str(np.round(yCHV*100)/100)[2:-2]+'\n')   
    



with open('log','a+') as fid:
    Write(fid)    
    Run()    
    time.sleep(0.13)                             #   !!    
    Write(fid)
    fid.writelines('='*32)



















