from django.urls import path

from .views import *


app_name = 'tarifPengiriman'

urlpatterns = [
    path('buat_tarif/', show_buat_tarif, name='show_buat_tarif'),
    path('daftar_tarif/', show_daftar_tarif, name='show_daftar_tarif'),
    path('update_tarif/<str:id>/<str:province>', show_update_tarif, name='show_update_tarif'),
    path('update/<str:id>/<str:province>', update_tarif, name='update_tarif'),
    path('hapus_tarif/<str:id>', hapus_tarif, name="hapus_tarif"),
    path('buat_tarif_logic/', buat_tarif, name='buat_tarif'),


]