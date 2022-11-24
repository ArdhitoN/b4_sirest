from django.urls import path

from .views import *


app_name = 'PromoRestoran'

urlpatterns = [
    path('', Baca_PromoRestoran, name='Baca_PromoRestoran') ,
    path('Buat_PromoRestoran/', Buat_PromoRestoran, name='Buat_PromoRestoran') ,
    path('Ubah_PromoRestoran/', Ubah_PromoRestoran, name='Ubah_PromoRestoran') ,
    path('Detail_PromoRestoran/', Detail_PromoRestoran, name='Detail_PromoRestoran')


]
