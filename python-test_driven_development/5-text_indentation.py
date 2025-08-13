#!/usr/bin/python3
"""
This module contains a function text_indentation that prints text
with 2 new lines after each of these characters: '.', '?' and ':'
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these
    characters: '.', '?' and ':'

    text must be a string, otherwise raise a TypeError exception
    with the message 'text must be a string'
    There should be no space at the beginning or at the
    end of each printed line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_line = ""

    for char in text:
        if char in '.?:':
            current_line += char
            print(current_line.strip())
            print()
            current_line = ""
        elif char == '\n':
            if current_line.strip():
                print(current_line.strip())
            current_line = ""
        else:
            current_line += char

    # Print any remaining content
    if current_line.strip():
        print(current_line.strip())


if __name__ == "__main__":
    import doctest
    doctest.testfile("5-text_indentation.txt")
