#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 14:49:20 2017

@author: p
"""

from epics import caget,caput
import time
import numpy as np

import tensorflow as tf

import matplotlib.pyplot as plt

plt.close('all')

def GenWeight(shape):
    initial = tf.truncated_normal(shape, stddev=1.)
    return tf.Variable(initial)
def GenBias(shape):
    initial = tf.constant(1., shape=shape)
    return tf.Variable(initial)























