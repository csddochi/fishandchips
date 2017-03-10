from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^main', views.main_view, name='main'),
    url(r'^login', views.sign_in, name='login'),
    url(r'^logout', views.log_out, name='logout'),
    url(r'^admin', admin.site.urls),
    url(r'^.*$', views.introduction, name='introduction'),
]
