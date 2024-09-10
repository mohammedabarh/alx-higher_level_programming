#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Extract the last digit, handling negative numbers correctly
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit

# Prepare the output string
output = f"Last digit of {number} is {last_digit}"

# Determine the appropriate message based on the last digit
if last_digit > 5:
    output += " and is greater than 5"
elif last_digit == 0:
    output += " and is 0"
else:
    output += " and is less than 6 and not 0"

# Print the final output
print(output)
