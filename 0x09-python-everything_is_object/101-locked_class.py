#!/usr/bin/python3
"""LockedClass module with class no class or object attiribute"""


class LockedClass:
    """
    class LockedClass with no class or object attribute
    It prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    """
    __slots__ = 'first_name'
