#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 12:48:11 2017

@author: p
"""


import numpy as np

from epics import caget, caput

G1='LEBT_PS:SOL_01:ISet'
G2='LEBT_PS:SOL_02:ISet'

S1='LEBT_PS:DCV_01:ISet'
S2='LEBT_PS:DCV_01:ISet'
S3='LEBT_PS:DCV_01:ISet'
S4='LEBT_PS:DCV_01:ISet'


iTotal =0
while True:
    iTotal+=1
    print iTotal
    
    maxG=350.
    maxS=50.
    
    vG1,vG2=np.round(np.random.random((2))*maxG*100.)/100.
    vS1,vS2,Vs3,vS4=np.round(np.random.random((4))*maxS*100.)/100.
    
    





