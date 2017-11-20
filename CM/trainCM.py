#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 11:08:01 2017

@author: p
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

import time
from epics import caget,caput

fName='trainCMData'

dataOri=np.loadtxt(fName)

dataBPM=dataOri[:,6:22]
dataPS=dataOri[:,70:86]

numItem,numBPM= np.shape(dataBPM)
numPS=np.shape(dataPS)[1]


##-------------##----------------##-------------------

def GenWeight(shape):
    initial = tf.truncated_normal(shape, stddev=1.)
    return tf.Variable(initial)

def GenBias(shape):
    initial=GenWeight((1,shape(0)))
    return initial[0,:]
    
def PreTrain(psSetRec,bpmRec,batchSize):
    numItem=np.shape(bpmRec)[0]
    idChoose_0=np.random.randint(0,high=numItem,size=(batchSize))
    idChoose_1=np.random.randint(1,high=numItem,size=(batchSize))
    
    d_psChoose=psSetRec[idChoose_1,:]-psSetRec[idChoose_0,:]
    d_BPMChoose=bpmRec[idChoose_1,:]-bpmRec[idChoose_0,:]
    
   # x0=bpmRec[idChoose_0,:]
    #dx=d_BPMChoose
    #X=np.hstack((x0,dx))
   
    X=d_BPMChoose
    Y=d_psChoose
    
    return X,Y

def RunTrain(se,opt,loss,numEpoch,batchSize,psSetRec,bpmRec):
    lossRecRec=[]
    for _ in range(numEpoch):
        X,Y=PreTrain(psSetRec,bpmRec,batchSize)
        
        se.run(opt,feed_dict={xIn:X,yIn:Y})
        if _% 50==0:
            lossRecTmp=se.run(loss,feed_dict={xIn:X,yIn:Y})
            lossRecRec.append(lossRecTmp)
    return lossRecRec
            

learningRate=0.005      #--------------------------------------------
numEpoch=500000
batchSize=50

numInput=numBPM
numOutput=numPS

xIn=tf.placeholder(tf.float32,shape=(None,numInput))
yIn=tf.placeholder(tf.float32,shape=(None,numOutput))

'''
num1=8
w1=GenWeight((numInput,num1))
b1= GenWeight((1,num1))[0,:]
x1=tf.nn.relu(tf.nn.xw_plus_b(xIn,w1,b1))

#
num2=numOutput
w2=GenWeight((num1,num2))
b2= GenWeight((1,num2))[0,:]
x2=tf.nn.xw_plus_b(x1,w2,b2)
'''

w0=GenWeight((numInput,numOutput))
x0=tf.matmul(xIn,w0)

xOut=x0

yOut=yIn


loss=tf.losses.mean_squared_error(xOut,yOut)


train=tf.train.AdamOptimizer(learningRate)
opt=train.minimize(loss)


if vars().has_key('se'):
    se.close()
else:
    se=tf.Session()
se.run(tf.global_variables_initializer())



######## ---------   Train  ------------------
plt.close('all')
lossRec=[]
lossMeanRec=[]
rAimRec=[]
for _ in range(numEpoch):
    X,Y=PreTrain(dataPS,dataBPM,batchSize)
    
    se.run(opt,feed_dict={xIn:X,yIn:Y})
    if _% 50==0:
        lossRecTmp=se.run(loss,feed_dict={xIn:X,yIn:Y})
        xAim=np.zeros((1,numBPM))-np.mean(dataBPM,axis=0)[np.newaxis,:]
        yAim=se.run(xOut,feed_dict={xIn:xAim})[0]
        lossRec.append(lossRecTmp)
        lossMeanRec.append(np.mean(lossRec))
        rAimRec.append(np.sum(np.square(yAim)))
        if len(lossRec)>200:
            lossRec.pop(0)
            lossMeanRec.pop(0)
            rAimRec.pop(0)


        plt.figure(1)
        plt.clf()
        plt.hold('on')
        plt.plot(lossRec,'r')
        plt.plot(lossMeanRec,'g')
        plt.grid('on')
        plt.title(_)
        plt.pause(0.01)
        
        plt.figure(2)
        plt.clf()
        plt.plot(yAim,'r-*')
        plt.grid('on')
        plt.title(_)
        plt.pause(0.01)
        

        plt.figure(3)
        plt.clf()
        plt.plot(rAimRec,'g-')
        plt.grid('on')
        plt.title(_)
        plt.pause(0.01)        
    ##--------   Final  ------------------------



