#!/usr/bin/python3

"""
Function prints a square with the character #
"""


def print_square(size):
    """
        Function prints a square with the character #
        Args:
            size: integer
        Returns:
            Nothing
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
