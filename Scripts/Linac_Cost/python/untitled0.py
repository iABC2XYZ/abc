#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 17:02:46 2017

@author: a
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

Eacc=np.arange(10,15,0.1)
plt.plot(Eacc,np.exp(Eacc-10)/20)


