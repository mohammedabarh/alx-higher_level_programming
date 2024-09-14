#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least 2 elements, using 0 for missing values
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # Perform addition of first two elements
    result = (a[0] + b[0], a[1] + b[1])
    
    return result
