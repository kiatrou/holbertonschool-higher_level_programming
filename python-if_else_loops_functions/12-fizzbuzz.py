#!/usr/bin/python3
def fizzbuzz():
    hundred = 1

    while hundred <= 100:
        if (hundred % 3) == 0 and (hundred % 5) == 0:
            print("FizzBuzz", end=" ")
        elif hundred % 3 == 0:
            print("Fizz", end=" ")
        elif hundred % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(hundred), end=" ")
        hundred += 1
