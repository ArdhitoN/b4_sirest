from django.urls import path

from .views import *


app_name = 'Promo'

urlpatterns = [
    path('', Buat_Promo, name='Buat_Promo') ,
    # path('Daftar_Promo/', Daftar_Promo, name='Daftar_Promo') ,
    path('Detail_MinimumTransaksi_Promo/', Detail_MinimumTransaksi_Promo, name='Detail_MinimumTransaksi_Promo') ,
    path('Detail_HariSpesial_Promo/', Detail_HariSpesial_Promo, name='Detail_HariSpesial_Promo') ,
    path('Daftar_Promo_restoran/', Daftar_Promo_restoran, name='Daftar_Promo_restoran') ,
    path('Form_Ubah_PromoMinTransaksi/', Form_Ubah_PromoMinTransaksi, name='Form_Ubah_PromoMinTransaksi') , 
    path('Form_Ubah_PromoHS/', Form_Ubah_PromoHS, name='Form_Ubah_PromoHS') ,
    path('buat_promoHS/', buat_promoHS, name='buat_promoHS') ,
    path('buat_promoMT/', buat_promoMT, name='buat_promoMT') ,
    path('Daftar_Promo/', Daftar_Promo2.as_view(), name='Daftar_Promo') ,
]
