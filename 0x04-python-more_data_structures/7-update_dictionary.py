#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        return a_dictionary
    if key is None:
        return a_dictionary
    if value is None:
        return a_dictionary

    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value

    return a_dictionary
