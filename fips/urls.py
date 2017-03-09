from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.introduction, name='introduction'),
    url(r'^main/$', views.main, name='main'),
    url(r'^login/', views.sign_in, name='login'),
    url(r'^logout/$', views.log_out, {'next_page': '/'}, name='logout'),

]
