#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers using binary search."""
    list_l = len(list_of_integers)
    if list_l == 0:
        return None
    peak_index = binary_search(list_of_integers, 0, list_l - 1)
    return list_of_integers[peak_index]


def binary_search(a, lo, hi):
    """Recursively performs binary search to find the peak."""
    if lo >= hi:
        return lo
    mid = ((hi - lo) // 2) + lo
    if a[mid] > a[mid + 1]:
        return binary_search(a, lo, mid)
    else:
        return binary_search(a, mid + 1, hi)
