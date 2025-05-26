#!/usr/bin/python3
"""
This module has the class MyList which inherites
ffrom list
"""


class MyList(list):
    """
    A class to represent my list

    Attributes
    ----------

    Methods
    ----------
    print_sorted:
        prints the list in ascending order
    """
    def print_sorted(self):
        print(sorted(self))
