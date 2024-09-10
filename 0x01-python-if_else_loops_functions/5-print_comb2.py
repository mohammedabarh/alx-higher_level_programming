#!/usr/bin/python3
numbers = range(100)  # Create a range from 0 to 99
formatted_numbers = [f'{num:02d}' for num in numbers]  # Format each number with leading zeros
print(', '.join(formatted_numbers))  # Join the formatted numbers with a comma and print
