# -*- coding: utf-8 -*-
"""Script that trains a sample model.

NOTE: Run

tensorboard --logdir=justice/similarity_model/tf_model

to see training status. This will also let you train multiple models, so long
as `model_name` below differs, and see their training performance.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path

import tensorflow as tf

from justice.similarity_model import model, training_data

model_base_dir = os.path.abspath(
    os.path.join(os.path.abspath(__file__), "../tf_models"))


def main():
    layer_sizes = [64, 32]
    symmetric = True
    for dropout in [0.7, 0.8, 0.9]:
        model_name = 'sample_{}_drop{:.2f}_{}_{}_v2'.format(
            'sym' if symmetric else 'asym',
            dropout,
            *layer_sizes)
        estimator = tf.estimator.Estimator(
            model_fn=model.model_fn,
            model_dir=os.path.join(model_base_dir, model_name),
            params={
                'batch_size': 32,
                'window_size': 5,
                'dropout_keep_prob': dropout,
                'layer_sizes': layer_sizes,
                'symmetric': symmetric,
            }
        )
        estimator.train(input_fn=training_data.sample_data_input_fn,
                        max_steps=int(1e5))


if __name__ == '__main__':
    main()
