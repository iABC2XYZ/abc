#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 12:17:54 2017

@author: A
"""

import tensorflow as tf  # Version 1.0 or 0.12
import numpy as np
import matplotlib.pyplot as plt

import os

plt.close('all')

inSeq=20
outSeq=20
batchSize = 50
ioputDim=2         
hiddenDim =30  
numIterLearning = 1000


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



def GetDataXY(indexCode,isTrain, lenSeq,batchSize,ioputDim):
    openCode=ReadHistDataIndex(indexCode,'open')

    if len(lenSeq)==1:
        inSeq=outSeq=lenSeq
    else:
        inSeq,outSeq=lenSeq[0],lenSeq[1]
    
    nSeq=inSeq+outSeq
    nData=len(openCode)
    NChoose=nData-nSeq
    nChoose= np.random.randint(low=0,high=NChoose+1,size=batchSize*ioputDim)
    
    xBatch = []
    yBatch = []
    iChoose=-1
    for _ in xrange(batchSize):
        x_=np.empty((inSeq,ioputDim))
        y_=np.empty((outSeq,ioputDim))
        for nIO in xrange(ioputDim):
            iChoose+=1
            xTmp=openCode[nChoose[iChoose]:nChoose[iChoose]+inSeq]
            yTmp=openCode[nChoose[iChoose]+inSeq:nChoose[iChoose]+nSeq]
    
    
            x_[:,nIO]=xTmp
            y_[:,nIO]=yTmp
    
        xBatch.append(x_)
        yBatch.append(y_)
    
    xBatch = np.array(xBatch)
    yBatch = np.array(yBatch)
    # shape: (batchSize, lenSeq, outputDim)

    xBatch = np.array(xBatch).transpose((1, 0, 2))
    yBatch = np.array(yBatch).transpose((1, 0, 2))

    return xBatch, yBatch
  



def TensorFlowPredict(indexCode,inSeq,outSeq,batchSize,hiddenDim,ioputDim,numIterLearning):


    lenSeq = [inSeq,outSeq]                      ##############################
   
    outputDim = inputDim =ioputDim           ###################################
   
    layersStackedCount = 2
    
    # Optmizer:
    learningRate = 0.01  # Small lr helps not to diverge during training.

    lrDecay = 0.9  # default: 0.9 . Simulated annealing.
    momentumTF = 0.00  # default: 0.0 . momentumTF technique in weights update
    lambdaL2Reg = 0.003  # L2 regularization of weights - avoids overfitting
    
    
    try:
        tf.nn.seq2seq = tf.contrib.legacy_sreq2seq
        tf.nn.rnn_cell = tf.contrib.rnn
        tf.nn.rnn_cell.GRUCell = tf.contrib.rnn.GRUCell
        print("TensorFlow's version : 1.0 (or more)")
    except:
        print("TensorFlow's version : 0.12")
    
    
    
    
    tf.reset_default_graph()

    sess = tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
    
    with tf.variable_scope('Seq2seq'):
    
        # Encoder: inputs
        enc_inp = [
            tf.placeholder(tf.float32, shape=(
                None, inputDim), name="inp_{}".format(t))
            for t in range(inSeq)
        ]
    
        # Decoder: expected outputs
        expected_sparse_output = [
            tf.placeholder(tf.float32, shape=(None, outputDim),
                           name="expected_sparse_output_".format(t))
            for t in range(outSeq)
        ]
    

        dec_inp = [tf.zeros_like(
            enc_inp[0], dtype=np.float32, name="GO")] + enc_inp[:-1]
    
        # Create a `layersStackedCount` of stacked RNNs (GRU cells here).
        cells = []
        for i in range(layersStackedCount):
            with tf.variable_scope('RNN_{}'.format(i)):
                cells.append(tf.nn.rnn_cell.GRUCell(hiddenDim))
                # cells.append(tf.nn.rnn_cell.BasicLSTMCell(...))
        cell = tf.nn.rnn_cell.MultiRNNCell(cells)
    
        # For reshaping the input and output dimensions of the seq2seq RNN:
        w_in = tf.Variable(tf.random_normal([inputDim, hiddenDim]))
        b_in = tf.Variable(tf.random_normal([hiddenDim], mean=1.0))
        w_out = tf.Variable(tf.random_normal([hiddenDim, outputDim]))
        b_out = tf.Variable(tf.random_normal([outputDim]))
    
        reshaped_inputs = [tf.nn.relu(tf.matmul(i, w_in) + b_in) for i in enc_inp]
    

        dec_outputs, dec_memory = tf.nn.seq2seq.basic_rnn_seq2seq(
            enc_inp,
            dec_inp,
            cell
        )
    
        output_scale_factor = tf.Variable(1.0, name="Output_ScaleFactor")

        reshaped_outputs = [output_scale_factor *
                            (tf.matmul(i, w_out) + b_out) for i in dec_outputs]
    

    with tf.variable_scope('Loss'):
        # L2 loss
        output_loss = 0
        for _y, _Y in zip(reshaped_outputs, expected_sparse_output):
            output_loss += tf.reduce_mean(tf.nn.l2_loss(_y - _Y))
    
        reg_loss = 0
        for tf_var in tf.trainable_variables():
            if not ("Bias" in tf_var.name or "Output_" in tf_var.name):
                reg_loss += tf.reduce_mean(tf.nn.l2_loss(tf_var))
    
        loss = output_loss + lambdaL2Reg * reg_loss
    
    with tf.variable_scope('Optimizer'):
        optimizer = tf.train.RMSPropOptimizer(
            learningRate, decay=lrDecay, momentum=momentumTF)
        train_op = optimizer.minimize(loss)

    
    # Training
    train_losses = []
    test_losses = []
    
    sess.run(tf.global_variables_initializer())
    for t in range(numIterLearning + 1):

        X, Y = GetDataXY(indexCode,isTrain=True, lenSeq=lenSeq,batchSize=batchSize,ioputDim=ioputDim)
    
        feed_dict = {enc_inp[t]: X[t] for t in range(len(enc_inp))}
        feed_dict.update({expected_sparse_output[t]: Y[
                     t] for t in range(len(expected_sparse_output))})
        _, loss_t = sess.run([train_op, loss], feed_dict)
        train_loss=loss_t
        
        train_losses.append(train_loss)
        
        if t % 10 == 0:
            
            X, Y = GetDataXY(indexCode,isTrain=True, lenSeq=lenSeq,batchSize=batchSize,ioputDim=ioputDim)

            feed_dict = {enc_inp[t]: X[t] for t in range(len(enc_inp))}
            feed_dict.update({expected_sparse_output[t]: Y[
                             t] for t in range(len(expected_sparse_output))})
            loss_t = sess.run([loss], feed_dict)
            test_loss= loss_t[0]

            test_losses.append(test_loss)
            print("Step {}/{}, train loss: {}, \tTEST loss: {}".format(t,
                                                                           numIterLearning, train_loss, test_loss))
    
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
    
    X, Y = GetDataXY(indexCode,isTrain=True, lenSeq=lenSeq,batchSize=batchSize,ioputDim=ioputDim)
    feed_dict = {enc_inp[t]: X[t] for t in range(inSeq)}
    outputs = np.array(sess.run([reshaped_outputs], feed_dict)[0])
    
    for j in range(nb_predictions):
        plt.figure(figsize=(12, 3))
    
        for k in range(outputDim):
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
    
    
    
    ######################PREDICT:
    #X=Generate_x_data4Future(indexCode,isTrain=True, lenSeq=lenSeq,batchSize=batchSize,ioputDim=ioputDim)
    
    openCode=ReadHistDataIndex(indexCode,'open')

    if len(lenSeq)==1:
        inSeq=outSeq=lenSeq
    else:
        inSeq,outSeq=lenSeq[0],lenSeq[1]
    
    nData=len(openCode)
    X4Future=openCode[nData-inSeq::]
    
    #print X4FutureTmp.shape,X.shape
    
    X4FutureTmp=np.empty((inSeq,batchSize,ioputDim))
    for iB in xrange(batchSize):
        for iIO in xrange(ioputDim):
            X4FutureTmp[:,iB,iIO]=X4Future
    
    
    
    feed_dict = {enc_inp[t]: X4FutureTmp[t] for t in range(inSeq)}
    Y4FutureTmp = np.array(sess.run([reshaped_outputs], feed_dict)[0])
    Y4Future=Y4FutureTmp[:,0,0]
    
    plt.figure('FUTURE  @  JIANG PEIYONG')
    plt.clf()
    plt.plot(np.arange(inSeq),X4Future,'b-')
    plt.hold('on')
    plt.plot(np.arange(inSeq),X4Future,'b^')
    plt.plot(np.arange(inSeq)+inSeq,Y4Future,'r-')
    plt.plot(np.arange(inSeq)+inSeq,Y4Future,'ro')
    
    plt.figure('FUTURE (ALL)  @  JIANG PEIYONG')
    plt.clf()
    plt.plot(np.arange(nData),openCode,'b-')
    plt.hold('on')
    plt.plot(np.arange(inSeq)+nData,Y4Future,'r-')

    
###################################################################################


indexCode='300401'
TensorFlowPredict(indexCode,inSeq,outSeq,batchSize,hiddenDim,ioputDim,numIterLearning)











