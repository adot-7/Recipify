from django.urls import path
from . import views

app_name='recipes'
urlpatterns = [
    path('', views.land, name='land'),
]