#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:46:06 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:


"""


import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np



def Quad4D(K):
    O=tf.constant([0.],shape=[1,1])
    I=tf.constant([1.],shape=[1,1])
    
    M_Col_1=tf.concat([I,K,O,O],0)

    M_Col_2=tf.concat([O,I,O,O],0)
    
    M_Col_3=tf.concat([O,O,I,K],0)
    
    M_Col_4=tf.concat([O,O,O,I],0)
    
    M=tf.concat([M_Col_1,M_Col_2,M_Col_3,M_Col_4],1)
    return M
    
def Drift4D(L):
    O=tf.constant([0.],shape=[1,1])
    I=tf.constant([1.],shape=[1,1])
    
    M_Col_1=tf.concat([I,O,O,O],0)
    M_Col_2=tf.concat([L,I,O,O],0)
    M_Col_3=tf.concat([O,O,I,O],0)
    M_Col_4=tf.concat([O,O,L,I],0)
    
    M=tf.concat([M_Col_1,M_Col_2,M_Col_3,M_Col_4],1)
    return M


def TwissO4D(alphaXO,betaXO,alphaYO,betaYO):
    
    O=tf.constant([0.],shape=[1,1])
    I=tf.constant([1.],shape=[1,1])
    betaX=tf.constant([betaXO],shape=[1,1])
    alphaX=tf.constant([alphaXO],shape=[1,1])
    betaY=tf.constant([betaYO],shape=[1,1])
    alphaY=tf.constant([alphaYO],shape=[1,1])    
    
    M_Col_1=tf.concat([I/tf.sqrt(betaX),alphaX/tf.sqrt(betaX),O,O],0)
    M_Col_2=tf.concat([O,tf.sqrt(betaX),O,O],0)
    M_Col_3=tf.concat([O,O,I/tf.sqrt(betaY),alphaY/tf.sqrt(betaY)],0)
    M_Col_4=tf.concat([O,O,O,tf.sqrt(betaY)],0)
    M=tf.concat([M_Col_1,M_Col_2,M_Col_3,M_Col_4],1)
    return M



