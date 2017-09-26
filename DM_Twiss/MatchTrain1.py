#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:37:16 2017
Author: Peiyong Jiang : jiangpeiyong@impcas.ac.cn
Function:
    旋转+拉伸：Qinqing  AdadeltaOptimizer
    

"""


import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

plt.close('all')

emitXI=1.
alphaXI=1.
betaXI=np.sqrt(2.)
alphaXO=0.
betaXO=1.



emitYI=1.
alphaYI=-1.
betaYI=np.sqrt(2.)
alphaYO=0.
betaYO=1.

gammaXI=(1.+alphaXI**2)/betaXI
gammaYI=(1.+alphaYI**2)/betaYI

sigmaXI=np.array([[betaXI,-alphaXI],[-alphaXI,gammaXI]])*emitXI
sigmaYI=np.array([[betaYI,-alphaYI],[-alphaYI,gammaYI]])*emitYI
sigmaO=np.zeros([2,2])
sigma0=np.vstack((np.hstack((sigmaXI,sigmaO)),np.hstack((sigmaO,sigmaYI))))

mu0=[0.,0.,0.,0.]

numPart=np.int32(1e5);
X=np.random.multivariate_normal(mu0,sigma0,numPart).T

plt.figure(1)
plt.clf
plt.subplot(121)
plt.plot(X[0,:],X[1,:],'b.')
plt.axis('equal')
plt.subplot(122)
plt.plot(X[2,:],X[3,:],'r.')
plt.axis('equal')

print(sigma0)


##

K1=tf.Variable(tf.random_normal([1,1]))
K2=tf.Variable(tf.random_normal([1,1]))
K3=tf.Variable(tf.random_normal([1,1]))
K4=tf.Variable(tf.random_normal([1,1]))

def Quad(K):
    O=tf.constant([0.],shape=[1,1])
    I=tf.constant([1.],shape=[1,1])
    
    M_Col_1=tf.concat([I,K,O,O],0)

    M_Col_2=tf.concat([O,I,O,O],0)
    
    M_Col_3=tf.concat([O,O,I,K],0)
    
    M_Col_4=tf.concat([O,O,O,I],0)
    
    M=tf.concat([M_Col_1,M_Col_2,M_Col_3,M_Col_4],1)
    return M
    
def Drift(L):
    O=tf.constant([0.],shape=[1,1])
    I=tf.constant([1.],shape=[1,1])
    
    M_Col_1=tf.concat([I,O,O,O],0)
    M_Col_2=tf.concat([L,I,O,O],0)
    M_Col_3=tf.concat([O,O,I,O],0)
    M_Col_4=tf.concat([O,O,L,I],0)
    
    M=tf.concat([M_Col_1,M_Col_2,M_Col_3,M_Col_4],1)
    return M


def TwissO(alphaXO,betaXO,alphaYO,betaYO):
    
    O=tf.constant([0.],shape=[1,1])
    I=tf.constant([1.],shape=[1,1])
    betaX=tf.constant([betaXO],shape=[1,1])
    alphaX=tf.constant([alphaXO],shape=[1,1])
    betaY=tf.constant([betaYO],shape=[1,1])
    alphaY=tf.constant([alphaYO],shape=[1,1])    
    
    M_Col_1=tf.concat([I/tf.sqrt(betaX),alphaX/tf.sqrt(betaX),O,O],0)
    M_Col_2=tf.concat([O,tf.sqrt(betaX),O,O],0)
    M_Col_3=tf.concat([O,O,I/tf.sqrt(betaY),alphaY/tf.sqrt(betaY)],0)
    M_Col_4=tf.concat([O,O,O,tf.sqrt(betaY)],0)
    M=tf.concat([M_Col_1,M_Col_2,M_Col_3,M_Col_4],1)
    return M



L=tf.constant([0.1],shape=[1,1])
##

D1=Drift(L)
Q1=Quad(K1)
D2=Drift(L)
Q2=Quad(K2)
D3=Drift(L)
Q3=Quad(K3)
D4=Drift(L)
Q4=Quad(K4)
D5=Drift(L)

MTwiss=TwissO(alphaXO,betaXO,alphaYO,betaYO)

xI=tf.placeholder(tf.float32,[4,None])


xD1=tf.matmul(D1,xI)
xQ1=tf.matmul(Q1,xD1)
xD2=tf.matmul(D2,xQ1)
xQ2=tf.matmul(Q2,xD2)
xD3=tf.matmul(D3,xQ2)
xQ3=tf.matmul(Q3,xD3)
xD4=tf.matmul(D4,xQ3)
xQ4=tf.matmul(Q4,xD4)
xD5=tf.matmul(D5,xQ4)
xO=tf.matmul(MTwiss,xD5)




#xR=(xO[0]**2+xO[1]**2)*(xO[2]**2+xO[3]**2)
#xR=(xO[2]**2+xO[3]**2)
#xR=(xO[0]+xO[2])**2+(xO[1]+xO[3])**2

#r=tf.random_uniform([1,1],minval=0.,maxval=1.)
#I=tf.constant([1.],shape=[1,1])
#xR=r*(xO[0]**2+xO[1]**2)+(I-r)*(xO[2]**2+xO[3]**2)

#xR=xO[0]**2+xO[1]**2+xO[2]**2+xO[3]**2

r_x=tf.random_uniform([1,1],minval=0.,maxval=1.)
r_xp=tf.random_uniform([1,1],minval=0.,maxval=1.)
r_y=tf.random_uniform([1,1],minval=0.,maxval=1.)
r_yp=tf.random_uniform([1,1],minval=0.,maxval=1.)

#xR=r_x*xO[0]**2+r_xp*xO[1]**2+r_y*xO[2]**2+r_yp*xO[3]**2
xR=tf.abs((xO[0]+1.)*(xO[1]+1.)*(xO[2]+1.)*(xO[3]+1.))

lossR=xR

rateLearn=0.5
optMethod=tf.train.AdamOptimizer(rateLearn)
train=optMethod.minimize(lossR)



sess = tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))

sess.run(tf.global_variables_initializer())



sizeBatch=512
numTrain=20000
for _ in xrange(numTrain):
    
    pickBatch=np.int32(np.random.rand(sizeBatch)*numPart)
    xFeed=X[:,pickBatch]
    
    sess.run(train,feed_dict={xI:xFeed})
    
    if (_ % 500 ==0):
        print(np.int32(np.float32(_)/np.float32(numTrain)*100.))



zReal=sess.run(xO,feed_dict={xI:X})

plt.figure(2)
plt.clf
plt.subplot(121)
plt.plot(zReal[0,:],zReal[1,:],'b.')
plt.axis('equal')
plt.subplot(122)
plt.plot(zReal[2,:],zReal[3,:],'r.')
plt.axis('equal')



print(sess.run(MTwiss))



"""

plt.figure(10)
plt.hold
plt.plot(zReal[0,:],zReal[1,:],'r.')
plt.plot(X[0,:],X[1,:],'b.')
#plt.plot(zReal[0,:],zReal[1,:],'r.')
plt.axis('equal')


plt.figure(11)
plt.hold
#plt.plot(zReal[0,:],zReal[1,:],'r.')
plt.plot(X[0,:],X[1,:],'b.')
plt.plot(zReal[0,:],zReal[1,:],'r.')
plt.axis('equal')


xOringinCov=np.cov(X)
emitXOrigin=np.sqrt(np.linalg.det(xOringinCov))


zRealCov=np.cov(zReal)
emitXReal=np.sqrt(np.linalg.det(zRealCov))


print('+++++++++++++++++++')
print(sess.run(P))
print('_________________________')

print(xOringinCov)

print(emitXOrigin)

print('________________________')

print(zRealCov)

print(emitXReal)

"""


plt.show()