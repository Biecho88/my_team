from django.urls import path
from . import views


urlpatterns = [
    path('', views.our_teams, name='our_teams'),
]