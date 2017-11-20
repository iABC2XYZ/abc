#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:09:50 2017

@author: p
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 00:03:34 2017

@author: p
"""


import numpy as np
import os
import matplotlib.pyplot as plt

fNameBK='log_Nov_16_07:03:15_2017'
fNameLog='log'
fNameData='logData'

os.system('cp '+fNameBK+' '+fNameLog)

fidLog=open(fNameLog,'r')
fidData=open(fNameData,'w+')

lenI=0
iRec=0
for i in fidLog:
    iRec+=1
    if i[0]=='B':
        continue
    lenI+=len(i)
    if len(i)<lenI/iRec*0.8:
        continue
    fidData.writelines(i)
fidLog.close()
fidData.close()
    
data=np.loadtxt(fNameData)
print np.shape(data)
numItem=np.shape(data)[0]
lenData=np.shape(data)[1]
if lenData==147:
    

    
    data2=np.zeros((numItem,211))
    
    data2[:,0:34]=data[:,0:34]
    data2[:,60:98]=data[:,34:72]
    data2[:,120:158]=data[:,72:110]
    data2[:,180:183]=data[:,128:131]
    data2[:,184:199]=data[:,131:146]
    data2[:,210]=data[:,146]
    
    fNameNew='New_'+fNameBK
    fidNew=open(fNameNew,'w+')
    for i in range(numItem):
        for j in range(211):
            iData=data2[i,j]
            fidNew.writelines('%.2f' %iData)
            fidNew.writelines(' ')
        fidNew.writelines('\n')
    fidNew.close()

if lenData==211:
    fNameNew='New_'+fNameBK
    fidNew=open(fNameNew,'w+')
    for i in range(numItem):
        for j in range(211):
            iData=data[i,j]
            fidNew.writelines('%.2f' %iData)
            fidNew.writelines(' ')
        fidNew.writelines('\n')
    fidNew.close()
    
    
    




