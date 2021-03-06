#!/usr/bin/env python3
"""
1-input.py
Module that defines a function called build_model
"""

import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    Function that builds a neural network with the Keras library
    Args:
        nx (int): number of input features to the network
        layers (list): list containing the number of nodes in each layer of
                       the network
        activations (list): list containing the activation functions used
                            for each layer of the network
        lambtha (float): L2 regularization parameter
        keep_prob (float): probability that a node will be kept for dropout
    Returns:
        the keras model
    """
    X_input = K.layers.Input(shape=(nx,))

    X = K.layers.Dense(layers[0],
                       activation=activations[0],
                       kernel_regularizer=K.regularizers.l2(lambtha))(X_input)

    for nodes, act in zip(layers[1::], activations[1::]):
        X = K.layers.Dropout(1 - keep_prob)(X)
        X = K.layers.Dense(nodes,
                           activation=act,
                           kernel_regularizer=K.regularizers.l2(lambtha))(X)

    model = K.Model(inputs=X_input, outputs=X)
    return model
