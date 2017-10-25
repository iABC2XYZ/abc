#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""

import numpy as np
from BetaGammaC import NP_Energy2BetaLambdaM

def WindowDef(z0,energyMeV,freq):
    betaLambdaM=NP_Energy2BetaLambdaM(energyMeV,freq)
    startWindow=z0-betaLambdaM/2.
    endWindow=z0+betaLambdaM/2.
    return startWindow,endWindow

def WindowInner(startWindow,endWindow,EleStart,EleEnd):
    flagStart=startWindow>EleStart
    flagEnd=endWindow<EleEnd
    flagCross=flagStart*flagEnd
    idInsection=np.argwhere(flagCross==1)+1
    
    if len(idInsection)==0:
        idInsection=np.array([0])
    else:
        idInsection=idInsection[:,0]

    return idInsection


def WindowLeft(startWindow,endWindow,EleStart,EleEnd):
    flagStart=startWindow<EleStart
    flagEnd=endWindow>EleStart
    
    flagCross=flagStart*flagEnd
    idInsection=np.argwhere(flagCross==1)+1

    if len(idInsection)==0:
        idInsection=np.array([0])
    else:
        idInsection=idInsection[:,0]

    return idInsection

def WindowRight(startWindow,endWindow,EleStart,EleEnd):
    flagStart=startWindow<EleEnd
    flagEnd=endWindow>EleEnd
    
    flagCross=flagStart*flagEnd
    idInsection=np.argwhere(flagCross==1)+1

    if len(idInsection)==0:
        idInsection=np.array([0])
    else:
        idInsection=idInsection[:,0]

    return idInsection








