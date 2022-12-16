from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# from rest_framework.fields import JSONField
# from rest_framework.utils import json
from django.db import connection
from .models import *
from django.views.generic import ListView, DetailView,TemplateView,View
# Create your views here.
# Create your views here.
from itertools import chain
from authentication.models import *


def list_promo(request) :
    # role = request.session.get('role')
     if 'user_email' not in request.session:
        return redirect('/authentication/login')
        
     uar = UserAccRepository()
     if( uar.isAdmin(request.session.get('user_email'))):
        promo_repo = PromoRepository()
        categories = promo_repo.get_all()
        context = {"Promolist" : categories}
        return render(request, 'Baca_Admin.html', context)

     elif ( uar.isRestaurant(request.session.get('user_email'))): 
        promo_repo = PromoRepository()
        categories = promo_repo.get_all()
        context = {"Promolist" : categories}
        return render(request, 'Baca_Restaurant.html', context)
     else :
        return redirect('/authentication/login')


def buat_HS(request) :
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    
    uar = UserAccRepository()    

    if( not uar.isAdmin(request.session.get('user_email'))):
        return redirect('/authentication/login')
    if request.method == "POST":
        nama_promo = request.POST.get("nama_promo")
        kuantitas =  request.POST.get("kuantitas")
        if (kuantitas  == ""):
            messages.info(request, "Data yang diisikan belum lengkap, silakan lengkapi data terlebih dahulu.")
        else :
            kuantitas = int(kuantitas)
            if (kuantitas < 1 or kuantitas > 100) :
                 messages.info(request, "persentase diskon harus di antara 1 hingga 100")
        tanggal = request.POST.get("tanggal")
        if (nama_promo == "" or tanggal == ""):
            messages.info(request, "Data yang diisikan belum lengkap, silakan lengkapi data terlebih dahulu.")
        

        else:
            promo_repo = PromoRepository()

            # if (promo_repo.check_promo(nama_promo) == True) :
            #     messages.info(request, "Nama Promo sudah ada, silakan gunakan nama promo yang lain")
            promo_repo.insertHS(nama_promo,kuantitas,tanggal)
            # category_repo = FoodCategoryRepository()
            # category_repo.add_category(nama_kategori)
            return redirect("Promo:Baca_Admin")
            # return render(request, 'Buat_PromoHS.html',)
    else :
        return render(request, 'Buat_PromoHS.html')


def buat_MT(request) :
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    
    uar = UserAccRepository()    
    
    if( not uar.isAdmin(request.session.get('user_email'))):
        return redirect('/authentication/login')

    if request.method == "POST":
        nama_promo = request.POST.get("nama_promo")
        kuantitas =  request.POST.get("kuantitas")
        if (kuantitas  == ""):
            messages.info(request, "Data yang diisikan belum lengkap, silakan lengkapi data terlebih dahulu.")
        else :
            kuantitas = int(kuantitas)
            if (kuantitas < 1 or kuantitas > 100) :
                 messages.info(request, "persentase diskon harus di antara 1 hingga 100")
        mintrans = request.POST.get("mintrans")
        if (nama_promo == "" or mintrans== ""):
            messages.info(request, "Data yang diisikan belum lengkap, silakan lengkapi data terlebih dahulu.")
        

        else:
            promo_repo = PromoRepository()

            # if (promo_repo.check_promo(nama_promo) == True) :
            #     messages.info(request, "Nama Promo sudah ada, silakan gunakan nama promo yang lain")
            promo_repo.insertMT(nama_promo,kuantitas,mintrans)
            # category_repo = FoodCategoryRepository()
            # category_repo.add_category(nama_kategori)
            return redirect("Promo:Baca_Admin")
            # return render(request, 'Buat_PromoHS.html',)
    else :
        return render(request, 'Buat_PromoMT.html')

def detailpromo(request,id) :
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    
    uar = UserAccRepository()    
    
    # if( not uar.isAdmin(request.session.get('user_email')) or not uar.isRestaurant(request.session.get('user_email')) ):
    
    #     return redirect('/authentication/login')
   
    promo_repo = PromoRepository()
    promo = promo_repo.detail_promo(id)
    context = {"promolist" : promo}
    
    print(promo[0].id)
    return render(request, 'Detail_Promo2.html', context)

def ubahpromo(request,id) :
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    
    uar = UserAccRepository()    
    
    if( not uar.isAdmin(request.session.get('user_email'))):
        return redirect('/authentication/login')

    promo_repo = PromoRepository()
    promo = promo_repo.detail_promo(id)
    context = {"promolist" : promo}
    print(promo)
    if (request.method == "POST"):
        id = promo[0].id
        tanggal_awal = promo[0].tanggal
        mintrans_awal = promo[0].mintrans
        kuantitas =  request.POST.get("kuantitas")
        tanggal = request.POST.get("tanggal")
        mintrans = request.POST.get("mintrans")
        print("masuk")
        promo_repo.ubah(id,tanggal_awal,mintrans_awal,kuantitas,tanggal,mintrans)

        return redirect("Promo:Baca_Admin")
    else :

        return render(request,'ubah_promo.html',context)

def buatpromo(request) :
    return render(request, 'menu.html',)

# def detailpromo2(request) :
#     return render(request, 'Detail_Promo2.html')
def deletepromo(request,id) :
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    
    uar = UserAccRepository()    
    
    if( not uar.isAdmin(request.session.get('user_email'))):
        return redirect('/authentication/login')

    promo_repo = PromoRepository()
    promo_repo.delete_promo(id)
    # context = {"promolist" : promo}
    
    # print(promo[0].id)
    return redirect("Promo:Baca_Admin")
