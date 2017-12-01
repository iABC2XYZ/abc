#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""

import numpy as np
import matplotlib.pyplot as plt

#
#fileList是文件＋Ｘ＋Ｙ的组合。例如　'beam_001.out:３,6'，表示beam_001.out文件，第三列是ｘ作为ｘ，第６列作为ｙ进行画图。
#在缺省的情况下，为０．例如：'beam_001.out:,6'表示Ｘ＝０，Ｙ为第６列。　　'beam_001.out:6,'表示Ｙ＝０，Ｘ为第６列。　
fileList=['beam_001.out:,6','beam_001.out:,4','beam_003.out:,3','beam_004.out:,4']

#nameFigure为画板的名字
nameFigure='Test'
#是否画Ｘ方向的数据。如果不画，Ｘ使用默认的０，１,2,3,4,...自然数列
PlotX=False  # True


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-


plt.figure(nameFigure)
plt.clf()
for iList in fileList:
    nInternal=iList.find(':')
    iFile=iList[0:nInternal].strip()
    iCol=iList[nInternal+1:].strip()
    
    
    nInternal=iCol.find(',')
    iColX=iCol[0:nInternal].strip()
    iColY=iCol[1+nInternal:].strip()
    
    
    iRead=0
    fid=open(iFile,'r')
    X=[]
    Y=[]
    for iLine in fid:
        iRead+=1
        
        if iRead==1:
            continue
        sLine=iLine.split()
        
        if iColX=='':
            X.append(0.)
        else:
            xTmp=np.float32(sLine[np.int32(iColX)+1])
            X.append(xTmp)
        
        if iColY=='':
            Y.append(0.)
        else:
            yTmp=np.float32(sLine[np.int32(iColY)+1])
            Y.append(yTmp)        
    
    
    plt.figure(nameFigure)
    plt.hold
    if PlotX:
        plt.plot(X,Y)
    else:
        plt.plot(Y)
    













