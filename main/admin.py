from django.contrib import admin

from main.models import(
    ArmorLootItem,
    GamerCaracter,
    WeaponLootItem,
)

admin.site.register(GamerCaracter)
admin.site.register(WeaponLootItem)
admin.site.register(ArmorLootItem)
