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
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    if request.method == "POST":
        form = FormAlamat(request.POST)
        if form.is_valid():
            street = form.cleaned_data["street"]
            district = form.cleaned_data["district"]
            city = form.cleaned_data["city"]
            province = form.cleaned_data["province"]
            request.session["street"] = street
            request.session["district"] = district
            request.session["city"] = city
            request.session["province"] = province
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
                    promos.append({"promo_name":promo[0]})
                restaurant_response_list.append({
                "rname": restaurant[0],
                "rbranch": restaurant[1],
                "remail": restaurant[2],
                "rpromo": promo})
            request.session["restaurants"] = restaurant_response_list
            return redirect("transaksi_pesanan:pilih_restoran")
    context = {"form":FormAlamat()}
    return render(request, 'tambah_pesanan.html', context)
            
def pilih_restoran(request):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    if request.method == "POST":
        restaurant = request.POST.get("restoran").split("||")
        request.session["restaurant_name"] = restaurant[0]
        request.session["restaurant_branch"] = restaurant[1]
        return redirect("transaksi_pesanan:pilih_makanan")
    context = {"restaurants": request.session["restaurants"]}
    return render(request, "pilih_restoran.html", context)

def pilih_makanan(request):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    if request.method == "POST":
        food_amount_list = []
        note_list = []
        total_food = 0
        food_list = request.session["food_list"]

        for i in range(len(food_list)):
            food_amount = int(request.POST.get("amount" + str(i)))
            note = ""
            if not food_amount:
                note = request.POST.get("note"+str(i))
            food_amount_list.append(food_amount)
            note_list.append(note)
            total_food += food_amount
        payment_method  = request.POST.get("metode-bayar")
        delivery_method = request.POST.get("metode-antar")
        
        # Store order to database
        cursor = connection.cursor()
        cursor.execute("SELECT now()::timestamp(0);")
        timestamp = cursor.fetchone()[0]
        request.session["order_timestamp"] = timestamp
        cursor.execute(f"SELECT * FROM DELIVERY_FEE_PER_KM WHERE id = \'{request.session['province']}\'")
        province = cursor.fetchone()[1]
        order_query = f"""
        INSERT INTO TRANSACTION
        (Email, datetime, street, district, city, province, totalfood, totaldiscount, deliveryfee, totalprice, rating)
        VALUES(
            \'{request.session["user_email"]}\',            
            \'{timestamp}\',
            \'{request.session["street"]}\',
            \'{request.session["district"]}\',
            \'{request.session["city"]}\',
            \'{province}\',
            {str(total_food)},
            0,
            0,
            0,
            0)"""
        cursor.execute(order_query)

        # Store food amount to database
        food_summary = []
        for i in range(len(food_list)):
            if not food_amount[i]:
                order_food_query = f"""
                INSERT INTO TRANSACTION_FOOD
                VALUES (
                    \'{request.session["user_email"]}\',
                    \'{timestamp}\',
                    \'{request.session["restaurant_name"]}\',
                    \'{request.session["restaurant_branch"]}\',
                    \'{food_list[i].name}\',
                    {food_amount_list[i]},
                """
                if note_list[i] == "":
                    order_food_query += f"{note_list[i]}"
                order_food_query += ");"
                cursor.execute(order_food_query)
        return redirect("transaksi_pesanan:daftar_pesanan_pelanggan")

    cursor = connection.cursor()
    query = f"""
    SELECT * FROM FOOD
    WHERE rname = \'{request.session["restaurant_name"]}\'
    AND rbranch = \'{request.session["restaurant_branch"]}\'
    """
    cursor.execute(query)
    query_result = cursor.fetchall()
    food_list = []
    for food in query_result:
        food_list.append({"name":food[2], "description":food[3], "stock":food[4], "price":food[5], "category":food[6]})
    request.session["food_list"] = food_list
    cursor.execute("SELECT * FROM PAYMENT_METHOD")
    payment_option_result = cursor.fetchall()
    payment_options = []
    for payment_option in payment_option_result:
        payment_options.append({"id": payment_option[0], "name": payment_option[1]})
    context = {"food_list" : food_list, "payment_options": payment_options}
    return render(request, "pilih_makanan.html", context)

def daftar_pesanan_pelanggan(request):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    return render(request, 'daftar_pesanan_pelanggan.html')

def konfirmasi_pembayaran(request):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    return render(request, 'konfirmasi_pembayaran.html')

def ringkasan_pesanan(request):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    return render(request, 'ringkasan_pesanan.html')

def pesanan_berlangsung_pelanggan(request):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    return render(request, 'pesanan_berlangsung_pelanggan.html')

def detail_pesanan_pelanggan(request):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    return render(request, 'detail_pesanan_pelanggan.html')