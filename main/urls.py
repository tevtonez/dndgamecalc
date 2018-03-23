from django.conf.urls import url
from main.views import (
    MonsterCreateView,
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

]
