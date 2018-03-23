from django.db import models

from main.helpers.common import find_value


class Character(models.Model):
    """Main class for all characters in the game."""

    class Meta:
        """Meta class."""

        abstract = True

    name = models.CharField(max_length=150)
    health = models.IntegerField(default=4)
    armor = models.IntegerField(default=5)
    attack = models.IntegerField(default=3)
    attack_range = models.IntegerField(default=0)
    attack_modifier = models.IntegerField(default=0)
    speed = models.IntegerField(default=5)
    character_level = models.IntegerField(default=1)
    character_description = models.TextField(
        max_length=1500,
        default="Character description..."
    )


class PlayerCharacter(Character):
    """Main class for all characters in the game."""

    player = models.BooleanField(default=True)

    RACE = (
        ('hum', 'Human'),
        ('dwa', 'Dwarf'),
        ('elf', 'Elf'),
    )
    character_race = models.CharField(
        choices=RACE,
        default='hum',
        max_length=3
    )

    def __str__(self):
        """Object string representation."""
        return ' '.join([
            str(self.name),
            str(find_value(self.RACE, self.character_race)),
        ])


class MonsterCharacter(Character):
    """Main class for all characters in the game."""

    monster = models.BooleanField(default=True)

    RACE = (
        ('bar', 'Barrel'),
        ('spd', 'Spider'),
        ('ske', 'Skeleton'),
        ('ska', 'Archer Skeleton'),
        ('fsp', 'Flying Spinner')
    )
    character_race = models.CharField(
        choices=RACE,
        default='ske',
        max_length=3
    )

    def __str__(self):
        """Object string representation."""
        if self.character_race not in ['bar', 'fsp']:
            full_info = '#' + str(self.name) + \
                ' (lv.' + str(self.character_level) + ')'
        else:
            full_info = ''

        return ' '.join([
            str(find_value(self.RACE, self.character_race)),
            full_info
        ])

# Hacking monsters' name field label
MonsterCharacter._meta.get_field('name').verbose_name = 'Monster #'


class LootItem(models.Model):
    """Describes Loot objects."""

    class Meta:
        """Meta class."""

        abstract = True

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

    item_level = models.IntegerField(default=1)
    item_dropped = models.BooleanField(default=False)


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
        ('0', '0'),  # broken      (level I)
        ('1', '1'),  # cracked     (level I)
        ('2', '2'),  # poor        (level II)
        ('3', '3'),  # normal      (level II)
        ('4', '4'),  # good        (level III)
        ('5', '5'),  # sharp       (level III)
    )
    modificator = models.CharField(
        choices=WPN_MODIFS,
        default='0',
        max_length=3)

    WPN_BONUS_TO = (
        ('at', 'attack'),
        ('ra', 'range'),
    )
    bonus_to = models.CharField(
        choices=WPN_BONUS_TO,
        default='at',
        max_length=2
    )

    def __str__(self):
        """Object string representation."""
        return ' '.join([
            "Level " + str(
                self.item_level
            ),
            str(
                find_value(self.ITM_CONDS, self.item_condition)
            ).capitalize(),
            str(
                find_value(self.ITM_MATERS, self.item_material)
            ).capitalize(),
            str(
                find_value(self.WPN_NAMES, self.weapon_name)
            ).capitalize(),
            '(' + str(
                find_value(self.WPN_BONUS_TO, self.bonus_to)
            ).capitalize(),
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
        ('0', '0'),  # broken wood                      (level I)
        ('1', '1'),  # bro/cra leather, cra wood, bro steel (level I)
        ('2', '2'),  # poor leather, cracked steel      (level II)
        ('3', '3'),  # normal leather, poor steel       (level II)
        ('4', '4'),  # good leather, normal steel       (level III)
        ('5', '5'),  # good steel                       (level III)
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
        default='0',
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
            "Level " + str(
                self.item_level
            ),
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
        ('0', '0'),  # broken   (level I)
        ('1', '1'),  # cracked  (level I)
        ('2', '2'),  # poor     (level II)
        ('3', '3'),  # normal   (level II)
        ('4', '4'),  # good     (level III)
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
            "Level " + str(
                self.item_level
            ),
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
