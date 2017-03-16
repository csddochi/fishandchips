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
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^notification', views.noti_view, name='notification'),
    url(r'^fanfic-board', views.fnfc_view, name='fanfic-board'),
    url(r'^free-board', views.free_view, name='free-board'),
    url(r'^file-board', views.file_view, name='file-board'),
    url(r'^story-board', views.stry_view, name='story-board'),
    url(r'^admin', admin.site.urls),
    url(r'^.*$', views.introduction, name='introduction'),
]
