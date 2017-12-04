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
plt.close('all')


yRatioPreLoad=np.loadtxt('Ratio.pre')
yRatioPre=yRatioPreLoad.T
xFit=np.linspace(0,1,np.shape(yRatioPre)[0])
pYRatioPre=np.polyfit(xFit,yRatioPre,1)
kRatio=pYRatioPre[0,:]
#kRatio[kRatio<-0.1]=-0.1


kRatioMaxIndex=[]
kRatio_=np.copy(kRatio)
numMax=5
for iMax in range(numMax):
    argMax=np.argmax(kRatio_)
    kRatio_[argMax]=0.
    kRatioMaxIndex.append(argMax)

plt.close(2)
plt.figure(2)
plt.clf()
plt.hold
plt.plot(kRatioMaxIndex,kRatio[kRatioMaxIndex],'ro')
plt.plot(kRatio,'b.')
plt.title('kRatio')


##

codeChoose=[]
idCode=0
fidCodeRead=open('ml.code','r')
fidCodeWrite=open('ml.code.Choose','w+')
for iCode in fidCodeRead:
    if idCode in kRatioMaxIndex:
        fidCodeWrite.writelines(iCode)
        codeChoose.append(iCode)
    idCode+=1


fidCodeRead.close()
fidCodeWrite.close()


##
xPre=np.loadtxt('ml.pre')
xPreChoose=xPre[kRatioMaxIndex,2::5].T

plt.close(501)
plt.figure(501)
plt.clf()
plt.plot(xPreChoose)
plt.title('xPreChoose')

##

yRatioPreChoose=yRatioPreLoad[kRatioMaxIndex,:].T
plt.close(502)
plt.figure(502)
plt.clf()
plt.plot(yRatioPreChoose)
plt.title('yRatioPreChoose')

##
yPreChoose=yRatioPreChoose
for iMax in range(numMax):
    yPreChoose[:,iMax]=(yRatioPreChoose[:,iMax]+1.)*xPreChoose[-1,iMax]

plt.close(503)
plt.figure(503)
plt.clf()
plt.plot(yPreChoose)
plt.title('yPreChoose')

##

xyPre=np.vstack((xPreChoose,yPreChoose))

plt.close(504)
plt.figure(504)
plt.clf()
plt.plot(xyPre)
plt.title('xyPre')

##

kRatioMean=np.mean(kRatio)
kRatioPosi=np.sum(kRatio>0)
kRatioNeg=np.sum(kRatio<0)




print kRatioMean
print kRatioPosi,kRatioNeg


plt.show()











