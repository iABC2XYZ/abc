#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:08:06 2017

@author: p
"""

import tensorflow as tf
from tensorflow import fft

def Dst(a):
    a= tf.constant([[1,2,3,4],[3,4,5,6]],dtype=tf.float32)
    
    aShape=tf.shape(a)
    
    n=aShape[0]
    
    a3=tf.expand_dims(a,axis=0)
    
    aUD=tf.image.flip_left_right(a3)
    aUD_Neg=tf.constant([-1],dtype=tf.float32)*aUD[0]
    
    y=tf.concat((a,aUD_Neg),0)
    
    oneYImag=tf.constant([0.],dtype=tf.float32,shape=(4,4))
    yComplex=tf.complex(y,oneYImag)
    
    yy=fft(yComplex)
    
    b=yy[1:n+1,:]/(-2.*tf.sqrt(tf.constant((-1.),dtype=tf.complex64)))
    
    realB=tf.real(b)
    return realB



