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

    ITM_SIZES = (
        ('n', 'na'),
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large')
    )

    item_size = models.CharField(
        choices=ITM_SIZES,
        default='s',
        max_length=1
    )

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
        default='na',
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
        default='na',
        max_length=3)

    def __str__(self):
        return ' '.join([
            str(self.find_value(self.ITM_CONDS, self.item_condition)).capitalize(),
            str(self.find_value(self.ITM_MATERS, self.item_material)).capitalize(),
            str(self.find_value(self.WPN_NAMES, self.weapon_name)).capitalize(),
            '(Damage',
            '+' + str(self.find_value(self.WPN_MODIFS, self.modificator)) + ')'
        ])

    def find_value(self, choices, name):
        """Finds value of a choice charfield to return in item name."""
        for i in choices:
            if i[0] == name:
                return i[1]
