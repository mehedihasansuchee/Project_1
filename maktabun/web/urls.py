from django.urls import path
from . import views

urlpatterns = [
    path('', views.deshboard, name='Deshboard'),
    path('home/', views.home, name='Home'),
    path('library/', views.library, name='Library'),
    path('about/', views.about, name='About'),
    path('contract', views.contract, name='Contract'),
    
]
