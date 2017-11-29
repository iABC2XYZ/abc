#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""

import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import tushare as ts

dayUse=30
dayPre=10


dayCut=dayUse+dayPre



aTmp=ts.get_hist_data('000338')

print type(aTmp)

print aTmp.head(50)

print aTmp.index
print aTmp.values

bTmp=aTmp.values

print type(bTmp) 
print np.shape(bTmp)

cTmp=aTmp.open

print cTmp.values

print aTmp.open[1]


plt.plot(aTmp.open)

print(aTmp.shape)















