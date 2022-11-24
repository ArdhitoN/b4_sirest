from django.urls import path
from kategori_makanan.views import *

app_name = "kategori_makanan"

urlpatterns = [
    path('', show_kategori_makanan, name='show_kategori_makanan'),
    path('tambah/', show_tambah_kategori_makanan, name='show_tambah_kategori_makanan'),
    path('hapus/<int:pk>', delete_kategori_makanan, name='delete_kategori_makanan'),
]
