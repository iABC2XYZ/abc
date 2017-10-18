# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf
from tensorflow import fft
import numpy as np
from scipy.fftpack import dst,dct

def Dst(a):
    aShape=tf.shape(a)
    
    n=aShape[0]
    
    a3=tf.expand_dims(a,axis=0)
    
    aUD=tf.image.flip_left_right(a3)
    aUD_Neg=tf.constant([-1],dtype=tf.float32)*aUD[0]
    
    y=tf.concat((a,aUD_Neg),0)
    
    oneYImag=tf.constant([0.],dtype=tf.float32,shape=(6,4))
    yComplex=tf.complex(y,oneYImag)
    
    yy=fft(yComplex)
    
    b=yy[1:n+1,:]/(-2.*tf.sqrt(tf.constant((-1.),dtype=tf.complex64)))
    
    realB=tf.real(b)
    return realB


a=np.float32(np.random.random((3,4)))
aFFT_NP=np.fft.fft(a)
aDST_NP=dst(a)

aImag=np.zeros_like(a)
aComplex=tf.complex(a,aImag)
aFFT_TF=tf.fft(aComplex)
A=tf.placeholder(shape=(3,4),dtype=tf.float32)
aDST_TF=Dst(A)

#----------------------------


aShape=tf.shape(A)
    
n=aShape[0]

a3=tf.expand_dims(A,axis=0)

aUD=tf.image.flip_left_right(a3)
aUD_Neg=tf.constant([-1],dtype=tf.float32)*aUD[0]

y=tf.concat((A,aUD_Neg),0)

oneYImag=tf.constant([0.],dtype=tf.float32,shape=(6,4))
yComplex=tf.complex(y,oneYImag)

yy=fft(yComplex)

bZeroReal=tf.constant([0.],dtype=tf.float32,shape=(3,4))
bZeroImag=tf.constant([1.],dtype=tf.float32,shape=(3,4))
bComplex=tf.complex(bZeroReal,bZeroImag)

b=yy[1:n+1,:]/2.*bComplex

realB=tf.real(b)

#



sess=tf.Session()

sess.run(tf.global_variables_initializer())

print type(a[0])

print a
print "----------"
print sess.run(aComplex)
print "=========="
print aFFT_NP
print "----------"
print sess.run(aFFT_TF)
print "=========="
print aDST_NP
print "----------"
print sess.run(aDST_TF,feed_dict={A:a})

print "=========="
print sess.run(y,feed_dict={A:a})
print "----------"
print sess.run(yComplex,feed_dict={A:a})
print "----------"
print sess.run(yy,feed_dict={A:a})
print "----------"
print sess.run(b,feed_dict={A:a})


'''
print sess.run(a)
print sess.run(aUD_Neg)
print sess.run(y)
print sess.run(yComplex)
print sess.run(yy)
print ('------')
print sess.run(b)
print sess.run(realB)
'''






