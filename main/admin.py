"""Admin panel main section."""
from django.contrib import admin

from main.models import(
    ArmorLootItem,
    GameLog,
    PlayerCharacter,
    MonsterCharacter,
    TrinketLootItem,
    WeaponLootItem,
)

admin.site.register(ArmorLootItem)
admin.site.register(GameLog)
admin.site.register(PlayerCharacter)
admin.site.register(MonsterCharacter)
admin.site.register(TrinketLootItem)
admin.site.register(WeaponLootItem)
