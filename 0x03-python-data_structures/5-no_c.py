#!/usr/bin/python3
def no_c(my_string):
    """
    Rmoves all characters c and C from a string.
    """
    new_string = ""
    for c in my_string:
        if c not in "cC":
            new_string += c
    return new_string
