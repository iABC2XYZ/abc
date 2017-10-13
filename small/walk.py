#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 18:26:23 2017

@author: A
"""



import os

'''
for root, dirs, files in os.walk("/home/A/Desktop", topdown=False):
    for name in files:
        print(os.path.join(root, name))
    
    print "____________"
    
    for name in dirs:
        print(os.path.join(root, name))
'''


print os.listdir('/home/A/Desktop')




