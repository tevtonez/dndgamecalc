"""Generate weapon."""

import random

from main.helpers.common import (
    TRN_BONUSES_TO,
    TRN_NAMES,
    TRN_MODIFS_POSITIVE,
)
from main.models import TrinketLootItem


# GENERATING TRINKETS
def gen_trn_items(level, quantity):
    """Generate trinket items."""
    modificator_positive = '0'
    trn_materials = ('woo', 'lea', 'ste', 'sil', 'gol')

    for q in range(quantity + 1):
        # get name
        trn_name = random.choice([x[0] for x in TRN_NAMES])
        # get bonus to
        bonus_to = random.choice([x[0] for x in TRN_BONUSES_TO])

        if level == 1:
            # get materials
            trn_material = random.choice(trn_materials[:2])
            modificator_positive = random.choice(
                [x[0] for x in TRN_MODIFS_POSITIVE][0:2]
            )

        elif level == 2:
            # get materials
            trn_material = random.choice(trn_materials[2:4])
            modificator_positive = random.choice(
                [x[0] for x in TRN_MODIFS_POSITIVE][2:4]
            )

        else:
            trn_material = trn_materials[:-1]
            modificator_positive = random.choice(
                [x[0] for x in TRN_MODIFS_POSITIVE][-2:]
            )

        trn_item = TrinketLootItem(
            trinket_name=trn_name,
            bonus_to=bonus_to,
            item_material=trn_material,
            modificator_positive=modificator_positive,
            item_level=level,
        )
        trn_item.save()


def generate_trinkets():
    """Generate weapon for the game."""
    gen_trn_items(1, 35)
    gen_trn_items(2, 25)
    gen_trn_items(3, 10)


generate_trinkets()
