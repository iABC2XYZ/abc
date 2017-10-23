#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""

def FieldAdd(exEx,exEy,exEz,exBx,exBy,exBz,inEx,inEy,inEz,inBx,inBy,inBz):

    Ex=exEx+inEx
    Ey=exEy+inEy
    Ez=exEz+inEz
    
    Bx=exBx+inBx
    By=exBy+inBy
    Bz=exBz+inBz   

    return Ex,Ey,Ez,Bx,By,Bz



def FieldInter_2D():
    inEx,inEy,inBx,inBy=0.,0.,0.,0.
    return inEx,inEy,inBx,inBy

def FieldInter_3D():
    inEx,inEy,inEz,inBx,inBy,inBz=0.,0.,0.,0.,0.,0.
    return inEx,inEy,inEz,inBx,inBy,inBz

def FieldExtern_Drift():
    exEx,exEy,exEz,exBx,exBy,exBz=0.,0.,0.,0.,0.,0.
    return exEx,exEy,exEz,exBx,exBy,exBz
    



   