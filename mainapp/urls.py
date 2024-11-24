from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='inicio'),
    path('inicio/', views.index,name='inicio'),
    path('acercade/', views.about,name='acercade'),
    path('mision/', views.mision,name='mision'),
    path('vision/', views.vision,name='vision'),
    path('registro/', views.registro,name='registro'),
    path('inicio_secion/', views.inicio_secion,name='inicio_secion'),
    path('logout_user/', views.logout_user,name='logout_user'),
]
