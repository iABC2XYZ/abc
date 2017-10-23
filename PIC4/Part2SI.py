#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 15:22:28 2017

@author: e
"""
from RegFn import MM2M_6,MM2M_4
from BetaGammaC import NP_Energy2BetaGammaC

def Bunched2SI(energyMeV,x,xp,y,yp,z,zp):
    x,xp,y,yp,z,zp=MM2M_6(x,xp,y,yp,z,zp)    #   m m m rad rad rad
    p0=NP_Energy2BetaGammaC(energyMeV)
    pz=p0*(1.+zp)               # bg
    px=xp/pz                    # bg
    py=yp/pz                    # bg
    return x,px,y,py,z,pz

def Coasting2SI(energyMeV,x,xp,y,yp,z,zp):
    x,xp,y,yp=MM2M_4(x,xp,y,yp)      # m m rad rad
    p0=NP_Energy2BetaGammaC(energyMeV)
    pz=p0*(1.+zp)               # bg
    px=xp/pz                    # bg
    py=yp/pz                    # bg
    return x,px,y,py,z,pz

