from django.contrib import admin
from django.urls import path, include

#name space is MUV
app_name = 'MUV'
import moviehub
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add_movie, name='add_movie')
]