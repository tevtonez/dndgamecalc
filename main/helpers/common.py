"""Common functions and classes."""

ITEMS_LEVELS = [1, 2, 3]
WEAPON_MOD_ZERO_VALUE_LIMIT = 5

WEAPON_NAMES = (
    ('bow'),
    ('swo'),
    ('clu'),
    ('sti'),
    ('axe'),
    ('ham'),
    ('arb'),
)

ARMOR_NAMES = (
    ('arm'),
    ('boo'),
    ('shi'),
)


def find_value(choices, name):
    """Find value of a choice charfield to return in item name."""
    for i in choices:
        if i[0] == name:
            return i[1]
