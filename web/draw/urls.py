# chat/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url('logging_School/', views.logging_School, name='logging_School'),
    url('logging_Education/', views.logging_Education, name='logging_Education'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]

