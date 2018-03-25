from django.conf.urls import url

from main.views import (
    CombatView,
    MonsterCreateView,
    MonsterDeleteView,
    RespawnPlayer,
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
    # monster attacks a player
    url(
        r'^combat/(?P<attacker_id>\d*)/(?P<victim_id>\d*)/(?P<monster_hit>(1|0))$',
        CombatView.as_view(),
        name='combat'
    ),
    url(
        r'^respawn_player/(?P<player_id>\d*)$',
        RespawnPlayer.as_view(),
        name='respawn_player'
    )
]
