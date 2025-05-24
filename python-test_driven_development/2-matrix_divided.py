#!/usr/bin/python3
def matrix_divided(matrix, div):
    # Check that matrix is a list of lists of numbers
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(elem, (int, float)) for row in matrix for elem in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

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
