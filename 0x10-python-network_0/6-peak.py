#!/usr/bin/python3
""" This function finds a peak in a list of unsorted integers. """
def find_peak(list_of_integers):
    """ Find a peak in a list of integers. """
    if not list_of_integers:
        return None
    max_val = max(list_of_integers)
    return max_val
