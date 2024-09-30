#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):  # Check if the element is an integer
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except IndexError:
        pass  # Ignore the exception when x is greater than list length
    print()  # Print a new line after printing the integers
    return count
