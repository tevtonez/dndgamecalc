"""Common functions and classes."""

ITEMS_LEVELS = [1, 2, 3]

ITEMS_TYPES = {
    'wpn': 'WeaponLootItem',
    'arm': 'ArmorLootItem',
    'trn': 'TrinketLootItem',
}

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

TRN_NAMES = (
    ('amu', 'amulet'),
    ('rin', 'ring'),
)

TRN_BONUSES_TO = (
    ('at', 'attack'),
    ('hp', 'health'),
    ('sp', 'speed'),
    ('ra', 'range'),
    ('ar', 'armor'),
)

TRN_MODIFS_POSITIVE = (
    # ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)

PLAYER_NAMES = ['Duke Vincent', 'Dadrin', 'Idrill']
PLAYERS_RACES = ['hum', 'dwa', 'elf']
MONSTER_RACES = [
    'bar',
    'spd',
    'ske',
    'ska',
    'fsp'
]
MONSTER_LEVELS = [1, 2, 3]


def find_value(choices, name):
    """Find value of a choice charfield to return in item name."""
    for i in choices:
        if i[0] == name:
            return i[1]
