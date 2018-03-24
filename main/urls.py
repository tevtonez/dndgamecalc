from django.conf.urls import url

from main.views import (
    MonsterCreateView,
    MonsterDeleteView,
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

]
