"""Generate weapon."""

import random

from main.helpers.common import (
    ITEMS_LEVELS,
    ARMOR_NAMES
)
from main.models import ArmorLootItem


# GENERATING ARMOR

def gen_armor_item(level):
    """Generate armor item."""
    rand_arm_name = random.choice(ARMOR_NAMES)
    modificator_negative = '0'

    # SHIELDS
    sheild_materials = ('woo', 'ste')

    l1_wood_shield_cond = ('bro', 'cra', 'poo')
    l2_wood_shield_cond = ('nor', 'goo')
    # l3_wood_shield_cond = ()

    l1_steel_shield_cond = ('bro', 'cra')
    l2_steel_shield_cond = ('poo', 'nor')
    l3_steel_shield_cond = 'goo'

    # ARMOR and BOOTS
    armor_materials = ('lea', 'ste')
    l1_arm_boots_cond = ('bro', 'cra')
    l2_arm_boots_cond = ('poo', 'nor')
    l3_arm_boots_cond = 'goo'

    l1_leather_arm_bonus = '1'
    l2_leather_arm_bonus = ('2', '3')
    l3_leather_arm_bonus = '4'

    l1_steel_arm_bonus = ('1', '2')
    l2_steel_arm_bonus = ('3', '4')
    l3_steel_arm_bonus = '5'

    l1_steel_arm_penalties = '1'
    l2_steel_arm_penalties = ('1', '2')
    l3_steel_arm_penalties = '3'

    # GENERATING SHIELDS
    if rand_arm_name == 'shi':
        if level != 3:
            rand_arm_material = random.choice(sheild_materials)
            if level == 1:
                if rand_arm_material == 'woo':
                    arm_condition = random.choice(l1_wood_shield_cond)
                    if arm_condition == 'bro':
                        modificator_positive = 0
                    else:
                        modificator_positive = 1
                else:
                    arm_condition = random.choice(l1_steel_shield_cond)
                    modificator_positive = 1

            if level == 2:
                modificator_positive = 2
                if rand_arm_material == 'woo':
                    arm_condition = random.choice(l2_wood_shield_cond)
                else:
                    arm_condition = random.choice(l2_steel_shield_cond)

        else:
            rand_arm_material = 'ste'
            arm_condition = l3_steel_shield_cond
            modificator_positive = 3

    # GNERATING ARMOR AND BOOTS
    else:
        rand_arm_material = random.choice(armor_materials)
        if rand_arm_name == 'arm' or rand_arm_name == 'boo':
            if level == 1:
                arm_condition = random.choice(l1_arm_boots_cond)

                if rand_arm_material == 'lea':
                    modificator_positive = l1_leather_arm_bonus
                else:
                    modificator_positive = random.choice(l1_steel_arm_bonus)
                    modificator_negative = l1_steel_arm_penalties

            if level == 2:
                arm_condition = random.choice(l2_arm_boots_cond)

                if rand_arm_material == 'lea':
                    modificator_positive = random.choice(l2_leather_arm_bonus)
                else:
                    modificator_positive = random.choice(l2_steel_arm_bonus)
                    modificator_negative = random.choice(l2_steel_arm_penalties)

            if level == 3:
                arm_condition = l3_arm_boots_cond

                if rand_arm_material == 'lea':
                    modificator_positive = l3_leather_arm_bonus
                else:
                    modificator_positive = l3_steel_arm_bonus
                    modificator_negative = l3_steel_arm_penalties

    if rand_arm_name == 'boo':
        modificator_negative = '0'

    armor_item = ArmorLootItem(
        armor_name=rand_arm_name,
        item_condition=arm_condition,
        item_material=rand_arm_material,
        modificator_positive=modificator_positive,
        modificator_negative=modificator_negative,
        item_level=level
    )
    armor_item.save()


def generate_armor():
    """Generate weapon for the game."""
    for level in ITEMS_LEVELS:
        if level == 1:
            for i in range(0, 35):
                gen_armor_item(level)

        elif level == 2:
            for i in range(0, 25):
                gen_armor_item(level)

        elif level == 3:
            for i in range(0, 10):
                gen_armor_item(level)


generate_armor()
