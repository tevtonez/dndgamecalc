"""Common functions and classes."""


def find_value(choices, name):
    """Find value of a choice charfield to return in item name."""
    for i in choices:
        if i[0] == name:
            return i[1]
