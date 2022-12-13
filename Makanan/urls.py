from django.urls import path

from .views import *


app_name = 'Makanan'

urlpatterns = [
    path('buat_makanan/', show_buat_makanan, name='show_buat_makanan'),
    path('buat_makanan-logic/', buat_makanan, name='buat_makanan'),

    path('daftarMakanan_restoView/', show_makanan_restoView, name='show_makanan_restoView'),
    
    path('update_makanan/<str:FoodName>/', show_update_makanan, name='show_update_makanan'),
    path('update_makanan-logic/<str:FoodName>/', update_makanan, name='update_makanan'),

    path('daftarMakanan_nonRestoView/<str:rname>/<str:rbranch>/', show_makanan_nonRestoView, name='show_makanan_nonRestoView'),

    path('detail_resto/<str:rname>/<str:rbranch>/', show_detail_resto, name='show_detail_resto'),
    
    path('daftar_restoran/', show_daftar_restoran, name='show_daftar_restoran'),
    

    path('hapus_makanan/<str:FoodName>/', hapus_makanan, name='hapus_makanan'),




]