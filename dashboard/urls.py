from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='default_home'),
    url(r'^home', views.home, name='home'),
    url(r'^create', views.create, name='create'),
    url(r'delete_entities', views.delete_entities, name='delete_entities'),
    url(r'^delete', views.delete, name='delete'),
    url(r'^edit_screen', views.edit_screen, name='edit_screen'),
    url(r'^update', views.update, name='update'),
    url(r'^overwrite', views.overwrite, name='overwrite'),
]