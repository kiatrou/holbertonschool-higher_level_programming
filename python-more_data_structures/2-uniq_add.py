#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_nums = []
    for num in my_list:
        if num not in unique_nums:
            unique_nums.append(num)
    return sum(unique_nums)
