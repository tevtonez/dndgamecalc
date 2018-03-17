from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from main import views as main_views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.IndexView.as_view(), name='home'),
    url(r'^main_template/$', main_views.mainIndexView.as_view(), name='main_template'),

    # logging users in/out
    url(r'^login/$', auth_views.login, {'template_name': 'main/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    #signup users
    url(r'signup/$', main_views.SignUpView.as_view(),name = 'signup'),

    # app url
    url(r'^main/', include('main.urls')),

]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
