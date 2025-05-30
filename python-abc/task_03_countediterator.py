#!/usr/bin/python3
"""
Iterator class
"""


class CountedIterator():
    def __init__(self, iterable):
        # Convert the input iterable (like a list) into an iterator object
        self.iterator = iter(iterable)
        # Initialize a counter to keep track of how many items
        # have been returned
        self.counter = 0

    def __next__(self):
        # Get the next item from the original iterator
        item = next(self.iterator)
        # Increment the counter by 1 each time __next__ is called
        self.counter += 1
        # Return the retrieved item
        return (item)

    def __iter__(self):
        # Return self to make this object an iterator itself
        return (self)

    def get_count(self):
        # Return the current count of items returned so far
        return (self.counter)
