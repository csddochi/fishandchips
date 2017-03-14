from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^main', views.main_view, name='main'),
    url(r'^login', views.sign_in, name='login'),
    url(r'^logout', views.log_out, name='logout'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^admin', admin.site.urls),
    url(r'^.*$', views.introduction, name='introduction'),
]
