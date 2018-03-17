from django.db import models


class Caracter(models.Model):
    """Main class for all caracters in the game."""

    name = models.CharField(max_length=150)
    health = models.IntegerField()
    armor = models.IntegerField()
    attack = models.CharField(max_length=3, default='3d6')
    attack_range = models.IntegerField()
    speed = models.IntegerField()

    def __str__(self):
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
    """Weapon class"""

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

    def __str__(self):
        return ' '.join([
            str(
                self.find_value(self.ITM_CONDS, self.item_condition)
            ).capitalize(),
            str(
                self.find_value(self.ITM_MATERS, self.item_material)
            ).capitalize(),
            str(
                self.find_value(self.WPN_NAMES, self.weapon_name)
            ).capitalize(),
            '(Damage',
            '+' + str(self.find_value(self.WPN_MODIFS, self.modificator)) + ')'
        ])

    def find_value(self, choices, name):
        """Finds value of a choice charfield to return in item name."""
        for i in choices:
            if i[0] == name:
                return i[1]


class ArmorLootItem(LootItem):
    """Weapon class"""

    ARM_NAMES = (
        ('arm', 'armor'),
        ('boo', 'boots'),
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
        ('na', 'na'),
        ('-1', '-1'),  # broken steel, cracked steel
        ('-2', '-2'),  # poor steel, normal steel
        ('-3', '-3'),  # good steel
    )
    modificator_negative = models.CharField(
        choices=ARM_MODIFS_NEGATIVE,
        default='-1',
        max_length=2)

    def __str__(self):

        if self.modificator_negative == 'na':
            obj_name_last_part = ')'
        else:
            obj_name_last_part = ', Speed ' + \
                str(
                    self.find_value(
                        self.ARM_MODIFS_NEGATIVE,
                        self.modificator_negative)
                ) + ')'
        return ' '.join([
            str(
                self.find_value(self.ITM_CONDS, self.item_condition)
            ).capitalize(),
            str(
                self.find_value(self.ITM_MATERS, self.item_material)
            ).capitalize(),
            str(
                self.find_value(self.ARM_NAMES, self.armor_name)
            ).capitalize(),
            '(Armor',
            '+' +
            str(
                self.find_value(
                    self.ARM_MODIFS_POSITIVE,
                    self.modificator_positive
                )
            ) + obj_name_last_part
        ])

    def find_value(self, choices, name):
        """Finds value of a choice charfield to return in item name."""
        for i in choices:
            if i[0] == name:
                return i[1]
