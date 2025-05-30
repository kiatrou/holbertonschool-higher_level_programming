#!/usr/bin/python3
"""
This module contains a function add_integer that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    a and b must be integers or floats; otherwise, raise TypeError.
    Floats are casted to integers before addition.

    Returns the integer sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

# Check for float('inf') and float('nan') without using math
    if isinstance(a, float):
        if a == float('inf') or a == -float('inf'):
            raise OverflowError("Float overflow: cannot convert to integer")
        if a != a:  # NaN check
            raise ValueError("cannot convert float")
    if isinstance(b, float):
        if b == float('inf') or b == -float('inf'):
            raise OverflowError("Float overflow: cannot convert to integer")
        if b != b:  # NaN check
            raise ValueError("cannot convert float")

    a = int(a)
    b = int(b)
    return (a + b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("0-add_integer.txt")
