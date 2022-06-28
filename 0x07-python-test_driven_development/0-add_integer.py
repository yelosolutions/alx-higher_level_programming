#!/usr/bin/python3


"""
A function which adds two numbers.
"""

def add_integer(a,b=98):
    """
    Function adds two integers
    Args:
        a: first number
        b: second number
    Returns:
        The addition of the two given numbers
    Raises:
        TypeError:
            if a or b is not an integer or float number
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
