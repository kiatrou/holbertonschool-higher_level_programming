#!/usr/bin/python3
for i in range(97, 123):
    if i != 101 and i != 113:
        print("{:c}".format(i), end="")

# in print statement - {:c} is a format specification
# (: introduces the format)
# (c formats the value as a character (based on ASCII values))
