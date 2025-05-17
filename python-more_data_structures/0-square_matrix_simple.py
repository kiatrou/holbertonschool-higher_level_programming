#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        new_row = []
        for i in range(len(row)):
            new_row.append(row[i] ** 2)
        result.append(new_row)
    return (result)

