from django.urls import path

from .views import *


app_name = 'tarifPengiriman'

urlpatterns = [
    path('buat_tarif/', show_buat_tarif, name='show_buat_tarif'),
    path('daftar_tarif/', show_daftar_tarif, name='show_daftar_tarif'),
    path('update_tarif/', show_update_tarif, name='show_update_tarif'),
    path('hapus_tarif', hapus_tarif, name="hapus_tarif"),


]