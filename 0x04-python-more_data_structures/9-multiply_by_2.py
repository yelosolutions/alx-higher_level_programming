#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    list_keys = list(new_dict.keys())
    for key in list_keys:
        new_dict[key] = new_dict[key] * 2
    return new_dict
