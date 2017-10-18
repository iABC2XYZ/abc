# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf
from tensorflow import fft

def Dct():
    pass

#def DST(a,n):
    

a= tf.constant([[1,2,3,4],[3,4,5,6]],dtype=tf.float32)

aShape=tf.shape(a)

n=aShape[0]

a3=tf.expand_dims(a,axis=0)

aUD=tf.image.flip_left_right(a3)
aUD_Neg=tf.constant([-1],dtype=tf.float32)*aUD[0]

y=tf.concat((a,aUD_Neg),0)

oneYImag=tf.constant([0.],dtype=tf.float32,shape=(4,4))
yComplex=tf.complex(y,oneYImag)

yy=fft(yComplex)

b=yy[1:n+1,:]/(-2.*tf.sqrt(tf.constant((-1.),dtype=tf.complex64)))

realB=tf.real(b)



#/(-2*sqrt(-1));


#aUD=tf.image.flip_up_down(tf.expand_dims(a))

'''
y=zeros(2*(n+1),m);
y(2:n+1,:)=aa;
y(n+3:2*(n+1),:)=-flipud(aa);
yy=fft(y);
b=yy(2:n+1,:)/(-2*sqrt(-1));
'''

sess=tf.Session()

sess.run(tf.global_variables_initializer())

print sess.run(a)
print sess.run(aUD_Neg)
print sess.run(y)
print sess.run(yComplex)
print sess.run(yy)
print ('------')
print sess.run(b)
print sess.run(realB)






