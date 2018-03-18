"""Admin panel main section."""
from django.contrib import admin

from main.models import(
    ArmorLootItem,
    GamerCharacter,
    TrinketLootItem,
    WeaponLootItem,
)

admin.site.register(ArmorLootItem)
admin.site.register(GamerCharacter)
admin.site.register(TrinketLootItem)
admin.site.register(WeaponLootItem)
