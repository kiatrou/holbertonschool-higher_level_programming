#!/usr/bin/python3
"""
This module contains a function matrix_divided that divides a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides matrix and returns the result.

    matrix must be a list of lists of integers or floats, otherwise raise a
    TypeError exception with the message matrix must be a matrix
    (list of lists) of integers/floats

    Returns result.
    """
    # Check that matrix is a list of lists of numbers
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(elem, (int, float)) for row in matrix
                    for elem in row)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Check all rows are the same length
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new matrix with divided and rounded values
    return [[round(elem / div, 2) for elem in row] for row in matrix]
