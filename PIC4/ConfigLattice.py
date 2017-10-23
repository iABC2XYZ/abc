#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""

from ConfigInput import X,PX,Y,PY,Z,PZ,Q,M,QReal,freq

from Input import *

from Field import FieldAdd,FieldInter_2D,FieldInter_3D,FieldExtern_Drift

i=1
while vars().has_key('ele_'+str(i)) :i+=1
numEle=i-1

zBegin/=1000.    # m

for iEle in range(1,numEle+1):
    if eval('ele_'+str(iEle)).lower()=='drift':
        ele='drift'
               
    if eval('ele_'+str(iEle))=='EMField':
        ele='emfield'

        EMMod=eval('EMMod_'+str(iEle))
        EMFieldLoc=eval('EMFieldLoc_'+str(iEle))
    
    

    #----------------------------------------
    
    zStart=eval('zStart_'+str(iEle))/1000.
    zEnd=eval('zEnd_'+str(iEle))/1000.
    
    try : freq=eval('freqMHz_'+str(iEle))*1e6
    except: freq=freqMHzG*1e6
    try : dT=eval('dT_'+str(iEle))/freq  
    except: dT=dTG/freq  
    
    try : xMin=eval('xMin_'+str(iEle))/1000.   
    except: xMin=xMinG/1000.
    try : xMax=eval('xMax_'+str(iEle))/1000.   
    except: xMax=xMaxG/1000.
    try : yMin=eval('yMin_'+str(iEle))/1000.   
    except: yMin=yMinG/1000.
    try : yMax=eval('yMax_'+str(iEle))/1000.   
    except: yMax=yMaxG/1000.
    






    #-----------------------------------------
    
    if ele=='drift':
        exEx,exEy,exEz,exBx,exBy,exBz=FieldExtern_Drift()
        
        if spaceCharge=='2d':
            inEx,inEy,inBx,inBy=FieldInter_2D()
            inEz,inBz=0.,0.
        if spaceCharge=='3d':
            inEx,inEy,inEz,inBx,inBy,inBz=FieldInter_3D()
        
        Ex,Ey,Ez,Bx,By,Bz=FieldAdd(exEx,exEy,exEz,exBx,exBy,exBz,inEx,inEy,inEz,inBx,inBy,inBz)
        
    
        
        
        
        
    if ele=='emfield':
        pass
        





