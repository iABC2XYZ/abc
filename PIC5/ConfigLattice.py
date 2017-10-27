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
from Field import FieldExtern_AllPart

from Windows import WindowDef,WindowInner,WindowLeft,WindowRight

import numpy as np

numPart=np.int64(numPart)

i=1
while vars().has_key('ele_'+str(i)) :i+=1
numEle=i-1


EleType=[]
EleStart=np.zeros(numEle)
EleEnd=np.zeros(numEle)

for iEle in range(1,numEle+1):
    EleType.append(eval('ele_'+str(iEle)).lower())
    EleStart[iEle-1]=eval('zStart_'+str(iEle))/1000.
    EleEnd[iEle-1]=eval('zEnd_'+str(iEle))/1000.



z0=zBegin/1000.
zOver=zFinish/1000.


if scStep==0:
    scDoor=0
else:
    scDoor=1


iScStep=0
beamEnergyMain=beamEnergy
while True:
    iScStep+=1
    
    startWindow,endWindow=WindowDef(z0,beamEnergy,freq)
    idInner=WindowInner(startWindow,endWindow,EleStart,EleEnd)
    idLeft=WindowLeft(startWindow,endWindow,EleStart,EleEnd)
    idRight=WindowRight(startWindow,endWindow,EleStart,EleEnd)
    
    if idInner[0]!=0:          # window 在某个场区内
        
        # 计算场
        Ex,Ey,Ez,Bx,By,Bz=np.zeros([numPart,1]),np.zeros([numPart,1]),np.zeros([numPart,1]), \
                             np.zeros([numPart,1]),np.zeros([numPart,1]),np.zeros([numPart,1])
        
        # 计算外场
        for idEle in idInner:
            exEx,exEy,exEz,exBx,exBy,exBz=FieldExtern_AllPart(idEle)
            Ex,Ey,Ez,Bx,By,Bz=FieldAdd(Ex,Ey,Ez,Bx,By,Bz,exEx,exEy,exEz,exBx,exBy,exBz)
            
            
        # 计算内场：
        xMin,xMax,yMin,yMax=-1e10,1e10,-1e10,1e10
        for idEle in idInner:
            try : xMinTmp=eval('xMin_'+str(idEle))/1000.   
            except: xMinTmp=xMinG/1000.
            try : xMaxTmp=eval('xMax_'+str(idEle))/1000.   
            except: xMaxTmp=xMaxG/1000.
            try : yMinTmp=eval('yMin_'+str(idEle))/1000.   
            except: yMinTmp=yMinG/1000.
            try : yMaxTmp=eval('yMax_'+str(idEle))/1000.   
            except: yMaxTmp=yMaxG/1000.
            
            if np.abs(xMinTmp)<np.abs(xMin):
                xMin=xMinTmp
            if np.abs(xMaxTmp)<np.abs(xMax):
                xMax=xMaxTmp
            if np.abs(yMinTmp)<np.abs(yMin):
                yMin=yMinTmp
            if np.abs(yMaxTmp)<np.abs(yMax):
                yMax=yMaxTmp
                
        zMin,zMax=startWindow,endWindow
            
            
        
        if iSpaceChargeStep==spaceChargeStep:
            iSpaceChargeStep-=spaceChargeStep
            if spaceCharge.lower()=='3d':
                xGrid,yGrid,zGrid=2**xGridLog,2**yGridLog,2**zGridLog
                
                inEx,inEy,inEz,inBx,inBy,inBz=FieldInter_3D(beamEnergyMain,X,Y,Z,QReal,xMin,xMax,yMin,yMax,zMin,zMax,xGrid,yGrid,zGrid)
                
                Ex,Ey,Ez,Bx,By,Bz=FieldAdd(Ex,Ey,Ez,Bx,By,Bz,inEx,inEy,inEz,inBx,inBy,inBz)
            if spaceCharge.lower()=='2d':
                xGrid,yGrid=2**xGridLog,2**yGridLog
                
                inEx,inEy,inEz,inBx=FieldInter_2D(beamEnergyMain,X,Y,Z,QReal,xMin,xMax,yMin,yMax,xGrid,yGrid)
                
                Ex,Ey,Bx,By=FieldAdd(Ex,Ey,Bx,By,inEx,inEy,inBx,inBy)

        
        try : freq=eval('freqMHz_'+str(iEle))*1e6
        except: freq=freqMHzG*1e6
        try : dT=eval('dT_'+str(iEle))/freq  
        except: dT=dTG/freq  
            
        
            
        
            
        
            
            
        
            
            
  


 
    if (idLeft[0]!=0) or (idRight[0]!=0):     # window 在厂区边界上
        print 'B1'
        pass
    

    z0+=0.1
    if z0>zOver:
        break
    



        
        
'''

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
        
'''




