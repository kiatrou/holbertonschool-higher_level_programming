#!/usr/bin/python3
for counter in range(97, 123):
    if counter != 101 and counter != 113:
        print("{:c}".format(counter), end="")

# in print statement - {:c} is a format specification
# (: introduces the format)
# (c formats the value as a character (based on ASCII values))
