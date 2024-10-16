#!/usr/bin/python3
"""Module that defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle of n rows.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list of lists: A list of lists of integers representing Pascal's triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
