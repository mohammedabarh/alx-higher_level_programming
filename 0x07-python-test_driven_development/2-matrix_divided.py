#!/usr/bin/python3
"""This module provides the matrix_divided function."""


def matrix_divided(matrix, div):
    """Divides each element of the matrix by the given divisor.

    Parameters:
        matrix: A list of lists containing integers or floats.
        div: The number used to divide each element in the matrix.

    Returns:
        A new list of lists with the results of the division.

    Raises:
        TypeError: If the matrix is not a list of lists of numbers.
        TypeError: If the sublists are not of equal size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(element / div, 2) for element in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
