from django.urls import path

from .views import *


app_name = 'RiwayatTransaksiPemesanan'

urlpatterns = [
    path('', Baca_RiwayatTransaksiPemesananPelanggan, name='Baca_RiwayatTransaksiPemesanan') ,
    path('Baca_RiwayatTransaksiPemesananRestoran/', Baca_RiwayatTransaksiPemesananRestoran, name='Baca_RiwayatTransaksiPemesananRestoran') ,
    path('Baca_RiwayatTransaksiPemesananKurir/', Baca_RiwayatTransaksiPemesananKurir, name='Baca_RiwayatTransaksiPemesananKurir')  ,
    path('Form_Penilaian_Pemesanan/', Form_Penilaian_Pemesanan, name='Form_Penilaian_Pemesanan') , 
    path('Detail_Pemesanan/', Detail_Pemesanan, name='Detail_Pemesanan') ,

]
