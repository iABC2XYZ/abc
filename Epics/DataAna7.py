#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:44:34 2017

@author: p
"""

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




def getDataRow(exData,sizeRow):
    numEx=np.shape(exData)[0]
    idChoose=np.random.randint(0,high=numEx,size=(sizeRow))
    yCHV=np.reshape(exData[idChoose,0:14],(sizeRow,7,2))
    xBPM=np.reshape(exData[idChoose,14:24],(sizeRow,5,2))
    return xBPM,yCHV



def conv1d(x, W):
    '''
    卷积层接下来要重复使用,tf.nn.conv2d是Tensorflow中的二维卷积函数,
    :param x: 输入 例如[5, 5, 1, 32]代表 卷积核尺寸为5x5,1个通道,32个不同卷积核
    :param W: 卷积的参数
        strides:代表卷积模板移动的步长,都是1代表不遗漏的划过图片的每一个点.
        padding:代表边界处理方式,SAME代表输入输出同尺寸
    :return:
    '''
    return tf.nn.conv1d(x, W, stride=1, padding="SAME")


exDataTmp=np.loadtxt('Rec.dat')
exDataSize=np.size(exDataTmp)/25*25
exData=exDataTmp[0:exDataSize:].reshape(exDataSize/25,25)

flagWrite=0
if flagWrite==1:
    with open('Rec.BK','w+') as f:
        for i in range(exDataSize/25):
            strLine=str(exData[i,:]).replace('\n',' ')[1:-1:]+'\n'
            f.writelines(strLine)
        
    

bpm=tf.placeholder(tf.float32,shape=(None,5,2))
cHV=tf.placeholder(tf.float32,shape=(None,7,2))


xInput=bpm
yInput=cHV

w1_1= GenWeight([1,2,4])
b1_1=GenBias([4])

w1_2= GenWeight([2,2,4])
b1_2=GenBias([4])

w1_3= GenWeight([3,2,4])
b1_3=GenBias([4])


x1_1=tf.nn.relu(conv1d(xInput, w1_1)+b1_1)
x1_2=tf.nn.relu(conv1d(xInput, w1_2)+b1_2)
x1_3=tf.nn.relu(conv1d(xInput, w1_3)+b1_3)

x1=tf.concat((tf.concat((x1_1,x1_2),axis=2),x1_3),axis=2)

##

w2= GenWeight([2,12,12])
b2=GenBias([12])

x2=tf.nn.relu(conv1d(x1, w2)+b2+x1)

##

w3= GenWeight([1,12,12])
b3=GenBias([12])

x3=tf.nn.relu(conv1d(x2, w3)+b3+x2)


##
w4= GenWeight([3,12,12])
b4=GenBias([12])

x4=tf.nn.relu(conv1d(x3, w4)+b4+x3)


##

w5= GenWeight([1,12,12])
b5=GenBias([12])

x5=tf.nn.relu(conv1d(x4, w5)+b5+x4)


##

w6= GenWeight([2,12,12])
b6=GenBias([12])

x6=tf.nn.relu(conv1d(x5, w6)+b6+x5)


##
w7= GenWeight([1,12,12])
b7=GenBias([12])

x7=tf.nn.relu(conv1d(x6, w7)+b7+x6)

##
w8= GenWeight([1,12,7])
b8=GenBias([7])

x8=conv1d(x7, w8)+b8

##
x9=tf.reshape(x8,(-1,7*5))


##
w10= GenWeight([35,14])
b10=GenBias([14])

x10=tf.matmul(x9,w10)+b10


##

xFinal=x10

xOutput=tf.reshape(xFinal,(-1,14))
yOutput=tf.reshape(yInput,(-1,14))
#xOutput=tf.nn.softmax(tf.reshape(xFinal,(-1,14)))
#yOutput=tf.nn.softmax(tf.reshape(yInput,(-1,14)))


#lossFn=-tf.reduce_mean(xOutput*tf.log(yOutput))
lossFn=tf.reduce_mean(tf.square(xOutput-yOutput))


trainBPM=tf.train.AdamOptimizer(0.01)
optBPM=trainBPM.minimize(lossFn)

iniBPM=tf.global_variables_initializer()


try:
    if vars().has_key('se'):
        se.close()
except:
    pass
se= tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
se.run(iniBPM)


nIt=1e7
sizeRow=50
stepLossRec=600
nLossRec=np.int32(nIt/stepLossRec+1)

lossRec=np.zeros((nLossRec))

iRec=0
for i in range(np.int32(nIt)):
    xBPM,yCHV=getDataRow(exData,sizeRow)
    se.run(optBPM,feed_dict={bpm:xBPM,cHV:yCHV})
    
    if i % stepLossRec==0:
        lossRecTmp=se.run(lossFn,feed_dict={bpm:xBPM,cHV:yCHV})
        lossRec[iRec]=lossRecTmp
        iRec+=1

        print lossRecTmp
                
        plt.figure(1)
        plt.hold
        plt.plot(iRec,lossRecTmp,'*b')
        plt.grid('on')
        plt.title(i)
        plt.pause(0.05)
        
        
        xBPM,yCHV=getDataRow(exData,5)
        yCHV_Cal=se.run(xFinal,feed_dict={bpm:xBPM})
        plt.figure(2)
        plt.clf()
        plt.hold
        #plt.plot(yCHV[0,:],'b*')
        #plt.plot(yCHV_Cal[0,:],'r*')
        #plt.plot(yCHV[1,:],'bo')
        #plt.plot(yCHV_Cal[1,:],'ro')
        #plt.plot(yCHV[2,:],'b^')
        #plt.plot(yCHV_Cal[2,:],'r^')
        #plt.plot(yCHV[3,:],'bs')
        #plt.plot(yCHV_Cal[3,:],'rs')
        plt.plot(np.reshape(yCHV[4,:],(14)),'bd')
        plt.plot(yCHV_Cal[4,:],'rd')        
        plt.title(i)
        plt.pause(0.05)
    
    
#se.close()


xBPMReal_1=np.ones((5,2))*0.
xBPMReal_2=np.ones((5,2))*3.
xBPMReal_3=np.ones((5,2))*(-3.)
xBPMReal_4=np.ones((5,2))
xBPMReal_4[:,0]=xBPMReal_4[:,0]*3.
xBPMReal_4[:,1]=xBPMReal_4[:,1]*(-3.)

xBPMReal=np.zeros((4,5,2))
xBPMReal[0,:,:]=xBPMReal_1
xBPMReal[1,:,:]=xBPMReal_2
xBPMReal[2,:,:]=xBPMReal_3
xBPMReal[3,:,:]=xBPMReal_4

yCHV_Cal4Real=se.run(xFinal,feed_dict={bpm:xBPMReal})

yCHV_Cal4Real_1=np.reshape(yCHV_Cal4Real[0,::],(7,2))
yCHV_Cal4Real_2=np.reshape(yCHV_Cal4Real[1,::],(7,2))
yCHV_Cal4Real_3=np.reshape(yCHV_Cal4Real[2,::],(7,2))
yCHV_Cal4Real_4=np.reshape(yCHV_Cal4Real[3,::],(7,2))

print '----------------- yCHV_Cal4Real_1 --------------------------'
print yCHV_Cal4Real_1
print '----------------- yCHV_Cal4Real_2 --------------------------'
print yCHV_Cal4Real_2
print '----------------- yCHV_Cal4Real_3 --------------------------'
print yCHV_Cal4Real_3
print '----------------- yCHV_Cal4Real_4 --------------------------'
print yCHV_Cal4Real_4

















