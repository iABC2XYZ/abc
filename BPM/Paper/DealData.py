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


nameFolder='/home/e/ABC/abc/BPM/Paper/'


nameData=nameFolder+'Rec_1106_2046.dat'
exData=np.loadtxt(nameData)

'''
for i in range(24):
    plt.figure(1)
    plt.clf()
    plt.plot(exData[:,i],'.')
    plt.title(i)
    plt.pause(1)
'''
'''
for i in range(10,24):
    plt.figure(1)
    plt.clf()
    plt.hist(exData[:,i],1000)
    plt.title(i)
    plt.pause(1)
'''


for i in range(0,24):
    print -np.mean(exData[:,i])


[-1.86408430966,1.56824205393,3.11142945232,3.86897583945,4.66700936151,1.38253433488,2.09661528113,1.15367116991,1.12618083973,2.16402881327]







