#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:10:51 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    Beam

"""

import tensorflow as tf
import numpy as np

numPart=np.int32(1e4)

energyInMeV=tf.constant([0.6])
energyOutMeV=tf.constant([4.])

nEmitTInput=tf.constant([0.1,0.1,0.1])

qParticle=tf.constant([1.])
mParticle=tf.constant([1.])

massMeV=tf.constant(938.274)






