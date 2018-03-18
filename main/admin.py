"""Admin panel main section."""
from django.contrib import admin

from main.models import(
    ArmorLootItem,
    GamerCaracter,
    TrinketLootItem,
    WeaponLootItem,
)

admin.site.register(ArmorLootItem)
admin.site.register(GamerCaracter)
admin.site.register(TrinketLootItem)
admin.site.register(WeaponLootItem)