psList=[\
         'MEBT_PS:DCH_06:ISet','MEBT_PS:DCV_06:ISet', \
           'MEBT_PS:DCH_07:ISet','MEBT_PS:DCV_07:ISet', \
           'HCM1_PS:DCH_01:ISet','HCM1_PS:DCV_01:ISet', \
           'HCM1_PS:DCH_02:ISet','HCM1_PS:DCV_02:ISet', \
           'HCM1_PS:DCH_03:ISet','HCM1_PS:DCV_03:ISet', \
           'HCM1_PS:DCH_04:ISet','HCM1_PS:DCV_04:ISet', \
           'HCM1_PS:DCH_05:ISet','HCM1_PS:DCV_05:ISet', \
           'HCM1_PS:DCH_06:ISet','HCM1_PS:DCV_06:ISet', \
           ]
bpmList=[\
         'BPM:4-X11','BPM:4-Y11',\
         'BPM:5-X11','BPM:5-Y11',\
         'BPM:6-X11', 'BPM:6-Y11',\
         'BPM:7-X11','BPM:7-Y11',\
         'BPM:8-X11','BPM:8-Y11',\
         'BPM:9-X11','BPM:9-Y11',\
         'BPM:10-X11','BPM:10-Y11',\
         'BPM:11-X11','BPM:11-Y11',\
         ]

def GetBPM(bpmList):
    bpmNow=[]
    for iBPM in bpmList:
        bpmNow.append(caget(iBPM))
    bpmNow=np.array(bpmNow)[np.newaxis,:]
    return bpmNow

def GetPS(psSetList):
    psNow=[]
    for iPS in psSetList:
        psNow.append(caget(iPS))
    psNow=np.array(psNow)[np.newaxis,:]
    return psNow

def PutPS(psSetList,psSetNow):
    for i in range(len(psSetList)):
        iStr,iVal=psSetList[i],psSetNow[i]
        caput(iStr,iVal)


def LogWrite(fid,X):
    fid.writelines('#=========================')
    timeNow='#  '+time.asctime()
    fid.writelines(timeNow)
    fid.writelines('\n')
    
    for i in X:
        for j in i:
            fid.writelines('%.2f ' %j)
        fid.writelines('\n')
            


bpmNow=GetBPM(bpmList)
bpmAim=0-bpmNow
psAim=se.run(xOut,feed_dict={xIn:bpmAim})
psNow=GetPS(psList)

psPut=(psNow+psAim)[0]
for i in range(len(psAim)):
    if i <4:
        if psPut[i]<-15:
            psPut[i]=-15
        if psPut[i]>15:
            psPut[i]=15
    else:
        if psPut[i]<-65:
            psPut[i]=-65
        if psPut[i]>65:
            psPut[i]=65

psPut=np.round(psPut*100)/100
print psPut

PutPS(psList,psPut)

time.sleep(80)

bpmUpdate=GetBPM(bpmList)

fid=open('TestLogVIP','a+')
LogWrite(fid,(bpmNow[0],bpmAim[0],psAim[0],psNow[0],psPut,bpmUpdate[0]))
fid.close()


plt.figure(9986)
plt.plot(psAim[0],'-*')
plt.figure(9987)
plt.plot(psNow[0],'-*')
plt.figure(9988)
plt.plot(bpmUpdate[0],'-*')







'''
for i in range(numBPM):
    plt.figure('BPM')
    plt.clf()
    plt.hist(dataBPM[:,i],100)
    plt.grid('on')
    plt.title(i)
    plt.pause(1)


for i in range(numPS):
    plt.figure('PS')
    plt.clf()
    plt.hist(dataPS[:,i],100)
    plt.grid('on')
    plt.title(i)
    plt.pause(1)
'''








'''
class NNMat():
    def __init__(self,numInput,numOutput,learningRate):
        self.numInput=numInput
        self.numOutput=numOutput
        self.learningRate=learningRate
    def GenWeight(shape):
        initial = tf.truncated_normal(shape, stddev=1.)
        return tf.Variable(initial)
    def GenBias(shape):
        initial = tf.constant(1., shape=shape)
        return tf.Variable(initial)
'''
        
    




















