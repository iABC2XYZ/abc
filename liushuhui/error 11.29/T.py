#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""

import numpy as np

import re
fileList=['beam_001.out:2','beam_001.out:3','beam_003.out:3','beam_004.out:3']

for iList in fileList:
    nInternal=iList.find(':')
    iFile=iList[0:nInternal].strip()
    iCol=iList[nInternal+1:].strip()
    
    
    fid=open(iFile,'r')
    for iLine in fid:
        reFind = re.findall('[a-zA-Z]+', iLine)
        if len(reFind)>0:
            print iLine
            print "*"
        

    
















