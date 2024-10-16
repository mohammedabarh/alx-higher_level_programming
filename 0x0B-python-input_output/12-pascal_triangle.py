#!/usr/bin/python3
"""Defines a function to generate Pascal's Triangle."""


def pascal_triangle(n):
    """Generate Pascal's Triangle of size n.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list: A list of lists, where each inner list represents a row
              of Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]  # Start with the first row of the triangle.

    while len(triangles) < n:
        tri = triangles[-1]  # Get the last row of the triangle.
        tmp = [1]  # Initialize the new row with the first element '1'.

        # Calculate the values for the new row.
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])

        tmp.append(1)  # End the new row with the last element '1'.
        triangles.append(tmp)  # Append the new row to the triangle.

    return triangles
