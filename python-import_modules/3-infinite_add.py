#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    total_sum = 0
    num = 0

    for i in args:
        num = int(i)
        total_sum += num
    print(total_sum)
