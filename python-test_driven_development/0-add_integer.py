#!/usr/bin/python3
"""
This module contains a function add_integer that adds two integers.
"""
def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of the two integers.

    Raises:
        TypeError: If either argument is not an integer or float.

    Examples:
    >>> add_integer(2, 99)
    101
    >>> add_integer(5, 5)
    10
    >>> add_integer(10)
    108
    >>> add_integer(3.7, 4.2)
    7
    >>> add_integer(-1, -2)
    -3
    >>> add_integer(0, 0)
    0
    >>> add_integer(5, 2.9)
    7
    >>> add_integer(4.5, 3)
    7
    >>> add_integer("hello", 1)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(1, "hello")  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
