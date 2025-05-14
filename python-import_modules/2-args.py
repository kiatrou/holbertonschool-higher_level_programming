#!/usr/bin/python3
import sys

counter = 0

for i in sys.argv:
    counter += 1
    print("{} arguments:".format(counter))
    print("{}: {}".format(counter, i))
    if i == 0:
        print("{} arguments.".format(counter))
