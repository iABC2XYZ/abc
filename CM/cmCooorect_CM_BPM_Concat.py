#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:48:22 2017

@author: p
"""

import numpy as np

fName=[\
       'New_log_Nov_16_02:28:14_2017',\
       'New_log_Nov_16_03:13:19_2017',\
       'New_log_Nov_16_07:03:15_2017',\
       ]




for iName in fName:
    if not vars().has_key('data'):
        data=np.loadtxt(iName)
    else:
        dataTmp=np.loadtxt(iName)
        data=np.vstack((data,dataTmp))
   
mCM,nCM=np.shape(data)     

fid = open('trainCMData','w+')

for i in range(mCM):
    for j in range(nCM):
        iData=data[i,j]
        fid.writelines('%.2f' %iData)
        fid.writelines(' ')
    fid.writelines('\n')
fid.close()
    
print np.shape(data)
    
















