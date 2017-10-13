#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:25:56 2017

@author: A
"""

t=np.linspace(0,500,5000)
x=np.sin(t)
plt.plot(t,x)

with open('/home/A/Codes/data/open/000000.open','w') as fid:
    for i in x:
        fid.writelines(str(i)+'\n')




