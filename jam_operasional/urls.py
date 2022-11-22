from django.urls import path
from . import views

urlpatterns = [
    path('buat/', views.jam_buat, name='jam-buat'),
    path('daftar/', views.jam_daftar, name='jam-daftar'),
    path('', views.jam_daftar, name='jam-daftar-index')
]