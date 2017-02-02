from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='default_home'),
    url(r'^home', views.home, name='home'),
    #url(r'^createentity', views.create, name='create'),
]