#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:18:39 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:


"""


import tensorflow as tf

def PartGen(numPart):
    x=tf.random_normal([numPart])
    xp=tf.random_normal([numPart])
    y=tf.random_normal([numPart])
    yp=tf.random_normal([numPart])
    z=tf.random_normal([numPart])
    zp=tf.random_normal([numPart])
    
    return x,xp,y,yp,z,zp



















