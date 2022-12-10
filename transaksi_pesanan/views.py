from django.shortcuts import render
from transaksi_pesanan.forms import *
from transaksi_pesanan.models import *

# Views Restoran

def p_berlangsung(response):
    return render(response, 'pesanan_berlangsung.html')

def p_detail(response):
    return render(response, 'pesanan_detail.html')

# Views Pelanggan

def tambah_transaksi(request):
    context = {"form":FormAlamat()}
    return render(request, 'tambah_pesanan.html', context)

def pilih_restoran(request):
    return render(request, "pilih_restoran.html")

def pilih_makanan(request):
    return render(request, "pilih_makanan.html")

def daftar_pesanan_pelanggan(request):
    return render(request, 'daftar_pesanan_pelanggan.html')

def konfirmasi_pembayaran(request):
    return render(request, 'konfirmasi_pembayaran.html')

def ringkasan_pesanan(request):
    return render(request, 'ringkasan_pesanan.html')

def pesanan_berlangsung_pelanggan(request):
    return render(request, 'pesanan_berlangsung_pelanggan.html')

def detail_pesanan_pelanggan(request):
    return render(request, 'detail_pesanan_pelanggan.html')