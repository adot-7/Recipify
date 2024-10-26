from django.urls import path, include
from . import views

app_name='recipes'
urlpatterns = [
    path('', views.land, name='land'),
    path('getstarted/', views.getresponse, name='getresponse'),
    path('about/', views.about, name="about")
]