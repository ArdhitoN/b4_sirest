from django.urls import path
from transaksi_pesanan.views import *

app_name = 'transaksi_pesanan'

urlpatterns = [
    # resto
    path('', p_berlangsung, name='rpesanan_index'),
    # path('detail/', p_detail, name='rpesanan_detail'),
    path('add_status/', p_addstatus, name='rpesanan_confirm'),
    # pelanggan
    path('tambah/', tambah_transaksi, name="tambah_transaksi"),
    path('pilih_alamat/', pilih_alamat, name="pilih_alamat"),
    path('pilih_restoran/', pilih_restoran, name="pilih_restoran"),
    path('pilih_makanan/', pilih_makanan, name="pilih_makanan"),
    path('daftar_pesanan_pelanggan/', daftar_pesanan_pelanggan, name="daftar_pesanan_pelanggan"),
    path('konfirmasi_pembayaran/', konfirmasi_pembayaran, name='konfirmasi_pembayaran'),
    path('ringkasan_pesanan/', ringkasan_pesanan, name='ringkasan_pesanan'),
    path('pesanan_berlangsung_pelanggan/', pesanan_berlangsung_pelanggan, name='pesanan_berlangsung_pelanggan'),
    path('detail_pesanan_pelanggan/', detail_pesanan_pelanggan, name='detail_pesanan_pelanggan'),
]