from django.contrib import admin

from main.models import(
    GamerCaracter,
    WeaponLootItem
)

admin.site.register(GamerCaracter)
admin.site.register(WeaponLootItem)
