#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:56:41 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
______________________________________________________


"""

import numpy as np
from InputBeam import energyInMeV,energyOutMeV
from InputLattice import numCav

xMin=np.float32(-20.)
xMax=np.float32(20.)

xpMin=np.float32(-20.)
xpMax=np.float32(20.)


yMin=np.float32(-20.)
yMax=np.float32(20.)

ypMin=np.float32(-20.)
ypMax=np.float32(20.)

phiMin=-np.pi
phiMax=np.pi*(np.float32(numCav)/2+1.)

energyMin=energyInMeV*0.95
energyMax=energyOutMeV*1.05





