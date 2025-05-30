#!/usr/bin/python3
"""
List class
"""


class VerboseList(list):
    def append(self, item):
        try:
            print(f"Added {item} to the list.")
            super().append(item)
        except Exception:
            print(f"Error appending {item}")

    def extend(self, x):
        try:
            print(f"Extended the list with {x} items.")
            super().extend(x)
        except Exception:
            print(f"Error extending with {x}")

    def remove(self, item):
        try:
            print(f"Removed {item} from the list.")
            super().remove(item)
        except Exception:
            print(f"Error removing {item}")

    def pop(self, index=-1):
        try:
            item = super().pop(index)
            print(f"Popped {item} from the list.")
            return item
        except IndexError:
            print(f"Error: Cannot pop from index {index}; index out of range.")
        except Exception:
            print(f"Error popping from list")
