def build_multilayer_lstm_graph_with_dynamic_rnn(
    state_size = state_size,
    num_classes = num_classes,
    batch_size = batch_size,
    num_steps = num_steps,
    num_layers = 3,
    learning_rate = learning_rate
    ):
    reset_graph()
    x = tf.placeholder(tf.int32, [batch_size, num_steps], name='x')
    y = tf.placeholder(tf.int32, [batch_size, num_steps], name='y')
    embeddings = tf.get_variable(name='embedding_matrix', shape=[num_classes, state_size])
    '''这里的输入是三维的[batch_size, num_steps, state_size]
        - embedding_lookup(params, ids)函数是在params中查找ids的表示， 和在matrix中用array索引类似,
          这里是在二维embeddings中找二维的ids, ids每一行中的一个数对应embeddings中的一行，所以最后是[batch_size, num_steps, state_size]
    '''
    rnn_inputs = tf.nn.embedding_lookup(params=embeddings, ids=x)
    cell = tf.nn.rnn_cell.LSTMCell(num_units=state_size, state_is_tuple=True)
    cell = tf.nn.rnn_cell.MultiRNNCell(cells=[cell]*num_layers, state_is_tuple=True)
    init_state = cell.zero_state(batch_size, dtype=tf.float32)
    '''使用dynamic_rnn方式'''
    rnn_outputs, final_state = tf.nn.dynamic_rnn(cell=cell, inputs=rnn_inputs,
                                                 initial_state=init_state)
    with tf.variable_scope('softmax'):
        W = tf.get_variable('W', [state_size, num_classes])
        b = tf.get_variable('b', [num_classes], initializer=tf.constant_initializer(0.0))

    rnn_outputs = tf.reshape(rnn_outputs, [-1, state_size])   # 转成二维的矩阵
    y_reshape = tf.reshape(y, [-1])
    logits = tf.matmul(rnn_outputs, W) + b                    # 进行矩阵运算
    total_loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=y_reshape))
    train_step = tf.train.AdamOptimizer(learning_rate).minimize(total_loss)

    return dict(x = x,
                y = y,
                init_state = init_state,
                final_state = final_state,
                total_loss = total_loss,
                train_step = train_step)