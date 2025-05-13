#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            if i == 8 and j == 9:
                print("{}{}".format(i, j))
            else:
                print("{}{}, ".format(i, j), end="")

# the first for loop is going through the first digit
# the second for loop is going through the second digit
# if j > i ensures there are no duplicate numbers
# second if statement ensures the combinations don't
# end with an extra comma or space
