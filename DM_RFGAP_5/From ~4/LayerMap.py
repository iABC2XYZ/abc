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
from ActionFunction import MyAct,MyZoomOut,MyZoomIn


def LayerMap(x,xp,y,yp,phi,energy,ETLMV,lenCellM,LastCellLen=0):
    x,xp,y,yp,phi,energy=MyZoomOut(x,xp,y,yp,phi,energy)
    
    K,dE=RFGap(ETLMV,phi,energy)
    x,xp,y,yp,phi,energy=Drift3D(lenCellM,x,xp,y,yp,phi,energy)
    x,xp,y,yp,phi,energy=RFGap3D(K,dE,x,xp,y,yp,phi,energy)
    if LastCellLen!=0:
        x,xp,y,yp,phi,energy=Drift3D(LastCellLen,x,xp,y,yp,phi,energy)
        
    
    
    x,xp,y,yp,phi,energy=MyAct(x,xp,y,yp,phi,energy)
    x,xp,y,yp,phi,energy=MyZoomIn(x,xp,y,yp,phi,energy)
    
    return x,xp,y,yp,phi,energy









