from django.urls import path
from . import views

urlpatterns = [
    path('', views.jam_daftar, name='jam-daftar-index'),
    path('buat/', views.jam_buat, name='jam-buat'),
    path('daftar/', views.jam_daftar, name='jam-daftar'),
    path('ubah/', views.jam_ubah, name='jam-ubah'),
]