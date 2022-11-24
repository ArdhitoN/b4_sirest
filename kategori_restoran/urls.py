from django.urls import path
from kategori_restoran.views import *

app_name = "kategori_restoran"

urlpatterns = [
    path('', show_kategori_restoran, name='show_kategori_restoran'),
    path('tambah/', show_tambah_kategori_restoran, name='show_tambah_kategori_restoran'),
    path('hapus/', delete_kategori_restoran, name='delete_kategori_restoran'),
]