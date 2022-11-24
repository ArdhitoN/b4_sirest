from django.urls import path

from .views import *


app_name = 'Makanan'

urlpatterns = [
    path('buat_makanan/', show_buat_makanan, name='show_buat_makanan'),
    path('daftarMakanan_restoView/', show_makanan_restoView, name='show_makanan_restoView'),
    path('ubah_makanan/', show_ubah_makanan, name='show_ubah_makanan'),

    path('daftarMakanan_nonRestoView/', show_makanan_nonRestoView, name='show_makanan_nonRestoView'),
    path('daftarMakanan_AView/', show_makanan_AView, name='show_makanan_AView'),
    path('daftarMakanan_KView/', show_makanan_KView, name='show_makanan_KView'),
    path('daftarMakanan_PView/', show_makanan_PView, name='show_makanan_PView'),



    path('detail_resto/', show_detail_resto, name='show_detail_resto'),
    path('detail_resto_AView/', show_detail_resto_AView, name='show_detail_resto_AView'),
    path('detail_resto_KView/', show_detail_resto_KView, name='show_detail_resto_KView'),
    path('detail_resto_PView/', show_detail_resto_PView, name='show_detail_resto_PView'),

    
    path('daftar_restoran/', show_daftar_restoran, name='show_daftar_restoran'),
    path('daftar_restoran_AView/', show_daftar_restoran_AView, name='show_daftar_restoran_AView'),
    path('daftar_restoran_KView/', show_daftar_restoran_KView, name='show_daftar_restoran_KView'),
    path('daftar_restoran_PView/', show_daftar_restoran_PView, name='show_daftar_restoran_PView'),



    path('hapus_makanan/', hapus_makanan, name='hapus_makanan'),




]