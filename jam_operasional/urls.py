from django.urls import path
from . import views

urlpatterns = [
    path('', views.jam_daftar, name='jam_daftar_index'),
    path('buat/', views.jam_buat, name='jam_buat'),
    path('daftar/', views.jam_daftar, name='jam_daftar'),
    path('ubah/', views.jam_ubah, name='jam_ubah'),
    path('buat_request/', views.jam_buat_op, name='jam_buat_op'),
]