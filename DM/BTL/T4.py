#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:52:28 2017

@author: p

    NN
    
"""


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PreData import RandItemMulti
from testPredict import DealBeta,RoundItemMultiPack,CalLatticeSingle

plt.close('all')

def GenWeight(shape):
    initial = tf.truncated_normal(shape, stddev=1.)
    return tf.Variable(initial)
def GenBias(shape):
    initial = tf.constant(1., shape=shape)
    return tf.Variable(initial)



numItem=64
numSample=2**8
numQuadHigh=20

weightSize=[numSample*4,2**6,2**4,numQuadHigh*3]

wFC1 = GenWeight([weightSize[0],weightSize[1]])
bFC1=GenWeight([weightSize[1]])

wFC2 = GenWeight([weightSize[1],weightSize[2]])
bFC2=GenWeight([weightSize[2]])

wFC3 = GenWeight([weightSize[2],weightSize[3]])
bFC3=GenWeight([weightSize[3]])


xInput=tf.placeholder(tf.float32,shape=[None,weightSize[0]])
yInput=tf.placeholder(tf.float32,shape=[None,weightSize[-1]])

xFC1=tf.matmul(xInput,wFC1)+bFC1
xAct1=tf.nn.relu(xFC1)
xFC2=tf.matmul(xAct1,wFC2)+bFC2
xAct2=tf.nn.relu(xFC2)
xFC3=tf.matmul(xAct2,wFC3)+bFC3

xFinal=xFC3

xOutput=xFinal
yOutput=yInput

xOutputMat=tf.reshape(xOutput,(numQuadHigh,3))

costFunc=tf.reduce_sum((yOutput-xOutput)**2)

trainBTL=tf.train.AdamOptimizer(0.03)
optBTL=trainBTL.minimize(costFunc)

iniBTL=tf.global_variables_initializer()



zGivenLearn=np.array([0,2,3,5,6,7,9,12,15,16,17])
betaXGivenLearn=np.sin(zGivenLearn+np.random.random(np.size(zGivenLearn)))+3
betaYGivenLearn=-np.sin(zGivenLearn+np.random.random(np.size(zGivenLearn)))+3
numQuadLearn=5

zGivenValidate=np.array([0,1,2,4,6,9,11,14,16,19,21])
betaXGivenValidate=np.sin(zGivenValidate-np.random.random(np.size(zGivenValidate)))+3
betaYGivenValidate=-np.sin(zGivenValidate-np.random.random(np.size(zGivenValidate)))+3
numQuadValidate=5

dataBeamLearn=DealBeta(zGivenLearn,betaXGivenLearn,betaYGivenLearn,numSample,numQuadLearn)
dataBeamValidate=DealBeta(zGivenLearn,betaXGivenLearn,betaYGivenLearn,numSample,numQuadValidate)


zGivenLearn=dataBeamLearn[:,0]
betaXGivenLearn=dataBeamLearn[:,1]
betaYGivenLearn=dataBeamLearn[:,2]
plt.figure(0)
plt.clf()
plt.subplot(121)
plt.hold('on')
plt.plot(zGivenLearn,betaXGivenLearn,'b')
plt.title('X')
plt.subplot(122)
plt.hold('on')
plt.plot(zGivenLearn,betaYGivenLearn,'b')
plt.title('Y')  


numRun=500
se= tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
se.run(iniBTL)

costRec=[]
for _ in xrange(numRun):
    dataLattice,dataBeam=RandItemMulti(numItem,numSample,numQuadHigh)
    se.run(optBTL,feed_dict={xInput:dataBeam.reshape(numItem,weightSize[0]),yInput:dataLattice.reshape(numItem,weightSize[-1])})
    T2=se.run(costFunc,feed_dict={xInput:dataBeam.reshape(numItem,weightSize[0]),yInput:dataLattice.reshape(numItem,weightSize[-1])})
    costRec.append(T2)
    print str(np.round((np.float32(_)/np.float32(numRun))*100.))+'%'
    plt.figure('cost')
    numPlot=10
    plt.clf()
    plt.subplot(121)
    plt.plot(costRec)
    plt.subplot(122)
    plt.plot(costRec[np.max([0,_-numPlot]):_],'-*')
    title(_)
    plt.pause(0.05)


for _ in range(numRun):
    dataLatticeLearn=se.run(xOutputMat,feed_dict={xInput:dataBeamLearn.reshape(1,weightSize[0])})
    
    
    dataLattice,dataBeam=RoundItemMultiPack(numItem,dataBeamLearn,dataLatticeLearn)
    
    dataBeam[dataBeam==np.inf]=9.e300
    dataBeam[np.isnan(dataBeam)]=9.e300
    
    se.run(optBTL,feed_dict={xInput:dataBeam.reshape(numItem,weightSize[0]),yInput:dataLattice.reshape(numItem,weightSize[-1])})


###
    
    ZLearn,betaXLearn,betaYLearn=CalLatticeSingle(dataBeamLearn,dataLatticeLearn)
    
    driftL=dataLatticeLearn[:,0]
    quadK=dataLatticeLearn[:,1]
    quadL=dataLatticeLearn[:,2]
    
    print dataLatticeLearn
    
    plt.figure(1)
    plt.clf()
    plt.subplot(121)
    plt.hold('on')
    plt.plot(driftL,'b-*')
    plt.plot(quadK,'g-*')
    plt.plot(quadL,'r-*')
    plt.title(_)
    plt.subplot(222)
    plt.hold('on')
    plt.plot(zGivenLearn,betaXGivenLearn,'b')
    plt.plot(ZLearn,betaXLearn,'r')
    plt.title('X')
    plt.subplot(224)
    plt.hold('on')
    plt.plot(zGivenLearn,betaYGivenLearn,'b')
    plt.plot(ZLearn,betaYLearn,'r')
    plt.title('Y')    
    
    
    plt.pause(0.005)

se.close()

print('END')











