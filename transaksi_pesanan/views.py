from django.shortcuts import render, redirect
from django.http import HttpResponse
from transaksi_pesanan.forms import *
from transaksi_pesanan.models import *

# Views Restoran

def p_berlangsung(request):
    
    if 'user_email' not in request.session:
        return redirect('/authentication/login')

    email = request.session['user_email']

    tr = TransaksiRepository()
    rr = RestaurantRepository()
    restaurant =  rr.getRestaurantByEmail(email)

    transaksi_foods = tr.getAllTransaksi(restaurant.rname, restaurant.rbranch)

    print(transaksi_foods[0].transaction_datetime)
    # print(transaksi_foods[0].date_epoch)

    return render(request, 'pesanan_berlangsung_restoran.html', {"transaksi_foods": transaksi_foods, 'restaurant': restaurant})

# def p_detail(request, user_email, datetime):

#     if 'user_email' not in request.session:
#         return redirect('/authentication/login')

#     email = request.session['user_email']

#     tr = TransaksiRepository()
#     rr = RestaurantRepository()
#     restaurant =  rr.getRestaurantByEmail(email)

#     transaksi = tr.detailTransaksiByEmailDatetime(user_email, datetime, restaurant.rname, restaurant.rbranch)
#     return render(request, 'pesanan_detail.html', {'transaksi': transaksi})

def p_addstatus(request):
    print(request.POST)
    if request.method == "POST":
        # get email
        email = request.POST["email"]
        # get datetime
        datetime = request.POST["datetime"]
        # get status
        status = request.POST["status"]
        tr = TransaksiRepository()
        if status == "Menunggu konfirmasi":
            success = tr.addTransactionHistory(email, datetime, 'TS_STAT003')
            if success:
                return redirect('/transaksi_pesanan/')
            else:
                return HttpResponse("gabisa confirm")
        if status == "Pesanan Dibuat":
            # assign delivery select random
            tr.addRandomCourierId(email, datetime)
            success = tr.addTransactionHistory(email, datetime, 'TS_STAT004')
            if success:
                return redirect('/transaksi_pesanan/')
            else:
                return HttpResponse("gabisa confirm")
    return HttpResponse("tes add status")

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