#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 22:29:48 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    APF
______________________________________________________
    DEsign an APF

"""
from Map import Drift3D,RFGap3D
from RFGap import RFGap
from InputLattice import numCav

def APF(ETLMV,lenCellM,x,xp,y,yp,phi,energy):
    for iCav in range(numCav):
        lCell=lenCellM[iCav]
        ETLMVCell=ETLMV[iCav]
        K,dE=RFGap(ETLMVCell,phi,energy)
        
        x,xp,y,yp,phi,energy=Drift3D(lCell,x,xp,y,yp,phi,energy)
        x,xp,y,yp,pphihiPi,energy=RFGap3D(K,dE,x,xp,y,yp,phi,energy)

    lCell=lenCellM[iCav]
    x,xp,y,yp,phi,energy=Drift3D(lCell,x,xp,y,yp,phi,energy)
    
    return x,xp,y,yp,phi,energy








