from django.urls import path

from .views import *


app_name = 'Makanan'

urlpatterns = [
    path('buat_makanan/', show_buat_makanan, name='show_buat_makanan'),
    path('daftarMakanan_restoView/', show_makanan_restoView, name='show_makanan_restoView'),
    path('ubah_makanan/', show_ubah_makanan, name='show_ubah_makanan'),

    path('daftarMakanan_nonRestoView/', show_makanan_nonRestoView, name='show_makanan_nonRestoView'),

    path('detail_resto/', show_detail_resto, name='show_detail_resto'),
    path('detail_resto_NRView/', show_detail_resto_NRView, name='show_detail_resto_NRView'),

    
    path('daftar_restoran/', show_daftar_restoran, name='show_daftar_restoran'),
    path('daftar_restoran_NRView/', show_daftar_restoran_NRView, name='show_daftar_restoran_NRView'),
    


    path('hapus_makanan/', hapus_makanan, name='hapus_makanan'),




]