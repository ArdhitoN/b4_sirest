from django.urls import path

from .views import *


app_name = 'tarifPengiriman'

urlpatterns = [
    path('buat_tarif/', show_buat_tarif, name='show_buat_tarif'),


]