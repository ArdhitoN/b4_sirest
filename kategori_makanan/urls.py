from django.urls import path
from kategori_makanan.views import *

urlpatterns = [
    path('', show_kategori_makanan, name='show_kategori_makanan'),
    path('tambah/', show_tambah_kategori_makanan, name='show_tambah_kategori_makanan')
]
