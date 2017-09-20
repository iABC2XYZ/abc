#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:55:55 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:


"""


import tensorflow as tf
import numpy as np

def TFLambdaR(e,a,b,g):
    a2_gb=(2.*a)**2+(g-b)**2
    a2_gb_R=tf.sqrt(a2_gb)
    g_b=g+b
    e2=2.*e
    
    lambda_1=(g_b-a2_gb_R)/e2
    lambda_2=(g_b+a2_gb_R)/e2
    
    lambda_1_R=tf.sqrt(lambda_1)
    lambda_2_R=tf.sqrt(lambda_2)
    
    
    Lambda_R=tf.diag([lambda_1_R[0],lambda_2_R[0]])
    Lmbda_R_T=tf.diag([1./lambda_1_R[0],1./lambda_2_R[0]])
    return Lambda_R, Lmbda_R_T

def TFOrthTrans(e,a,b,g):
    g_b=g-b
    a2_gb=(2.*a)**2+g_b**2
    a2_gb_R=tf.sqrt(a2_gb)
    
    B=g_b-a2_gb_R
    E=g_b+a2_gb_R
    
    B_2a=B**2+(2.*a)**2
    B_2a_R=tf.sqrt(B_2a)
    
    E_2a=E**2+(2.*a)**2
    E_2a_R=tf.sqrt(E_2a)
    
    C=B/B_2a_R
    D=2.*a/B_2a_R
    
    F=E/E_2a_R
    G=2.*a/E_2a_R
    
    
    P1=tf.expand_dims(tf.concat([C,D],0),1)
    P2=tf.expand_dims(tf.concat([F,G],0),1)
    P=tf.concat([P1,P2],1)
    P_I=tf.matrix_inverse(P)
 
    return P,P_I










