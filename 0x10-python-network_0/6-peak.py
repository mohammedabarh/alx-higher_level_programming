#!/usr/bin/python3
"""Find a peak in a list of unsorted integers."""
def find_peak(list_of_integers):
    """Return a peak in a list of integers."""
    if not list_of_integers:
        return None
    peak = list_of_integers[0]
    for i in list_of_integers:
        if i > peak:
            peak = i
    return peak
