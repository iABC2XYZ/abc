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


bpms=exData[:,14:24]
bpmsMean=np.mean(bpms,axis=0)

d_bpm=bpms-bpmsMean


r_d_bpm=np.sum(np.square(d_bpm),axis=1)

idMin_r_d_bpm=np.ar




print np.shape(r_d_bpm)






