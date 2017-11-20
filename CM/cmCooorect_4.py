#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:46:48 2017

@author: p
"""

from epics import caget,caput
import time
import numpy as np

import tensorflow as tf

import matplotlib.pyplot as plt

plt.close('all')

filenRec='log_'+time.asctime().replace(' __','_').replace(' ','_')[4:]
fid=open(filenRec,'a+')

psUseStart=1
psUseEnd=7
bpmUseStart=1
bpmUseEnd=6

"""
psSetListLib=['MEBT_PS:DCH_01:ISet','MEBT_PS:DCV_01:ISet', \    #  1
           'MEBT_PS:DCH_02:ISet','MEBT_PS:DCV_02:ISet', \    #  2
           'MEBT_PS:DCH_03:ISet','MEBT_PS:DCV_03:ISet', \    #  3
           'MEBT_PS:DCH_04:ISet','MEBT_PS:DCV_04:ISet', \    #  4
           'MEBT_PS:DCH_05:ISet','MEBT_PS:DCV_05:ISet', \    #  5
           'MEBT_PS:DCH_06:ISet','MEBT_PS:DCV_06:ISet', \    #  6
           'MEBT_PS:DCH_07:ISet','MEBT_PS:DCV_07:ISet', \    #  7
           'HCM1_PS:DCH_01:ISet','HCM1_PS:DCV_01:ISet', \    #  8
           'HCM1_PS:DCH_02:ISet','HCM1_PS:DCV_02:ISet', \    #  9
           'HCM1_PS:DCH_03:ISet','HCM1_PS:DCV_03:ISet', \    #  10
           'HCM1_PS:DCH_04:ISet','HCM1_PS:DCV_04:ISet', \    #  11
           'HCM1_PS:DCH_05:ISet','HCM1_PS:DCV_05:ISet', \    #  12
           'HCM1_PS:DCH_06:ISet','HCM1_PS:DCV_06:ISet', \    #  13
        ]

psMonListLib=[]
for iSet in psSetList:
    psMonList.append(iSet.replace('Set','Mon'))

bpmListLib=['BPM:1-X11','BPM:1-Y11',\       #  1
          'BPM:2-X11', 'BPM:2-Y11',\      #  2
         'BPM:3-X11','BPM:3-Y11',\      #  3
         'BPM:4-X11','BPM:4-Y11',\      #  4
         'BPM:5-X11','BPM:5-Y11',\      #  5
         'BPM:6-X11', 'BPM:6-Y11',\      #  6
         'BPM:7-X11','BPM:7-Y11',\      #  7
         'BPM:8-X11','BPM:8-Y11',\      #  8
         'BPM:9-X11','BPM:9-Y11',\      #  9
         'BPM:10-X11','BPM:10-Y11',\      #  10
         'BPM:11-X11','BPM:11-Y11',\      #  11
         ]

psSetMaxLib=[15,15,\    #  MEBT 1
         15 ,15,\        #  MEBT 2
         15 ,15,\        #  MEBT 3
         15 ,15,\        #  MEBT 4
         15 ,15,\        #  MEBT 5
         15 ,15,\        #  MEBT 6
         15 ,15,\        #  MEBT 7
         65,65,\        #  HCM1# 1
         65,65,\        #  HCM1# 2
         65,65,\        #  HCM1# 3
         65,65,\        #  HCM1# 4
         65,65,\        #  HCM1# 5
         65,65,\        #  HCM1# 6
         ]

psSetMinLib=[-15,-15,\    #  MEBT 1
         -15 ,-15,\    #  MEBT 2
         -15 ,-15,\    #  MEBT 3
         -15 ,-15,\    #  MEBT 4
         -15 ,-15,\    #  MEBT 5
         -15 ,-15,\    #  MEBT 6
         -15 ,-15,\    #  MEBT 7
         -65,-65,\         #  HCM1# 1
         -65,-65,\        #  HCM1# 2
         -65,-65,\        #  HCM1# 3
         -65,-65,\        #  HCM1# 4
         -65,-65,\        #  HCM1# 5
         -65,-65,\        #  HCM1# 6
         ]

