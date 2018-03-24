"""Generating monsters and players."""

from main.models import (
    PlayerCharacter
)


# GENERATING PLAYERS
duke = PlayerCharacter(
    name='Duke Vincent',
    health='4',
    armor='7',
    attack_range=0,
    attack_modifier=2,
    speed=5,
    character_description='Duke Vincent is a noble knight. He was the only child in a reach family of Duke Kraus and Duchess Aleana and parents gave him great education and training as well as nobility.\nHe became a great leader and savior of poor and miserable.'
)
duke.save()

dadrin = PlayerCharacter(
    name='Dadrin',
    health='5',
    armor='6',
    attack_range=0,
    attack_modifier=3,
    speed=4,
    character_race='dwa',
    character_description='Dadrin is a descendant of a great family line of Northern Dwarfs of Aralath: the Great Kingdom of Thousand Mountains.\nAfter the kingdom has been defeated by a black dragon Whizzing Death and whole his family being slayed he left his home and wandered through the realms of Great Continent, participating in hundreds of adventures.'
)
dadrin.save()

idrill = PlayerCharacter(
    name='Idrill',
    health='4',
    armor='5',
    attack_range=4,
    attack_modifier=1,
    speed=7,
    character_race='elf',
    character_description='Idrill is a daughter of a ruler of a mighty Southern elf clan that lives in the heart of Evergreen Forest Vastness.\nShe has her own task in this part of Great Continent but by the forces of fate she joins Duke Vincent and Dadrin in the quest of defeating a monster in a cave of skeletons.'
)
idrill.save()
