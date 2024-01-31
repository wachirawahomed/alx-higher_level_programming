#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): The input matrix (list of lists of integers or floats).
        div (int, float): The divisor. >= 0.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    # Error messages
    matrix_type_error = ("matrix must be a matrix (list of lists) "
                         "of integers/floats")
    matrix_size_error = 'Each row of the matrix must have the same size'
    div_type_error = 'div must be a number'
    div_zero_error = 'division by zero'

    # Validate matrix type
    if not isinstance(matrix, list):
        raise TypeError(matrix_type_error)

    # Validate matrix content and size
    row_len = 0
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrix_type_error)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(matrix_type_error)
        if row_len and len(row) != row_len:
            raise TypeError(matrix_size_error)
        row_len = len(row)

    # Validate divisor type and non-zero
    if not isinstance(div, (int, float)):
        raise TypeError(div_type_error)
    if div == 0:
        raise ZeroDivisionError(div_zero_error)

    # Perform matrix division
    result_matrix = [
        [round(number / div, 2) for number in row] for row in matrix
    ]

    return result_matrix
