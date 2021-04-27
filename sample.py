#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 4/12/21-10:38
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : superior_god
# @File     : sample.py
# @Project  : 00PythonProjects
import os

import tensorflow as tf

from model import CharRNN
from read_utils import TextConverter

FLAGS = tf.flags.FLAGS

tf.flags.DEFINE_integer('lstm_size', 128, 'size of hidden state of lstm')
tf.flags.DEFINE_integer('num_layers', 2, 'number of lstm layers')
tf.flags.DEFINE_boolean('use_embedding', False, 'whether to use embedding')
tf.flags.DEFINE_integer('embedding_size', 128, 'size of embedding')
tf.flags.DEFINE_string('converter_path', '', 'model/name/converter.pkl')
tf.flags.DEFINE_string('checkpoint_path', '', 'checkpoint path')
tf.flags.DEFINE_string('start_string', ' ', 'use this string to start generating')
tf.flags.DEFINE_integer('max_length', 30, 'max length to generate')
tf.flags.DEFINE_string('result', 'result.txt', 'use this string to start generating')
tf.flags.DEFINE_string('name', 'default', 'name of the model')

def main(_):
    # FLAGS.start_string = FLAGS.start_string.decode('utf-8')
    FLAGS.checkpoint_path = os.path.join(FLAGS.checkpoint_path, FLAGS.name)
    converter_path = FLAGS.checkpoint_path + "/converter.pkl"
    print(converter_path)
    converter = TextConverter(filename=converter_path)
    if os.path.isdir(FLAGS.checkpoint_path):
        FLAGS.checkpoint_path = \
            tf.train.latest_checkpoint(FLAGS.checkpoint_path)

    model = CharRNN(converter.vocab_size, sampling=True,
                    lstm_size=FLAGS.lstm_size, num_layers=FLAGS.num_layers,
                    use_embedding=FLAGS.use_embedding,
                    embedding_size=FLAGS.embedding_size)

    model.load(FLAGS.checkpoint_path)

    start = converter.text_to_arr(FLAGS.start_string)
    arr = model.sample(FLAGS.max_length, start, converter.vocab_size)
    print(converter.arr_to_text(arr))
    with open(FLAGS.result, 'w') as f:
        f.write(converter.arr_to_text(arr))


if __name__ == '__main__':
    tf.app.run()
