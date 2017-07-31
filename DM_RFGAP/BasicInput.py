#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:14:09 2017

@author: A
"""
import tensorflow as tf
import numpy as np

constEnergyInMeV=tf.constant([0.6])
constEnergyOutMeV=tf.constant([4.])
constFreqMHz=tf.constant([162.5])

constEmitN=tf.constant([1.,1.,1.])
numPart=np.int32(1e4)
numCav=np.int32(60)
energyInMeV=np.float32(0.6)
energyOutMeV=np.float32(4.)
massMeV=np.float32(938.274)


