#!/usr/bin/python3
def max_integer(list=[]):
    if len(list) == 0:
        return None
    else:
        max_int = list[0]
        for i in list:
            if i > max_int:
                max_int = i
        return max_int
