from django.conf.urls import url

from main.views import (
    CombatView,
    MonsterCreateView,
    MonsterDeleteView,
    RespawnPlayer,
    ItemDropView,
    ItemEquipView,
)

app_name = 'main'

urlpatterns = [
    # url(r'^$', views.index, name='app_index'),

    # creating monsters
    url(
        r'^monster/(?P<monster_race>.*)/(?P<monster_number>.*)/$',
        MonsterCreateView.as_view(),
        name='generate_monster'
    ),
    # deleting monsters manually
    url(
        r'^monster/(?P<monster_id>\d*)$',
        MonsterDeleteView.as_view(),
        name='delete_monster'
    ),
    # combat
    url(
        r'^combat/(?P<attacker_id>\d*)/(?P<victim_id>\d*)/(?P<monster_hit>(1|0))$',
        CombatView.as_view(),
        name='combat'
    ),
    # respawn a player
    url(
        r'^respawn_player/(?P<player_id>\d*)$',
        RespawnPlayer.as_view(),
        name='respawn_player'
    ),
    # drop item from inventory
    url(
        r'^drop-item/(?P<player_id>\d*)/(?P<item_id>\d*)/(?P<item_class>\d*)$',
        ItemDropView.as_view(),
        name='drop_item'
    ),
    # equip item
    url(
        r'^equip-item/(?P<player_id>\d*)/(?P<item_id>\d*)/(?P<item_class>\d*)/(?P<action>\d*)$',
        ItemEquipView.as_view(),
        name='equip_item'
    ),
]
