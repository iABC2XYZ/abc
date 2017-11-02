#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 22:03:21 2017

@author: p
"""

import numpy as np

a=np.ones((33))

with open('/home/p/ABC/abc/Epics/test','a+') as f:
    f.writelines(str(a))
    
    
A=str(a).replace('\n','')[1:-1:]+' '



print A


if True:
    pass
elif True:
    pass
    


