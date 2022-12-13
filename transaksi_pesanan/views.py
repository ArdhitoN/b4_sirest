from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.http import HttpResponseBadRequest, JsonResponse
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

def pilih_alamat(request):
    if request.method == "POST":
        form = FormAlamat(request.POST)
        if form.is_valid():
            street = form.cleaned_data["street"]
            district = form.cleaned_data["district"]
            city = form.cleaned_data["city"]
            province = form.cleaned_data["province"]
            response = {
                "street" : street,
                "district" : district,
                "city" : city,
                "province" : province,
            }
            cursor = connection.cursor()
            province_query = f"""
            SELECT * FROM DELIVERY_FEE_PER_KM
            WHERE id = '{province}'
            """
            cursor.execute(province_query)
            province_name = cursor.fetchall()[0][1]
            restaurant_query = f"""
            SELECT * FROM RESTAURANT
            WHERE province = '{province_name}'
            """
            cursor.execute(restaurant_query)
            restaurant_list = cursor.fetchall()
            restaurant_response_list = []
            for restaurant in restaurant_list:
                promo_query = f"""
                SELECT PromoName
                FROM Promo, Restaurant_promo
                WHERE Pid = id
                AND Rname = '{restaurant[0]}'
                AND RBranch = '{restaurant[1]}'
                """
                cursor.execute(promo_query)
                query_result = cursor.fetchall()
                promos = []
                for promo in query_result:
                    promos.append(promo[0])
                restaurant_response_list.append({
                "rname": restaurant[0],
                "rbranch": restaurant[1],
                "remail": restaurant[2],
                "rpromo": promo})
            response.update({"restaurants" : restaurant_response_list})
            return JsonResponse(response)
    return HttpResponseBadRequest()
            
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