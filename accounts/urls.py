from django.conf.urls import url,include

from . import views
from rest_framework import routers
from accounts.views import *




urlpatterns = [
    url(r'^Country/$', UserCreate, name='account-create'),
    url(r'^Country/(?P<id>\d+)/$', user_details, name='account-create1'),
    url(r'^Country/$', UserCreationView.as_view()),
]
