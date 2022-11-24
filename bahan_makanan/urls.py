from django.urls import path
from bahan_makanan.views import *

app_name = "bahan_makanan"

urlpatterns = [
    path('', show_bahan_makanan, name='show_bahan_makanan'),
    path('tambah/', show_tambah_bahan_makanan, name='show_tambah_bahan_makanan'),
    path('hapus/', delete_bahan_makanan, name='delete_bahan_makanan'),
]