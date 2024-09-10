#!/usr/bin/python3

for letter in range(97, 123):  # ASCII values from 'a' to 'z'
    if letter != 101 and letter != 113:  # Exclude 'e' (101) and 'q' (113)
        print(chr(letter), end="")
