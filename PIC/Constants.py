#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 16:55:57 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:


"""

import numpy as np
import Input
import sys

if Input.beamParticle.lower()=='proton':
    massMeV=938.275
else:
    massMeV=931.474

pi=np.pi

c=299792458.


