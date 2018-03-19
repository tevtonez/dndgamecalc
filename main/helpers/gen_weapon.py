"""Generate weapon."""

import random

from main.helpers.common import (
    ITEMS_LEVELS,
    WEAPON_NAMES,
    WEAPON_MOD_ZERO_VALUE_LIMIT
)
from main.models import WeaponLootItem


# GENERATING WEAPON
def gen_weapon_item(
    wp_conditions,
    wp_materials,
    wp_modifiers,
    level,
):
    """Generate weapon item."""
    global WEAPON_MOD_ZERO_VALUE_LIMIT
    rand_wp_name = random.choice(WEAPON_NAMES)
    if rand_wp_name == 'bow' or rand_wp_name == 'arb':
        wp_bonus_to = 'ra'
    else:
        wp_bonus_to = 'at'

    # limiting # of level 1 items wiht zero modifier
    modifier = random.choice(wp_modifiers)
    if level == 1:
        if modifier == '0':
            if WEAPON_MOD_ZERO_VALUE_LIMIT > 0:
                WEAPON_MOD_ZERO_VALUE_LIMIT = WEAPON_MOD_ZERO_VALUE_LIMIT - 1
            else:
                modifier = '1'

    w = WeaponLootItem(
        weapon_name=rand_wp_name,
        item_condition=random.choice(wp_conditions),
        item_material=random.choice(wp_materials),
        modificator=modifier,
        bonus_to=wp_bonus_to,
        item_level=level
    )
    w.save()


def generate_weapon():
    """Generate weapon for the game."""
    for level in ITEMS_LEVELS:
        if level == 1:
            # generating weapon of Level I
            wp_conditions = (
                ('cra'),
                ('bro'),
            )
            wp_materials = (
                ('woo'),
            )
            wp_modifiers = (
                ('0'),  # broken      (level I)
                ('1'),  # cracked     (level I)
            )
            for i in range(0, 35):

                gen_weapon_item(
                    wp_conditions,
                    wp_materials,
                    wp_modifiers,
                    level
                )

        elif level == 2:
            # generating weapon of Level II
            wp_conditions = (
                ('poo'),
                ('nor'),
            )
            wp_materials = (
                ('ste'),
                ('sil'),
            )
            wp_modifiers = (
                ('2'),  # poor        (level II)
                ('3'),  # normal      (level II)
            )
            for i in range(0, 25):
                gen_weapon_item(
                    wp_conditions,
                    wp_materials,
                    wp_modifiers,
                    level
                )

        elif level == 3:
            # generating weapon of Level III
            wp_conditions = (
                ('goo'),
                ('sha'),
            )
            wp_materials = (
                ('gol'),
            )
            wp_modifiers = (
                ('4'),  # good        (level III)
                ('5'),  # sharp       (level III)
            )
            for i in range(0, 10):
                gen_weapon_item(
                    wp_conditions,
                    wp_materials,
                    wp_modifiers,
                    level
                )


generate_weapon()
