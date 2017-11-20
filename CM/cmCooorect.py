#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 14:49:20 2017

@author: p
"""

from epics import caget,caput
import time
import numpy as np

import tensorflow as tf

import matplotlib.pyplot as plt

plt.close('all')

def GenWeight(shape):
    initial = tf.truncated_normal(shape, stddev=1.)
    return tf.Variable(initial)
def GenBias(shape):
    initial = tf.constant(1., shape=shape)
    return tf.Variable(initial)


dcSetHV='HCMX_PS:DCH_99:ISet'

bpmXY11='BPM:0-X11'



cmID=1
bpmStart=5
bpmEnd=10
cavStart=1
cavEnd=6

learningRate=0.01

flagAim=2

#


##
numBPM=(bpmEnd-bpmStart+1)*2
numDC=(cavEnd-cavStart+1)*2


bpmX=tf.placeholder(tf.float32,shape=[None,numBPM])
dcY=tf.placeholder(tf.float32,shape=[None,numDC])

wXY=GenWeight((numBPM,numDC))

dcY_=tf.matmul(bpmX,wXY)

lossCorrect=tf.losses.mean_squared_error(dcY_,dcY)

trainCorrect=tf.train.AdamOptimizer(learningRate)
optCorrect=trainCorrect.minimize(lossCorrect)



se=tf.Session()
se.run(tf.global_variables_initializer())


dcRec=[]
bpmRec=[]


def GetBPM(bpmStart,bpmEnd,bpmXY11):
    xBPM=[]
    yBPM=[]
    for i in range(bpmStart,bpmEnd+1):
        xNameBPM=bpmXY11.replace('0-X',str(i)+'-X')
        yNameBPM=bpmXY11.replace('0-X',str(i)+'-Y')
        xBPMTmp=caget(xNameBPM)
        yBPMTmp=caget(yNameBPM)
        xBPM.append(xBPMTmp)
        yBPM.append(yBPMTmp)
    return xBPM,yBPM

def GetBPM4Train(bpmStart,bpmEnd,bpmXY11):
    xBPM,yBPM=GetBPM(bpmStart,bpmEnd,bpmXY11)
    bpmX=np.hstack((xBPM,yBPM))
    bpmX=np.round(bpmX*100.)/100.
    bpmX=bpmX[np.newaxis,:]
    return bpmX

def GetDCCurrent(cmID,cavStart,cavEnd,dcSetHV):    
    iDCH=[]
    iDCV=[]
    for i in xrange(cavStart,cavEnd+1):
        nameDC_H=dcSetHV.replace('H_99','H_0'+str(i)).replace('X',str(cmID))
        nameDC_V=dcSetHV.replace('H_99','V_0'+str(i)).replace('X',str(cmID))
          
        iDCHTmp=caget(nameDC_H)   
        iDCVTmp=caget(nameDC_V)  
        
        iDCH.append(iDCHTmp)
        iDCV.append(iDCVTmp)
                
    return iDCH,iDCV

def GetDCCurrent4Train(cmID,cavStart,cavEnd,dcSetHV):    
    dcH,dcV=GetDCCurrent(cmID,cavStart,cavEnd,dcSetHV)
    dcY=np.hstack((dcH,dcV))
    dcY=np.round(dcY*100.)/100.
    dcY=dcY[np.newaxis,:]
                
    return dcY

#
    
def CheckDCCurrentSet(dcYSet,dcMax,dcMin):
    dcYSet[dcYSet>dcMax]=dcMax*2-dcYSet[dcYSet>dcMax]
    dcYSet[dcYSet<dcMin]=dcMin*2-dcYSet[dcYSet<dcMin]
    return dcYSet



def Init(bpmStart,bpmEnd,bpmXY11,cmID,cavStart,cavEnd,dcSetHV):

    bpmX=GetBPM4Train(bpmStart,bpmEnd,bpmXY11)
    bpmX4Train=bpmX
    
    dcY=GetDCCurrent4Train(cmID,cavStart,cavEnd,dcSetHV)
    dcY4Train=dcY
    return bpmX4Train,dcY4Train



def PutDCH(cmID,dcYSet,dcSetHV):
    numCav=len(dcYSet)/2
    for i in range(0,numCav):
        nameDCH=dcSetHV.replace('X',str(cmID)).replace('H_99','H_0'+str(i+1))
        nameDCV=dcSetHV.replace('X',str(cmID)).replace('H_99','V_0'+str(i+1))
        #caput(nameDCH,dcYSet[i])
        #caput(nameDCV,dcYSet[i+numCav])
        #print nameDCH
        #print nameDCV


def Sleep(cmID,dcYSet,dcSetHV):
    while True:
        flagSleep=0
        
        numCav=len(dcYSet)/2
        for i in range(0,numCav):
            nameDCH=dcSetHV.replace('X',str(cmID)).replace('H_99','H_0'+str(i+1)).replace('Set','Mon')
            nameDCV=dcSetHV.replace('X',str(cmID)).replace('H_99','V_0'+str(i+1)).replace('Set','Mon')
            getDCH=caget(nameDCH)
            getDCV=caget(nameDCV)
            
            if np.abs(getDCH-dcYSet[i])>1. or np.abs(getDCV-dcYSet[i+numCav])>1.:
                flagSleep=1
                continue
            else:
                flagSleep=2
                
        if flagSleep==1:
            time.sleep(1)
        elif flagSleep==2:
            time.sleep(0.8)
            break;
        


def BpmAim(flagAim):
    if flagAim==1:
        bpmX=GetBPM4Train(bpmStart,bpmEnd,bpmXY11)
        bpmAim=-bpmX[0,:]
        bpmAim[0]=bpmX[0,0]
        bpmAim[len(bpmAim)/2]=bpmX[0,len(bpmAim)/2]
    if flagAim==2:
        bpmX=GetBPM4Train(bpmStart,bpmEnd,bpmXY11)
        bpmAim=-bpmX[0,:]
        return bpmAim
        

def STR(iDCHPut):
    str_iDCHPut=str(np.round(np.array(iDCHPut)*100.)/100.)[1:-1].strip().replace('\n',' ').replace(',',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ')+' '
    return str_iDCHPut

##
dcAmp=5
dcMax=65
dcMin=-65

#

#
batchSize=100

#

cutRec=5
iRec=0
bpmX4Train,dcY4Train=Init(bpmStart,bpmEnd,bpmXY11,cmID,cavStart,cavEnd,dcSetHV)
bpmAim=BpmAim(flagAim)
while True:
    iRec+=1
    
    if iRec<cutRec:
        d_dcYSet=(np.random.random([1,numDC])*-1)*dcAmp
        dcYSet=dcY4Train[-1,:]+d_dcYSet
        dcYSet=CheckDCCurrentSet(dcYSet,dcMax,dcMin)
        dcY4Train=np.vstack((dcY4Train,dcYSet))
        PutDCH(cmID,dcYSet,dcSetHV)
        #Sleep(cmID,dcYSet,dcSetHV)
        bpmNow=GetBPM4Train(bpmStart,bpmEnd,bpmXY11)
        bpmX4Train=np.vstack((bpmX4Train,bpmNow))


        idX1=np.random.randint(0,high=iRec,size=[batchSize])
        idX2=np.random.randint(0,high=iRec,size=[batchSize])
        X=bpmX4Train[idX2,:]-bpmX4Train[idX1,:]
        Y=dcY4Train[idX2,:]-dcY4Train[idX1,:]
        
        se.run(optCorrect,feed_dict={bpmX:X,dcY:Y})
    else:
        bpmNow=GetBPM4Train(bpmStart,bpmEnd,bpmXY11)
        d_BPM=(bpmAim-bpmNow[0,:])[np.newaxis,:]
        d_dcYSet=se.run(dcY_,feed_dict={bpmX:d_BPM})
        
        d_dcYSet[d_dcYSet>dcAmp]=dcAmp
        d_dcYSet[d_dcYSet<-dcAmp]=-dcAmp
        
        dcYSet=dcY4Train[-1,:]+d_dcYSet
        dcYSet=CheckDCCurrentSet(dcYSet,dcMax,dcMin)
        dcY4Train=np.vstack((dcY4Train,dcYSet))
        PutDCH(cmID,dcYSet,dcSetHV)
        
        idX1=np.random.randint(0,high=iRec-1,size=[batchSize])
        idX2=np.random.randint(0,high=iRec-1,size=[batchSize])
        X=bpmX4Train[idX2,:]-bpmX4Train[idX1,:]
        Y=dcY4Train[idX2,:]-dcY4Train[idX1,:]        
        
        se.run(optCorrect,feed_dict={bpmX:X,dcY:Y})
        
        #Sleep(cmID,dcYSet,dcSetHV)
        bpmNow=GetBPM4Train(bpmStart,bpmEnd,bpmXY11)
        bpmX4Train=np.vstack((bpmX4Train,bpmNow))        
        
        
    
    with open('log','a+') as fid:
        strLines= '-'*10+'bpm X-Y >> dc X-Y '+'-'*10+'\n'
        fid.writelines(strLines)
        for i in range(numBPM):
            if i==numBPM/2:
                fid.writelines('\n')
            fid.writelines('%.2f ' %bpmNow[0,i]) 
        fid.writelines('\n')

        for i in range(numDC):
            if i==numDC/2:
                fid.writelines('\n')
            fid.writelines('%.2f ' %dcYSet[0,i]) 
        fid.writelines('\n')
        
        
        
  
    #if iRec>15:
    #    break


    
    
    
    
    






























print ('END')












