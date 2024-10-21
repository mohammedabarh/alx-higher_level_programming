#!/usr/bin/python3
"""
This module performs matrix multiplication using the NumPy library.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The product of the two matrices.
    """
    return numpy.matmul(m_a, m_b)
