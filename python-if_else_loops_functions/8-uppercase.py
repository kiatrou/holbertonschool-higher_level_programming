#!/usr/bin/python3
def uppercase(str):
    output = ""

    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            output += chr(ord(i) - 32)
        else:
            output += i
    print("{}".format(output))
