#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:35:32 2017

@author: p
"""

import numpy as np


xTmp=np.random.random((1,5))
yTmp=np.random.random((1,5))

print xTmp
print yTmp

print xTmp<yTmp

xTmp[xTmp<yTmp]=yTmp[xTmp<yTmp]
print xTmp

