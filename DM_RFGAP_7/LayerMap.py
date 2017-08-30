#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:46:03 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    LayerMap
______________________________________________________


"""

from Map import Drift3D,RFGap3D
from RFGap import RFGap
from ActionFunction import MyAct
import tensorflow as tf





def LayerMap(x,xp,y,yp,z,betaC,ETLMV,lenCellM,LastCellLen=0):    
    
    
    K,dBeta=RFGap(z,betaC,ETLMV)

    x,xp,y,yp,z,betaC=Drift3D(x,xp,y,yp,z,betaC,lenCellM)
    x,xp,y,yp,z,betaC=RFGap3D(x,xp,y,yp,z,betaC,K,dBeta)
    
    if LastCellLen!=0:
        x,xp,y,yp,z,betaC=Drift3D(x,xp,y,yp,z,betaC,LastCellLen)
        
    x,xp,y,yp,z,betaC,numPartLost=MyAct(x,xp,y,yp,z,betaC)

    
    return x,xp,y,yp,z,betaC,numPartLost









