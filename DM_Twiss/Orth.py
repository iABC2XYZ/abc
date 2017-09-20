#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:41:05 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:


"""

import numpy as np


def LambdaR(e,a,b,g):
    arg_2agb=(2.*a)**2+(g-b)**2
    arg_2agb_R=np.sqrt(arg_2agb)
    arg_gb=g+b
    arg_2e=2.*e
    
    lambda_1=(arg_gb-arg_2agb_R)/arg_2e
    lambda_2=(arg_gb+arg_2agb_R)/arg_2e
    
    lambda_1_R=np.sqrt(lambda_1)
    lambda_2_R=np.sqrt(lambda_2)
    
    return np.array([[lambda_1_R,0],[0,lambda_2_R]])

def OrthTrans(e,a,b,g):
    g_b=g-b
    a2_gb=(2.*a)**2+g_b**2
    a2_gb_R=np.sqrt(a2_gb)
    
    B=g_b-a2_gb_R
    E=g_b+a2_gb_R
    
    B_2a=B**2+(2.*a)**2
    B_2a_R=np.sqrt(B_2a)
    
    E_2a=E**2+(2.*a)**2
    E_2a_R=np.sqrt(E_2a)
    
    C=B/B_2a_R
    D=2.*a/B_2a_R
    
    F=E/E_2a_R
    G=2.*a/E_2a_R
    
    return np.array([[C,F],[D,G]])
    



