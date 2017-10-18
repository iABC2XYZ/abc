# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf
from tensorflow import fft
import numpy as np
from scipy.fftpack import dst,dct

def Dst(x,N):
    pass

  
    '''
    tf.reduce_sum(x[n]*tf.sin(np.pi*(k+1.)*(n+1.)/(N+1.))))
    
    k=
    
    y=[]
    for k in range(N):
        for n in range(N):
            y=tf.concat(y,tf.reduce_sum(x[n]*tf.sin(np.pi*(k+1.)*(n+1.)/(N+1.)))),0)
    return y
    '''

N=4

k=np.linspace(1,N,N)
n=k
K,N=np.meshgrid(k,n)
KN=K*N
knSin=np.sin(np.pi*KN/(N+1.))

print k,n
print '-----------'
print KN
print KN/(N+1.)
print knSin

"""
a=np.float32(np.random.random((4)))
aDst=dst(a)

x=tf.placeholder(shape=[4],dtype=tf.float32)
xDst=Dst(x,4)

sess=tf.Session()

sess.run(tf.global_variables_initializer())


print a
print aDst
print sess.run(xDst,feed_dict={x:a})

"""






