"""Generating monsters and players."""

from main.models import (
    PlayerCharacter
)


def gen_players():
    """Generate players."""
    base_health = 4
    base_armor = 5
    base_range = 0
    base_attack = 3
    base_speed = 4

    # GENERATING PLAYERS
    duke = PlayerCharacter(
        name='Vincent',
        health=base_health,
        respawn_health=base_health,
        armor=base_armor + 2,
        attack_range=base_range,
        attack_modifier=1,
        speed=base_speed + 1,
        player_id='vin',

        initial_health=base_health,
        initial_armor=base_armor + 2,
        initial_attack_modifier=base_attack,
        initial_attack_range=base_range,
        initial_speed=base_speed + 1,

        character_description='Duke Vincent is a noble knight. He was the only child in a reach family of Duke Kraus and Duchess Aleana and parents gave him great education and training as well as nobility.\nHe became a great leader and savior of poor and miserable.'
    )
    duke.save()

    dadrin = PlayerCharacter(
        name='Dadrin',
        health=base_health + 1,
        respawn_health=base_health + 1,
        armor=base_armor + 1,
        attack_range=base_range,
        attack_modifier=base_attack - 1,
        speed=base_speed,
        character_race='dwa',
        player_id='dad',

        initial_health=base_health + 1,
        initial_armor=base_armor + 1,
        initial_attack_modifier=base_attack - 1,
        initial_attack_range=base_range,
        initial_speed=base_speed,

        character_description='Dadrin is a descendant of a great family line of Northern Dwarfs of Aralath: the Great Kingdom of Thousand Mountains.\nAfter the kingdom has been defeated by a black dragon Whizzing Death and whole his family being slayed he left his home and wandered through the realms of Great Continent, participating in hundreds of adventures.'
    )
    dadrin.save()

    idrill = PlayerCharacter(
        name='Idrill',
        health=base_health,
        respawn_health=base_health,
        armor=base_armor,
        attack_range=base_range + 4,
        attack_modifier=base_attack - 2,
        speed=base_speed + 3,
        character_race='elf',
        player_id='idr',

        initial_health=base_health,
        initial_armor=base_armor,
        initial_attack_modifier=base_attack - 2,
        initial_attack_range=base_range + 4,
        initial_speed=base_speed + 3,

        character_description='Idrill is a daughter of a ruler of a mighty Southern elf clan that lives in the heart of Evergreen Forest Vastness.\nShe has her own task in this part of Great Continent but by the forces of fate she joins Duke Vincent and Dadrin in the quest of defeating a monster in a cave of skeletons.'
    )
    idrill.save()
