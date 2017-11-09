#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""

import numpy as np
import matplotlib.pyplot as plt


nameFolder='/home/e/ABC/abc/BPM/Paper/'


nameData=nameFolder+'Rec_1106_2046.dat'
exData=np.loadtxt(nameData)

'''
for i in range(24):
    plt.figure(1)
    plt.clf()
    plt.plot(exData[:,i],'.')
    plt.title(i)
    plt.pause(1)
'''
'''
for i in range(10,24):
    plt.figure(1)
    plt.clf()
    plt.hist(exData[:,i],1000)
    plt.title(i)
    plt.pause(1)
'''

exDataMean=[]
for i in range(14,24):
    exDataMeanTmp= np.mean(exData[:,i])
    exDataMean.append(exDataMeanTmp)
    


print "+"
print str(np.round(np.array(exDataMean)*100.)/100.).replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace(' ',',')

print ('\n')

exDataMean[0]=0.00
exDataMean[7]=0.00

print "-"
print str(np.round(-np.array(exDataMean)*100.)/100.).replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace(' ',',')


##

exDataMean=[]
for i in range(14,24):
    exDataMeanTmp= np.mean(exData[:,i])
    exDataMean.append(exDataMeanTmp)

bpms=exData[:,14:24]

for i in range(10):
    bpms[:,i]-=exDataMean[i]

rBPM=[]
for i in range(np.shape(bpms)[0]):
    rBPM.append(np.sum(np.square(bpms[i,:])))

idMinR=np.argmin(rBPM)

print idMinR,rBPM[idMinR]

print '---- I  -------'
print (exData[idMinR,14:24])

print exDataMean


print  np.sum(np.square(exData[idMinR+1,14:24]-exDataMean))


#plt.plot(rBPM)
#plt.show()

#print np.where(np.min(rBPM)==rBPM)







