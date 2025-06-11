#!/usr/bin/python3
"""
This is a function that returns a list of lists of integers
representing the Pascal triangle of n
"""


def pascal_triangle(n):
    """
    Prints pascal triangle
    """
    if n <= 0:
        return

    triangle = [[1]]

    # for rows 2 to n
    for i in range(1, n):
        # get the last row
        previous_row = triangle[-1]
        # every row starts with 1
        new_row = [1]

    # compute the middle values by adding pairs of the previous row
    for j in range(len(previous_row) - 1):
        new_row.append(previous_row) + previous_row[j + 1]

    # every row ends with 1
    new_row.append(1)
    # adds the new row to the triangle
    triangle.append(new_row)

    return (triangle)
