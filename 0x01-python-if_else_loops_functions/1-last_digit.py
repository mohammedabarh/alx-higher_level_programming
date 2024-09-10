#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)  # Generate a random integer
last_digit = number % 10  # Get the last digit

# Adjust last_digit for negative numbers
if last_digit < 0:
    last_digit = -last_digit

# Prepare the output string
if number < 0:
    print(f"Last digit of {number} is -{last_digit}", end=" ")
else:
    print(f"Last digit of {number} is {last_digit}", end=" ")

# Determine the message based on the last digit
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
