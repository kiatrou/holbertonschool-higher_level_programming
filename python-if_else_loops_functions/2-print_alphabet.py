#!/usr/bin/python3
letter = 97
while letter < 122:
    print(f"{chr(letter)}", end="")
    letter += 1

# using chr ensures the program prints the ASCII value, not the number
# end="" ensures the letters are printed on the same line without newline characters