#!/usr/bin/python3

"""
Function prints a message
"""


def say_my_name(first_name, last_name=""):
    """
        Function prints a message
        Args:
            first_name: a string
            last_name: a string
        Returns:
            Nothing
        Raises:
            TypeError: if first_name is not a string
            TypeError: if last_name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is  {} {}".format(first_name, last_name))
