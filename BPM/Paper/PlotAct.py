#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
@author: Peiyong Jiang
作者: 姜培勇
jiangpeiyong@impcas.ac.cn

本文件解释：



"""




import tensorflow as tf;  
import numpy as np;  
import matplotlib.pyplot as plt;  
  
x = np.linspace(-10,10,100)  
y1 = tf.nn.sigmoid(x)  
y2 = tf.nn.tanh(x)  
y3 = tf.nn.elu(x)  
y4 = tf.nn.softplus(x)  
y5 = tf.nn.softsign(x)  
y6 = tf.nn.relu(x)  
y7 = tf.nn.relu6(x)  
  
with tf.Session() as sess:  
    sess.run(tf.initialize_all_variables())  
    ax1 = plt.subplot2grid((4,2), (0,0))  
    ax1.plot(x, sess.run(y1))  
    ax1.set_title('sigmoid')  
  
    ax2 = plt.subplot2grid((4,2), (0,1))  
    ax2.plot(x, sess.run(y2))  
    ax2.set_title('tanh')  
  
    ax3 = plt.subplot2grid((4,2), (1,0))  
    ax3.plot(x, sess.run(y3))  
    ax3.set_title('elu')  
  
    ax4 = plt.subplot2grid((4,2), (1,1))  
    ax4.plot(x, sess.run(y4))  
    ax4.set_title('softplus')  
  
    ax5 = plt.subplot2grid((4,2), (2,0))  
    ax5.plot(x, sess.run(y5))  
    ax5.set_title('softsign')  
  
    ax6 = plt.subplot2grid((4,2), (2,1))  
    ax6.plot(x, sess.run(y6))  
    ax6.set_title('relu')  
  
    ax7 = plt.subplot2grid((4,2), (3,0))  
    ax7.plot(x, sess.run(y7))  
    ax7.set_title('relu6')  
  
    plt.show()  




with tf.Session() as sess:  
    sess.run(tf.initialize_all_variables())  
    h=plt.figure(1001)
    plt.plot(x, sess.run(y1))
    plt.xticks((-10,-5, 0, 5,10), ('-10','-5', '0','5' ,'10'), color='k', size=20)
    plt.yticks((0, 0.5, 1), ('0', '0.5' ,'1'), color='k', size=20)
    h.savefig('sigmoid.png')

    h=plt.figure(1002)
    plt.plot(x, sess.run(y2))  
    plt.xticks((-10,-5, 0, 5,10), ('-10','-5', '0','5' ,'10'), color='k', size=20)
    plt.yticks((-1, 0, 1), ('-1', '0' ,'1'), color='k', size=20)
    h.savefig('tanh.png')

  
    h=plt.figure(1003)
    plt.plot(x, sess.run(y3))  
    plt.xticks((-10,-5, 0, 5,10), ('-10','-5', '0','5' ,'10'), color='k', size=20)
    plt.yticks((-1, 0,5, 10), ('-1', '0' ,'5','10'), color='k', size=20)
    h.savefig('elu.png')
  
    h=plt.figure(1004)
    plt.plot(x, sess.run(y4)) 
    plt.xticks((-10,-5, 0, 5,10), ('-10','-5', '0','5' ,'10'), color='k', size=20)
    plt.yticks((0,5, 10), ('0' ,'5','10'), color='k', size=20)
    h.savefig('softplus.png')
      

    h=plt.figure(1005)
    plt.plot(x, sess.run(y5))  
    plt.xticks((-10,-5, 0, 5,10), ('-10','-5', '0','5' ,'10'), color='k', size=20)
    plt.yticks((-1,0, 1), ('-1' ,'0','1'), color='k', size=20)
    h.savefig('softsign.png')
          
    
  
    h=plt.figure(1006)
    plt.plot(x, sess.run(y6))  
    plt.xticks((-10,-5, 0, 5,10), ('-10','-5', '0','5' ,'10'), color='k', size=20)
    plt.yticks((0,5, 10), ('0' ,'5','10'), color='k', size=20)
    h.savefig('relu.png')
          
    
    h=plt.figure(1007)
    plt.plot(x, sess.run(y7))  
    plt.xticks((-10,-5, 0, 5,10), ('-10','-5', '0','5' ,'10'), color='k', size=20)
    plt.yticks((0,3, 6), ('0' ,'3','6'), color='k', size=20)
    h.savefig('relu6.png')
    plt.show()  







