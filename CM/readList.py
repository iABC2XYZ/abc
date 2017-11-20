#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 02:05:26 2017

@author: p
"""

import csv
import numpy as np



fName='LIST.csv'

def CSV(fName):

    listCSV=csv.reader(file(fName,'rb'))
    
    iRec=0
    bpmListLib=[]
    
    mainMonListLib=[]
    
    psSetListLib=[]
    psMonListLib=[]
    
    psSetMaxLib=[]
    psSetMinLib=[]
    psSetAmpLib=[]
    
    #---#---#---#---
    bpmList=[]
    
    mainMonList=[]
    
    psSetList=[]
    psMonList=[]
    
    psSetMax=[]
    psSetMin=[]
    psSetAmp=[]
    
    #---#---#---#---
    
    for line in listCSV:
        if iRec==0:
            iRec+=1
            continue
        bpmListLib.append(line[1])
        if line[4][0] !='#':
            mainMonListLib.append(line[4])
        psSetListLib.append(line[7])
        psMonListLib.append(line[7].replace('Set','Mon'))
        psSetMaxLib.append(np.float32( line[8]))
        psSetMinLib.append(np.float32( line[9]))
        psSetAmpLib.append(np.float32( line[10]))
        
        if line[2]=='1':
            bpmList.append(line[1])
        if line[5]=='1':
            if line[4][0] !='#':
                mainMonList.append(line[4])
        if line[11]=='1':
            psSetList.append(line[7])
            psMonList.append(line[7].replace('Set','Mon'))
            psSetMax.append(np.float32( line[8]))
            psSetMin.append(np.float32( line[9]))
            psSetAmp.append(np.float32( line[10]))

    return bpmListLib, mainMonListLib, psSetListLib, psMonListLib, psSetMaxLib, psSetMinLib, psSetAmpLib,\
 bpmList, mainMonList, psSetList, psMonList, psSetMax, psSetMin, psSetAmp
    
    







