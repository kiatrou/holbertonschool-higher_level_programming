#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # skips script name itself (argv[0])
    args = sys.argv[1:]
    # gives count of arguments
    num_args = len(args)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    for i in range(num_args):
        print("{}: {}".format(i + 1, args[i]))
