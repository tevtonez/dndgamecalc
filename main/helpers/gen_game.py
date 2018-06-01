"""Game generation helper."""

from main.models import (
    GameLog,
    WeaponLootItem,
    ArmorLootItem,
    TrinketLootItem,
    PlayerCharacter,
    MonsterCharacter
)

from main.helpers.gen_players import gen_players
from main.helpers.gen_weapon import generate_weapon
from main.helpers.gen_armor import generate_armor
from main.helpers.gen_trinkets import generate_trinkets


def reset_game():
    """Rest game by deleting and regenerating all game objects."""
    # deleting all items
    GameLog.objects.all().delete()
    WeaponLootItem.objects.all().delete()
    ArmorLootItem.objects.all().delete()
    TrinketLootItem.objects.all().delete()
    PlayerCharacter.objects.all().delete()
    MonsterCharacter.objects.all().delete()

    # generating everything
    gen_players()
    generate_weapon()
    generate_armor()
    generate_trinkets()

    game_log = GameLog()
    game_log.save()
