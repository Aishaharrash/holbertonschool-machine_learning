#!/usr/bin/env python3
"""
3-one_hot.py
Module that defines a function called one_hot
"""

import tensorflow.keras as K


def one_hot(labels, classes=None):
    """
    Function that converts a label vector into a one-hot matrix
    Args:
        labels (np.ndarray): the label vector (1, classes)
        classes: number of classes
    Returns:
        the one-hot matrix
    """
    return K.utils.to_categorical(labels, classes)
