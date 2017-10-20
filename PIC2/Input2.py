#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 09:39:41 2017

@author: e
"""



# Beam -------------------------------------------
numBeam=3
freqMHz=162.5

beamName=['proton','C2+','H-1']
beamState=['bunch','DC','DC']
beamDistribition=['GS','WB','KV']
beamShare=[0.8,0.13,0.07]

beamCharge=[1,2,-1]
beamMass=[1,6,1]
beamEnergy=[1,0.9,1.1]

emitNx=[1,1,1]
emitNy=[1,1,1]
emitNz=[1,1,1]           # emitZ DC 不读

alphaTx=[1,1,1]
alphaTy=[1,1,1]
alphaTz=[1,1,1]         # alphaZ DC  是长度占比于1个bl. >1 则等于1

betaTx=[1,1,1]
betaTy=[1,1,1]
betaTz=[1,1,1]          # betaZ DC   对应 dp_p

muTx=[0,0,0]
muTxp=[0,0,0]
muTy=[0,0,0]
muTyp=[0,0,0]
muTz=[0,0,0]
muTzp=[0,0,0]


# config -------------------------------------------
numPart=1e4

# mapField  -------------------------------------------
xGridLog,yGridLog,zGridLog=4,4,6
xMin,xMax=-14.,14    #mm
yMin,yMax=-14.,14    #mm



