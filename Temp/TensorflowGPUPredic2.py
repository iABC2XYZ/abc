#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 12:17:54 2017

@author: A
"""

import tensorflow as tf  # Version 1.0 or 0.12
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import os

plt.close('all')

inSeq=10
outSeq=3
batch_size = 50  # Low value used for live demo purposes - 100 and 1000 would be possible too, crank that up!
ioput_dim=2                    # Output dimension (e.g.: multiple signals at once, tied in time)
hidden_dim = 50  # Count of hidden neurons in the recurrent units.



def ReadHistDataIndex(indexCode,kindCode):
    
    fileName='./data/'+kindCode.lower()+'/'+indexCode+'.'+kindCode.lower()
    if(kindCode.lower()=='date'):
        if  not (os.path.exists(fileName)):
            return '3000-01-01'
        with open(fileName,'r') as fid:
            dataCodeTmp=fid.readlines()
        nDataCodeTmp=len(dataCodeTmp)
        dataCode=np.copy(dataCodeTmp)
        for nLine in xrange(nDataCodeTmp):
            dataCode[nLine]=dataCodeTmp[nDataCodeTmp-nLine-1]
    else:
        if  not (os.path.exists(fileName)):
            return [0]
        dataCode= np.loadtxt(fileName)
        if np.shape(dataCode)==():
            return [0]
        
        dataCode=np.flip(np.loadtxt(fileName),0)
              
    return dataCode



def generate_x_y_data(indexCode,isTrain, seq_length,batch_size,ioput_dim):
    openCode=ReadHistDataIndex(indexCode,'open')

    if len(seq_length)==1:
        inSeq=outSeq=seq_length
    else:
        inSeq,outSeq=seq_length[0],seq_length[1]
        
    print openCode
    
    
    
    
    '''
    
    batch_x = []
    batch_y = []
    
    for _ in range(batch_size):
        x_=np.empty((inSeq,ioput_dim))
        y_=np.empty((outSeq,ioput_dim))
        for nIO in xrange(ioput_dim):
            rand = random.random() * 2 * math.pi
    
            sig = np.sin(np.linspace(0.0 * math.pi + rand,
                                      3.0 * math.pi + rand, inSeq+outSeq))
            xTmp=sig[:inSeq]
            yTmp=sig[inSeq:]
            x_[:,nIO]=xTmp
            y_[:,nIO]=yTmp
    
        batch_x.append(x_)
        batch_y.append(y_)


    batch_x = np.array(batch_x)
    batch_y = np.array(batch_y)
    # shape: (batch_size, seq_length, output_dim)

    batch_x = np.array(batch_x).transpose((1, 0, 2))
    batch_y = np.array(batch_y).transpose((1, 0, 2))
    # shape: (seq_length, batch_size, output_dim)

    return batch_x, batch_y
    '''


seq_length=[inSeq,outSeq]
generate_x_y_data('603505',isTrain=True, seq_length=seq_length,batch_size=batch_size,ioput_dim=ioput_dim)



















'''

def generate_x_y_data(isTrain, seq_length,batch_size,ioput_dim):
    """
    Data for exercise 1.

    returns: tuple (X, Y)
        X is a sine and a cosine from 0.0*pi to 1.5*pi
        Y is a sine and a cosine from 1.5*pi to 3.0*pi
    Therefore, Y follows X. There is also a random offset
    commonly applied to X an Y.

    The returned arrays are of shape:
        (seq_length, batch_size, output_dim)
        Therefore: (10, batch_size, 2)

    For this exercise, let's ignore the "isTrain"
    argument and test on the same data.
    """
    
    
    if len(seq_length)==1:
        inSeq=outSeq=seq_length
    else:
        inSeq,outSeq=seq_length[0],seq_length[1]
    
    batch_x = []
    batch_y = []
    
    for _ in range(batch_size):
        x_=np.empty((inSeq,ioput_dim))
        y_=np.empty((outSeq,ioput_dim))
        for nIO in xrange(ioput_dim):
            rand = random.random() * 2 * math.pi
    
            sig = np.sin(np.linspace(0.0 * math.pi + rand,
                                      3.0 * math.pi + rand, inSeq+outSeq))
            xTmp=sig[:inSeq]
            yTmp=sig[inSeq:]
            x_[:,nIO]=xTmp
            y_[:,nIO]=yTmp
    
        batch_x.append(x_)
        batch_y.append(y_)


    batch_x = np.array(batch_x)
    batch_y = np.array(batch_y)
    # shape: (batch_size, seq_length, output_dim)

    batch_x = np.array(batch_x).transpose((1, 0, 2))
    batch_y = np.array(batch_y).transpose((1, 0, 2))
    # shape: (seq_length, batch_size, output_dim)

    return batch_x, batch_y

'''






'''



def TensorFlowPredict(indexCode,inSeq,outSeq,batch_size,hidden_dim,ioput_dim):

    #inSeq=10
    #outSeq=3
    seq_length = [inSeq,outSeq]                      ##############################
    
    #batch_size = 50  # Low value used for live demo purposes - 100 and 1000 would be possible too, crank that up!
    
    # Output dimension (e.g.: multiple signals at once, tied in time)
    #ioput_dim=5
    output_dim = input_dim =ioput_dim           ###################################
    
    #hidden_dim = 50  # Count of hidden neurons in the recurrent units.
    # Number of stacked recurrent cells, on the neural depth axis.
    layers_stacked_count = 2
    
    # Optmizer:
    learning_rate = 0.007  # Small lr helps not to diverge during training.
    # How many times we perform a training step (therefore how many times we
    # show a batch).
    nb_iters = 100
    lr_decay = 0.92  # default: 0.9 . Simulated annealing.
    momentum = 0.5  # default: 0.0 . Momentum technique in weights update
    lambda_l2_reg = 0.003  # L2 regularization of weights - avoids overfitting
    
    
    try:
        tf.nn.seq2seq = tf.contrib.legacy_seq2seq
        tf.nn.rnn_cell = tf.contrib.rnn
        tf.nn.rnn_cell.GRUCell = tf.contrib.rnn.GRUCell
        print("TensorFlow's version : 1.0 (or more)")
    except:
        print("TensorFlow's version : 0.12")
    
    
    
    
    tf.reset_default_graph()
    # sess.close()
    sess = tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
    
    with tf.variable_scope('Seq2seq'):
    
        # Encoder: inputs
        enc_inp = [
            tf.placeholder(tf.float32, shape=(
                None, input_dim), name="inp_{}".format(t))
            for t in range(inSeq)
        ]
    
        # Decoder: expected outputs
        expected_sparse_output = [
            tf.placeholder(tf.float32, shape=(None, output_dim),
                           name="expected_sparse_output_".format(t))
            for t in range(outSeq)
        ]
    
        # Give a "GO" token to the decoder.
        # You might want to revise what is the appended value "+ enc_inp[:-1]".
        dec_inp = [tf.zeros_like(
            enc_inp[0], dtype=np.float32, name="GO")] + enc_inp[:-1]
    
        # Create a `layers_stacked_count` of stacked RNNs (GRU cells here).
        cells = []
        for i in range(layers_stacked_count):
            with tf.variable_scope('RNN_{}'.format(i)):
                cells.append(tf.nn.rnn_cell.GRUCell(hidden_dim))
                # cells.append(tf.nn.rnn_cell.BasicLSTMCell(...))
        cell = tf.nn.rnn_cell.MultiRNNCell(cells)
    
        # For reshaping the input and output dimensions of the seq2seq RNN:
        w_in = tf.Variable(tf.random_normal([input_dim, hidden_dim]))
        b_in = tf.Variable(tf.random_normal([hidden_dim], mean=1.0))
        w_out = tf.Variable(tf.random_normal([hidden_dim, output_dim]))
        b_out = tf.Variable(tf.random_normal([output_dim]))
    
        reshaped_inputs = [tf.nn.relu(tf.matmul(i, w_in) + b_in) for i in enc_inp]
    
        # Here, the encoder and the decoder uses the same cell, HOWEVER,
        # the weights aren't shared among the encoder and decoder, we have two
        # sets of weights created under the hood according to that function's def.
        dec_outputs, dec_memory = tf.nn.seq2seq.basic_rnn_seq2seq(
            enc_inp,
            dec_inp,
            cell
        )
    
        output_scale_factor = tf.Variable(1.0, name="Output_ScaleFactor")
        # Final outputs: with linear rescaling similar to batch norm,
        # but without the "norm" part of batch normalization hehe.
        reshaped_outputs = [output_scale_factor *
                            (tf.matmul(i, w_out) + b_out) for i in dec_outputs]
    
    
    
    
    with tf.variable_scope('Loss'):
        # L2 loss
        output_loss = 0
        for _y, _Y in zip(reshaped_outputs, expected_sparse_output):
            output_loss += tf.reduce_mean(tf.nn.l2_loss(_y - _Y))
    
        # L2 regularization (to avoid overfitting and to have a  better
        # generalization capacity)
        reg_loss = 0
        for tf_var in tf.trainable_variables():
            if not ("Bias" in tf_var.name or "Output_" in tf_var.name):
                reg_loss += tf.reduce_mean(tf.nn.l2_loss(tf_var))
    
        loss = output_loss + lambda_l2_reg * reg_loss
    
    with tf.variable_scope('Optimizer'):
        optimizer = tf.train.RMSPropOptimizer(
            learning_rate, decay=lr_decay, momentum=momentum)
        train_op = optimizer.minimize(loss)
    
    
    
    
    # Training
    train_losses = []
    test_losses = []
    
    sess.run(tf.global_variables_initializer())
    for t in range(nb_iters + 1):
        #train_loss = train_batch(batch_size, seq_length, ioput_dim)
        
        X, Y = generate_x_y_data(isTrain=True, seq_length=seq_length,batch_size=batch_size,ioput_dim=ioput_dim)
        #print X.shape, Y.shape
    
    
        feed_dict = {enc_inp[t]: X[t] for t in range(len(enc_inp))}
        feed_dict.update({expected_sparse_output[t]: Y[
                     t] for t in range(len(expected_sparse_output))})
        _, loss_t = sess.run([train_op, loss], feed_dict)
        train_loss=loss_t
        
        train_losses.append(train_loss)
        
        if t % 10 == 0:
            # Tester
            #test_loss = test_batch(batch_size)
            
            X, Y = generate_x_y_data(isTrain=False, seq_length=seq_length,batch_size=batch_size,ioput_dim=ioput_dim)

            feed_dict = {enc_inp[t]: X[t] for t in range(len(enc_inp))}
            feed_dict.update({expected_sparse_output[t]: Y[
                             t] for t in range(len(expected_sparse_output))})
            loss_t = sess.run([loss], feed_dict)
            test_loss= loss_t[0]
                    
            
            
            
            test_losses.append(test_loss)
            print("Step {}/{}, train loss: {}, \tTEST loss: {}".format(t,
                                                                           nb_iters, train_loss, test_loss))
    
    print("Fin. train loss: {}, \tTEST loss: {}".format(train_loss, test_loss))
    
    
    
    
    # Plot loss over time:
    plt.figure(figsize=(12, 6))
    plt.plot(
        np.array(range(0, len(test_losses))) /
        float(len(test_losses) - 1) * (len(train_losses) - 1),
        np.log(test_losses),
        label="Test loss"
    )
    plt.plot(
        np.log(train_losses),
        label="Train loss"
    )
    plt.title("Training errors over time (on a logarithmic scale)")
    plt.xlabel('Iteration')
    plt.ylabel('log(Loss)')
    plt.legend(loc='best')
    plt.show()
    
    
    
    
    # Test          ############################
    nb_predictions = 5
    print("Let's visualize {} predictions with our signals:".format(nb_predictions))
    
    X, Y = generate_x_y_data(isTrain=False, seq_length=seq_length, batch_size=nb_predictions,ioput_dim=ioput_dim)
    feed_dict = {enc_inp[t]: X[t] for t in range(inSeq)}
    outputs = np.array(sess.run([reshaped_outputs], feed_dict)[0])
    
    for j in range(nb_predictions):
        plt.figure(figsize=(12, 3))
    
        for k in range(output_dim):
            past = X[:, j, k]
            expected = Y[:, j, k]
            pred = outputs[:, j, k]
    
            label1 = "Seen (past) values" if k == 0 else "_nolegend_"
            label2 = "True future values" if k == 0 else "_nolegend_"
            label3 = "Predictions" if k == 0 else "_nolegend_"
            plt.plot(range(len(past)), past, "o--b", label=label1)
            plt.plot(range(len(past), len(expected) + len(past)),
                     expected, "x--b", label=label2)
            plt.plot(range(len(past), len(pred) + len(past)),
                     pred, "o--y", label=label3)
    
        plt.legend(loc='best')
        plt.title("Predictions v.s. true values")
        plt.show()
    
    print("Reminder: the signal can contain many dimensions at once.")
    print("In that case, signals have the same color.")
    print("In reality, we could imagine multiple stock market symbols evolving,")
    print("tied in time together and seen at once by the neural network.")
    
    
    
    ################################################################################

indexCode='0000'
TensorFlowPredict(indexCode,inSeq,outSeq,batch_size,hidden_dim,ioput_dim)


'''












