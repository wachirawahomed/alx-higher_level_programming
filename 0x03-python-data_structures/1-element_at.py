#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element from a list like in C.
    """

    if 0 <= idx < len(my_list):
        return (my_list[idx])
    return None
