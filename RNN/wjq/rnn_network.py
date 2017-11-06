#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function, division
import numpy as np
import tensorflow as tf

NUM_EPOCHS = 1000
LEARNING_RATE = 0.3
N_HIDDEN_2 = 13
RNN_SIZE = 13
DEPTH = 10
TIMESTEPS = 12
START_LEARNING_RATE = 0.08
MAX_GRAD_NORM = 5
INPUT = 4
OUTPUT = 4


def split_data():
    x=np.random.random((200,4))
    y=x*4
    return  (x,y)     

x, y_ = split_data()

weights = {
    'input': tf.Variable(tf.truncated_normal([INPUT, N_HIDDEN_2], stddev=0.1)),
    'h1': tf.Variable(tf.truncated_normal([N_HIDDEN_2, N_HIDDEN_2], stddev=0.1)),
    'out': tf.Variable(tf.truncated_normal([N_HIDDEN_2, OUTPUT], stddev=0.1))
}

biases = {
    'input': tf.Variable(tf.zeros([N_HIDDEN_2])),
    'b1': tf.Variable(tf.zeros([N_HIDDEN_2])),
    'out': tf.Variable(tf.zeros([OUTPUT]))
}
batchX_placeholder = tf.placeholder(tf.float32, shape=[None, INPUT])
batchY_placeholder = tf.placeholder(tf.float32, shape=[None, OUTPUT])

inputs_series = [tf.nn.xw_plus_b(batchX_placeholder, weights['input'], biases['input'])]

lstm_cell = tf.contrib.rnn.GRUCell(RNN_SIZE)
stack_lstm = tf.contrib.rnn.MultiRNNCell([lstm_cell] * DEPTH)
states_series, current_state = tf.contrib.rnn.static_rnn(stack_lstm, inputs_series, dtype=tf.float32)
#states_series, current_state = tf.nn.dynamic_rnn(stack_lstm, inputs_series, dtype=tf.float32)
print('-----------------------------------')
print(states_series[-1])
layer1 = tf.nn.relu(tf.nn.xw_plus_b(states_series[-1], weights['h1'], biases['b1']))
prediction = tf.nn.xw_plus_b(layer1, weights['out'], biases['out'])

cost = tf.reduce_mean(tf.losses.mean_squared_error(y_, prediction))
optimizer = tf.train.AdagradOptimizer(LEARNING_RATE)
train_op = optimizer.minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    loss_list = []
    for epoch in range(NUM_EPOCHS):
        x, y = split_data()
        _total_loss, _train_step, _predictions_series = sess.run([cost, train_op, prediction],feed_dict={batchX_placeholder: x, batchY_placeholder: y})
        if epoch % 10 == 0:
            print("The Epoch is: ", epoch, " The Train loss=", _total_loss)

