#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers
    Complexity: O(log(n))
    """
    if not list_of_integers:
        return None
    
    # Binary search approach
    left, right = 0, len(list_of_integers) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # If mid element is smaller than its next element, peak is on the right side
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        # Otherwise, peak is on the left side or at mid
        else:
            right = mid
    
    return list_of_integers[left]