psSetAmpLib=[5,5,\   #  MEBT 1
         5 ,5,\   #  MEBT 2
         5 ,5,\   #  MEBT 3
         5 ,5,\   #  MEBT 4
         5 ,5,\   #  MEBT 5
         5 ,5,\   #  MEBT 6
         5 ,5,\   #  MEBT 7
         5,5,\         #  HCM1# 1
         5,5,\        #  HCM1# 2
         5,5,\         #  HCM1# 3
         5,5,\        #  HCM1# 4
         5,5,\        #  HCM1# 5
         5,5,\        #  HCM1# 6
         ]
"""

psSetListLib=['MEBT_PS:DCH_01:ISet','MEBT_PS:DCV_01:ISet', \
           'MEBT_PS:DCH_02:ISet','MEBT_PS:DCV_02:ISet', \
           'MEBT_PS:DCH_03:ISet','MEBT_PS:DCV_03:ISet', \
           'MEBT_PS:DCH_04:ISet','MEBT_PS:DCV_04:ISet', \
           'MEBT_PS:DCH_05:ISet','MEBT_PS:DCV_05:ISet', \
           'MEBT_PS:DCH_06:ISet','MEBT_PS:DCV_06:ISet', \
           'MEBT_PS:DCH_07:ISet','MEBT_PS:DCV_07:ISet', \
           'HCM1_PS:DCH_01:ISet','HCM1_PS:DCV_01:ISet', \
           'HCM1_PS:DCH_02:ISet','HCM1_PS:DCV_02:ISet', \
           'HCM1_PS:DCH_03:ISet','HCM1_PS:DCV_03:ISet', \
           'HCM1_PS:DCH_04:ISet','HCM1_PS:DCV_04:ISet', \
           'HCM1_PS:DCH_05:ISet','HCM1_PS:DCV_05:ISet', \
           'HCM1_PS:DCH_06:ISet','HCM1_PS:DCV_06:ISet', \
        ]

psMonListLib=[]
for iSet in psSetListLib:
    psMonListLib.append(iSet.replace('Set','Mon'))

bpmListLib=['BPM:1-X11','BPM:1-Y11',\
          'BPM:2-X11', 'BPM:2-Y11',\
         'BPM:3-X11','BPM:3-Y11',\
         'BPM:4-X11','BPM:4-Y11',\
         'BPM:5-X11','BPM:5-Y11',\
         'BPM:6-X11', 'BPM:6-Y11',\
         'BPM:7-X11','BPM:7-Y11',\
         'BPM:8-X11','BPM:8-Y11',\
         'BPM:9-X11','BPM:9-Y11',\
         'BPM:10-X11','BPM:10-Y11',\
         'BPM:11-X11','BPM:11-Y11',\
         ]

psSetMaxLib=[15,15,\
         15 ,15,\
         15 ,15,\
         15 ,15,\
         15 ,15,\
         15 ,15,\
         15 ,15,\
         65,65,\
         65,65,\
         65,65,\
         65,65,\
         65,65,\
         65,65,\
         ]

psSetMinLib=[-15,-15,\
         -15 ,-15,\
         -15 ,-15,\
         -15 ,-15,\
         -15 ,-15,\
         -15 ,-15,\
         -15 ,-15,\
         -65,-65,\
         -65,-65,\
         -65,-65,\
         -65,-65,\
         -65,-65,\
         -65,-65,\
         ]

psSetAmpLib=[5,5,\
         5 ,5,\
         5 ,5,\
         5 ,5,\
         5 ,5,\
         5 ,5,\
         5 ,5,\
         5,5,\
         5,5,\
         5,5,\
         5,5,\
         5,5,\
         5,5,\
         ]
#  --------------------

psSetList=psSetListLib[(psUseStart-1)*2:(psUseEnd)*2]
psMonList=psMonListLib[(psUseStart-1)*2:(psUseEnd)*2]
psSetMax=psSetMaxLib[(psUseStart-1)*2:(psUseEnd)*2]
psSetMin=psSetMinLib[(psUseStart-1)*2:(psUseEnd)*2]
psSetAmp=psSetAmpLib[(psUseStart-1)*2:(psUseEnd)*2]

bpmList=bpmListLib[(bpmUseStart-1)*2:(bpmUseEnd)*2]

###  -----------------    PICK  -------------------------------
eroorList=['MEBT_PS:DCH_05:ISet']
for iError in eroorList:
    indexError=psSetList.index(eroorList[0])
    psSetList.pop(indexError)
    psMonList.pop(indexError)
    psSetMax.pop(indexError)
    psSetMin.pop(indexError)
    psSetAmp.pop(indexError)
    
    






##--------------


def LogWrite(fid,X_,Y_):
    X1=X_[0,0::2]
    Y1=Y_[0,0::2]
    X2=X_[0,1::2]
    Y2=Y_[0,1::2]
    
    timeNow='# BPM : X>>Y   |   PS :  X>>Y  |  '+time.asctime()
    fid.writelines(timeNow)
    fid.writelines('\n')
    for iX in X1:
        fid.writelines('%.2f ' %iX) 
    fid.writelines('\n')
    for iX in X2:
        fid.writelines('%.2f ' %iX) 
    fid.writelines('\n')
    for iX in Y1:
        fid.writelines('%.2f ' %iX) 
    fid.writelines('\n')
    for iX in Y2:
        fid.writelines('%.2f ' %iX) 
    fid.writelines('\n')


def Plot(hPlot,bpmRec,psSetRec,psMonList,numRec):
    numItem=np.shape(bpmRec)[0]
    if numItem<numRec:
        X1=bpmRec[:,0::2]
        X2=bpmRec[:,1::2]
        Y1=psSetRec[:,0::2]
        Y2=psSetRec[:,1::2]
    else:
        X1=bpmRec[-numRec::,0::2]
        X2=bpmRec[-numRec::,1::2]
        Y1=psSetRec[-numRec::,0::2]
        Y2=psSetRec[-numRec::,1::2]
    
    psMon=GetPS(psMonList)
    xPSMon=psMon[0,0::2]
    yPSMon=psMon[0,1::2]
    
    plt.figure(hPlot)
    plt.clf()
    plt.subplot(1,2,1)
    plt.plot(X1.T,'-*')
    plt.grid('on')
    plt.axis([-0.5,len(X1.T)-0.5,-10,10])
    plt.subplot(1,2,2)
    plt.plot(X2.T,'-*')
    plt.grid('on')
    plt.axis([-0.5,len(X2.T)-0.5,-10,10])
    plt.pause(0.01)
    
    plt.figure(hPlot+1)
    plt.clf()
    plt.hold
    plt.subplot(1,2,1)
    plt.plot(Y1.T,'-*')
    plt.plot(xPSMon,'ro')
    plt.grid('on')
    plt.axis([-0.5,len(Y1.T)-0.5,-15.5,15.5])
    plt.subplot(1,2,2)
    plt.plot(Y2.T,'-*')
    plt.plot(yPSMon,'ro')
    plt.grid('on')
    plt.axis([-0.5,len(Y1.T)-0.5,-15.5,15.5])
    plt.pause(0.01)    

## ----------------
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
        
## ------------------- INIT  4  ALL  ----------
    
bpmNow=GetBPM(bpmList)
psSetNow=GetPS(psSetList)

bpmAim=-bpmNow
bpmAim[0,0:2]=0
bpmAimOri=np.zeros(np.shape(bpmAim))
bpmAimOri[0,0:2]=bpmNow[0,0:2]
bpmAim=np.hstack((bpmAimOri,bpmAim))

LogWrite(fid,bpmNow,psSetNow)

bpmRec=bpmNow
psSetRec=psSetNow

## ---------------- INIT 4 DATA  ------------
def PutPS(psSetList,psSetNow):
    for i in range(len(psSetList)):
        iStr,iVal=psSetList[i],psSetNow[i]
        caput(iStr,iVal)

        

def Sleep(psSetNow_,psMonList):
    iPrint=0
    while True:
        iPrint+=1
        psMonNow_= GetPS(psMonList)
        psSetNow=psSetNow_[0,:]
        psMonNow=psMonNow_[0,:]
        
        d_PS=np.abs(psSetNow-psMonNow)
        #print psMonList
        #print d_PS
        
        flag_PS=d_PS<2
        flag_PS_All=np.prod(flag_PS)
        time.sleep(1)
        if flag_PS_All==0:
            idFalse=np.array(np.where( flag_PS==False))[0,:]+1
            numQ=np.int32(idFalse/2)
            if idFalse[0] % 2 ==1:
                nameCV='H'
            else:
                nameCV='V'
            if iPrint>3:
                print 'Please check   '+str(numQ)+'   '+nameCV+'  '+str(np.round(100*psSetNow[idFalse])/100)+' '+str(np.round(100*psMonNow[idFalse])/100)

        if  flag_PS_All==1:
            break
    
    
    
     
def CheckPSSet(psSetNow,psSetMax,psSetMin,flagPSSet):
    psSetMaxArray=np.array(psSetMax)
    psSetMinArray=np.array(psSetMin)
    flagPSSet[psSetNow<psSetMinArray]=1
    flagPSSet[psSetNow>psSetMaxArray]=-1
    psSetNow[psSetNow<psSetMinArray]=2*psSetMinArray[psSetNow<psSetMinArray]-psSetNow[psSetNow<psSetMinArray]
    psSetNow[psSetNow>psSetMaxArray]=2*psSetMaxArray[psSetNow>psSetMaxArray]-psSetNow[psSetNow>psSetMaxArray]
    return psSetNow,flagPSSet

def CheckPSSetSim(psSetNow,psSetMax,psSetMin):
    psSetMaxArray=np.array(psSetMax)
    psSetMinArray=np.array(psSetMin)
    psSetNow[psSetNow<psSetMinArray]=2*psSetMinArray[psSetNow<psSetMinArray]-psSetNow[psSetNow<psSetMinArray]
    psSetNow[psSetNow>psSetMaxArray]=2*psSetMaxArray[psSetNow>psSetMaxArray]-psSetNow[psSetNow>psSetMaxArray]
    return psSetNow


def CheckPSSetChange(psSetChange_,psSetAmp):
    psSetChange=psSetChange_[0,:]
    psSetMax=np.array(psSetAmp)
    psSetMin=-np.array(psSetAmp)
    psSetMaxArray=np.array(psSetMax)
    psSetMinArray=np.array(psSetMin)
    psSetChange[psSetChange<psSetMinArray]=psSetMinArray[psSetChange<psSetMinArray]
    psSetChange[psSetChange>psSetMaxArray]=psSetMaxArray[psSetChange>psSetMaxArray]
    return psSetChange


#####----------------------------    


numBPM=len(bpmList)
numPS=len(psSetList)
numInitData=25      ######################################################
for i in xrange(numInitData):
    print "Init Data"
    print i
    psSetLast=psSetRec[-1,:]
    if i==0:
        flagPSSet=np.sign(np.random.random(np.shape(psSetLast))-0.5)
    
    psSetChange=(np.random.random((np.shape(psSetLast)))*1)*np.array(psSetAmp)
    psSetChange=psSetChange*flagPSSet
    
    psSetNow=psSetLast+psSetChange
    psSetNow,flagPSSet=CheckPSSet(psSetNow,psSetMax,psSetMin,flagPSSet)

    PutPS(psSetList,psSetNow)
    
    psSetNow=psSetNow[np.newaxis,:]
    psSetRec=np.vstack((psSetRec,psSetNow))
    
    Sleep(psSetNow,psMonList)

    bpmNow=GetBPM(bpmList)
    bpmRec=np.vstack((bpmRec,bpmNow))
    
    Plot(1001,bpmRec,psSetRec,psMonList,3)
    LogWrite(fid,bpmNow,psSetNow)
    
#### -------  CONFIG -------------------------------
    
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
    #idChoose_0=idChoose_1-1
    
    d_psChoose=psSetRec[idChoose_1,:]-psSetRec[idChoose_0,:]
    d_BPMChoose=bpmRec[idChoose_1,:]-bpmRec[idChoose_0,:]
    
    x0=bpmRec[idChoose_0,:]
    dx=d_BPMChoose
    X=np.hstack((x0,dx))
    
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
            

learningRate=0.001      #--------------------------------------------
numEpoch=2000
batchSize=150

numInput=numBPM*2
numOutput=numPS

xIn=tf.placeholder(tf.float32,shape=(None,numInput))
yIn=tf.placeholder(tf.float32,shape=(None,numOutput))

num1=8
w1=GenWeight((numInput,num1))
b1= GenWeight((1,num1))[0,:]
x1=tf.nn.relu(tf.nn.xw_plus_b(xIn,w1,b1))

#
num2=8
w2=GenWeight((num1,num2))
b2= GenWeight((1,num2))[0,:]

x2=tf.nn.relu(tf.nn.xw_plus_b(x1,w2,b2))

num3=numOutput
w3=GenWeight((num2,num3))
b3= GenWeight((1,num3))[0,:]
x3=tf.nn.dropout(tf.nn.xw_plus_b(x2,w3,b3),keep_prob=0.5)

xOut=x3

yOut=yIn

loss=tf.losses.mean_squared_error(xOut,yOut)
train=tf.train.AdamOptimizer(learningRate)
opt=train.minimize(loss)

se=tf.Session()
se.run(tf.global_variables_initializer())

######## ---------   Train   Initial------------------

lossRecRec=RunTrain(se,opt,loss,numEpoch,batchSize,psSetRec,bpmRec)

######## ---------   Train  ------------------
numTrain=200
for iTrain in range(numTrain):
    print "Train"
    print iTrain
    
    psSetLast=psSetRec[-1,:]
    psSetChange=se.run(xOut,feed_dict={xIn:bpmAim})
    print bpmAim
    psSetChange=CheckPSSetChange(psSetChange,psSetAmp)
    psSetChange*=0.5
    psSetNow=psSetLast+psSetChange    
    
    psSetNow=CheckPSSetSim(psSetNow,psSetMax,psSetMin)
    

    """
    ##-------
    bpmNow=GetBPM(bpmList)
    if np.std(bpmNow)>1.2:
        flagMin=psSetNow>(np.array(psSetMax)*0.75)
        flagMax=psSetNow<(np.array(psSetMin)*0.75)
        flagM=flagMin * flagMax
        psSetNow[flagM]=psSetNow[flagM==1]*(np.random.random((np.shape(psSetNow[flagM==1])))*0.5)
    
    ## -------
    """
    
    PutPS(psSetList,psSetNow)
        
    psSetNow=psSetNow[np.newaxis,:]
    psSetRec=np.vstack((psSetRec,psSetNow))
    lossRecRec=RunTrain(se,opt,loss,numEpoch,batchSize,psSetRec,bpmRec)
    
    
    Sleep(psSetNow,psMonList)
    #time.sleep(7)
    bpmNow=GetBPM(bpmList)
    bpmRec=np.vstack((bpmRec,bpmNow))
    
    Plot(1001,bpmRec,psSetRec,psMonList,1)
    LogWrite(fid,bpmNow,psSetNow)

    plt.figure(999)
    plt.clf()
    plt.plot(lossRecRec)
    plt.pause(0.01)
##--------   Final  ------------------------

se.close()
    
fid.close()





























