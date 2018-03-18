"""Models."""

from django.db import models
from main.helpers.common import find_value


class Caracter(models.Model):
    """Main class for all caracters in the game."""

    name = models.CharField(max_length=150)
    health = models.IntegerField()
    armor = models.IntegerField()
    attack = models.CharField(max_length=3, default='3d6')
    attack_range = models.IntegerField()
    speed = models.IntegerField()

    def __str__(self):
        """Object string representation."""
        return ' '.join([
            str(self.name),
            str(self.id)
        ])


class GamerCaracter(models.Model):
    """Main class for all caracters in the game."""

    gamer = models.BooleanField()


class LootItem(models.Model):
    """Describes Loot objects."""

    # sizes are for amulets
    ITM_SIZES = (
        ('n', 'na'),
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large')
    )
    item_size = models.CharField(
        choices=ITM_SIZES,
        default='n',
        max_length=1
    )

    # condition are for WEAPON and ARMOR items
    ITM_CONDS = (
        ('nan', 'na'),
        ('sha', 'sharp'),
        ('goo', 'good'),
        ('nor', 'normal'),
        ('poo', 'poor'),
        ('cra', 'cracked'),
        ('bro', 'broken')
    )
    item_condition = models.CharField(
        choices=ITM_CONDS,
        default='na',
        max_length=3
    )

    # materials are for ALL items
    ITM_MATERS = (
        ('sil', 'silver'),
        ('gol', 'golden'),
        ('ste', 'steel'),
        ('lea', 'leather'),
        ('woo', 'wooden'),
        ('rub', 'ruby'),
        ('opa', 'opal'),
        ('zir', 'zirkon'),
    )
    item_material = models.CharField(
        choices=ITM_MATERS,
        default='woo',
        max_length=3
    )


class WeaponLootItem(LootItem):
    """Weapon class."""

    WPN_NAMES = (
        ('bow', 'bow'),
        ('swo', 'sword'),
        ('clu', 'club'),
        ('sti', 'stick'),
        ('axe', 'axe'),
        ('ham', 'hammer'),
        ('arb', 'arbalet'),
    )
    weapon_name = models.CharField(
        choices=WPN_NAMES,
        default='sti',
        max_length=3
    )

    WPN_MODIFS = (
        ('0', '0'),  # broken
        ('1', '1'),  # cracked
        ('2', '2'),  # poor
        ('3', '3'),  # normal
        ('4', '4'),  # good
        ('5', '5'),  # sharp
    )
    modificator = models.CharField(
        choices=WPN_MODIFS,
        default='0',
        max_length=3)

    bonus_to = models.CharField(
        choices=(
            ('at', 'attack'),
        ),
        default='at',
        max_length=2
    )

    def __str__(self):
        """Object string representation."""
        return ' '.join([
            str(
                find_value(self.ITM_CONDS, self.item_condition)
            ).capitalize(),
            str(
                find_value(self.ITM_MATERS, self.item_material)
            ).capitalize(),
            str(
                find_value(self.WPN_NAMES, self.weapon_name)
            ).capitalize(),
            '(Attack',
            '+' + str(find_value(self.WPN_MODIFS, self.modificator)) + ')'
        ])


class ArmorLootItem(LootItem):
    """Armor class."""

    ARM_NAMES = (
        ('arm', 'armor'),
        ('boo', 'boots'),
        ('shi', 'shield'),
    )
    armor_name = models.CharField(
        choices=ARM_NAMES,
        default='arm',
        max_length=3
    )

    ARM_MODIFS_POSITIVE = (
        ('0', '0'),  # broken leather, broken steel
        ('1', '1'),  # cracked leather
        ('2', '2'),  # poor leather, cracked steel
        ('3', '3'),  # normal leather, poor steel
        ('4', '4'),  # good leather, normal steel
        ('5', '5'),  # good steel
    )
    modificator_positive = models.CharField(
        choices=ARM_MODIFS_POSITIVE,
        default='1',
        max_length=1)

    # negative mogifs only for metal armor
    ARM_MODIFS_NEGATIVE = (
        ('0', '0'),
        ('1', '1'),  # broken steel, cracked steel
        ('2', '2'),  # poor steel, normal steel
        ('3', '3'),  # good steel
    )
    modificator_negative = models.CharField(
        choices=ARM_MODIFS_NEGATIVE,
        default='-1',
        max_length=2)

    bonus_to = models.CharField(
        choices=(
            ('ar', 'armor'),
        ),
        default='ar',
        max_length=2
    )

    penalty_to = models.CharField(
        choices=(
            ('sp', 'speed'),
        ),
        default='sp',
        max_length=2
    )

    def __str__(self):
        """Object string representation."""
        if self.modificator_negative == '0':
            obj_name_last_part = ')'
        else:
            obj_name_last_part = ', Speed -' + \
                str(
                    find_value(
                        self.ARM_MODIFS_NEGATIVE,
                        self.modificator_negative)
                ) + ')'
        return ' '.join([
            str(
                find_value(self.ITM_CONDS, self.item_condition)
            ).capitalize(),
            str(
                find_value(self.ITM_MATERS, self.item_material)
            ).capitalize(),
            str(
                find_value(self.ARM_NAMES, self.armor_name)
            ).capitalize(),
            '(Armor',
            '+' +
            str(
                find_value(
                    self.ARM_MODIFS_POSITIVE,
                    self.modificator_positive
                )
            ) + obj_name_last_part
        ])


class TrinketLootItem(LootItem):
    """Trinkets class."""

    TRN_NAMES = (
        ('amu', 'amulet'),
        ('rin', 'ring'),
    )
    trinket_name = models.CharField(
        choices=TRN_NAMES,
        default='amu',
        max_length=3
    )

    TRN_MODIFS_POSITIVE = (
        ('0', '0'),  # broken
        ('1', '1'),  # cracked
        ('2', '2'),  # poor
        ('3', '3'),  # normal
    )
    modificator_positive = models.CharField(
        choices=TRN_MODIFS_POSITIVE,
        default='0',
        max_length=1)

    TRN_BONUSES_TO = (
        ('at', 'attack'),
        ('hp', 'health'),
        ('sp', 'speed'),
        ('ra', 'range'),
        ('ar', 'armor'),
    )
    bonus_to = models.CharField(
        choices=TRN_BONUSES_TO,
        default='ar',
        max_length=2
    )

    def __str__(self):
        """Object string representation."""
        s_bonus_to = str(
            find_value(
                self.TRN_BONUSES_TO,
                self.bonus_to
            )
        ).capitalize()
        return ' '.join([
            str(
                find_value(self.ITM_SIZES, self.item_size)
            ).capitalize(),
            str(
                find_value(self.ITM_CONDS, self.item_condition)
            ).capitalize(),
            str(
                find_value(self.ITM_MATERS, self.item_material)
            ).capitalize(),
            str(
                find_value(self.TRN_NAMES, self.trinket_name)
            ).capitalize(),
            'of ' + s_bonus_to,
            '(' + s_bonus_to,
            '+' +
            str(
                find_value(
                    self.TRN_MODIFS_POSITIVE,
                    self.modificator_positive
                )
            ) + ')'
        ])
