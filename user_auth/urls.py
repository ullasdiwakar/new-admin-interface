from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'login', views.login, name='login'),
    url(r'logout', views.logout, name='logout'),
    url(r'makeadmins', views.create_admin, name='make'),
    url(r'validate', views.validate, name='validate'),
]
