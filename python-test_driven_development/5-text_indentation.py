#!/usr/bin/python3
"""
This module contains a function text_indentation that prints text
with 2 new lines after each of these characters: '.', '?' and ':'
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?' and ':'
    
    text must be a string, otherwise raise a TypeError exception
    with the message 'text must be a string'
    There should be no space at the beginning or at the end of each printed line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text):
        if text[i] in '.?:':
            print(text[i])
            print()
            i += 1
            # Skip any spaces after special characters
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end='')
            i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("5-text_indentation.txt")
