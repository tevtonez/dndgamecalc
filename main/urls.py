from django.conf.urls import url

from main.views import (
    MonsterAttacksView,
    MonsterCreateView,
    MonsterDeleteView,
    PlayerAttacksView,
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
        r'^monster-attacks/(?P<monster_id>\d*)/(?P<player_attacked>.*)$',
        MonsterAttacksView.as_view(),
        name='monster_attacks'
    ),
    # player attacks a monster
    url(
        r'^player-attacks/(?P<player>.*)/(?P<monster_id>\d*)$',
        PlayerAttacksView.as_view(),
        name='player_attacks'
    ),
]
