#!/usr/bin/python3
import sys


def safe_function(fct, *args):

    """
    Excecute a function safely

    Args:
        fct: the function to be executed
        args: arguments for fct

    Return: the return value of the fct if succesful. Otherwise null
    """
    try:
        return fct(*args)
    except BaseException as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
