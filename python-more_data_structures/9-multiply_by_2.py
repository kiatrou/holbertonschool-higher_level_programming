#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied = {}
    # note - items allows the looping of both keys and values
    # without it, loop will only loop keys
    for key, value in a_dictionary.items():
        multiplied[key] = value * 2
    return (multiplied)
