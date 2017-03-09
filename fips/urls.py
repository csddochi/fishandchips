from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.introduction, name='introduction'),
    url(r'^login/', views.sign_in, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^main/$', views.main, name='main'),
]
