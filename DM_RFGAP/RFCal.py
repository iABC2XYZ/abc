#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 17:14:30 2017

@author: A
"""

from ConstPhysics import *
import tensorflow as tf

def CalWavelength(freqMHz):
    return tf.div(cLight,freqMHz*1.e6)


