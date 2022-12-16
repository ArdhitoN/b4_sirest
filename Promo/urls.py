from django.urls import path

from .views import *


app_name = 'Promo'

urlpatterns = [
     path('', buatpromo, name='Buat_Promo') ,
    # path('', list_promo, name='Buat_Promo') ,
    # path('Buat_Admin/', buatpromo, name='buatpromo') ,
    # path('buat_promoHS/', buat_HS, name='buat_promoHS') ,
    path("Baca_Admin", list_promo, name ='Baca_Admin'),
    path('detail/<str:id>', detailpromo, name='detail_promo'),
    path('ubah/<str:id>', ubahpromo, name='ubah_promo'),
     path('delete/<str:id>', deletepromo, name='delete_promo'),
    path('buat_HS/', buat_HS, name='buat_promoHS') ,
    path('buat_MT/', buat_MT, name='buat_promoMT') ,
    path("Baca_Restaurant", list_promo, name ='Baca_Restaurant'),
]
