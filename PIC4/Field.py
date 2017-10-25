#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""

import numpy as np

from Input import *

numPart=np.int64(numPart)

def FieldAdd(exEx,exEy,exEz,exBx,exBy,exBz,inEx,inEy,inEz,inBx,inBy,inBz):

    Ex=exEx+inEx
    Ey=exEy+inEy
    Ez=exEz+inEz
    
    Bx=exBx+inBx
    By=exBy+inBy
    Bz=exBz+inBz   

    return Ex,Ey,Ez,Bx,By,Bz



def FieldInter_2D(beamEnergyMain,X,Y,Z,QReal,xMin,xMax,yMin,yMax,xGrid,yGrid):
    inEx,inEy,inBx,inBy=0.,0.,0.,0.
    return inEx,inEy,inBx,inBy

def FieldInter_3D(beamEnergyMain,X,Y,Z,QReal,xMin,xMax,yMin,yMax,zMin,zMax,xGrid,yGrid,zGrid):
    inEx,inEy,inEz,inBx,inBy,inBz=0.,0.,0.,0.,0.,0.
    return inEx,inEy,inEz,inBx,inBy,inBz

def FieldExtern_Drift():
    exEx,exEy,exEz,exBx,exBy,exBz=0.,0.,0.,0.,0.,0.
    return exEx,exEy,exEz,exBx,exBy,exBz
    

def FieldExtern(idEle):
    exEx,exEy,exEz,exBx,exBy,exBz=0.,0.,0.,0.,0.,0.
    return exEx,exEy,exEz,exBx,exBy,exBz


def FieldExtern_AllPart(idEle):
    eleType=eval('ele_'+str(idEle)).lower()
    if eleType[:3:]=='dri':
        exEx,exEy,exEz,exBx,exBy,exBz=np.array([0]),np.array([0]),np.array([0]),np.array([0]),np.array([0]),np.array([0])
    if eleType[:3:]=='rfq':
        exEx,exEy,exEz,exBx,exBy,exBz=np.zeros([numPart,1]),np.zeros([numPart,1]),np.zeros([numPart,1]),np.zeros([numPart,1]),np.zeros([numPart,1]),np.zeros([numPart,1])

        pass
    if eleType[:3:]=='emf':
        exEx,exEy,exEz,exBx,exBy,exBz=np.zeros([numPart,1]),np.zeros([numPart,1]),np.zeros([numPart,1]),np.zeros([numPart,1]),np.zeros([numPart,1]),np.zeros([numPart,1])

        pass
    
    
    
         
    return exEx,exEy,exEz,exBx,exBy,exBz





   