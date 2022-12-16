from django.shortcuts import render

from urllib import request

from django.shortcuts import redirect

from django.contrib import messages

from django.contrib import auth

from django.contrib.auth.decorators import login_required

import datetime

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse

from django.core import serializers

from django.utils.decorators import method_decorator

from authentication.models import *

from .models import *

# Create your views here.
def show_buat_tarif(request, message=False):

    if 'user_email' not in request.session:
        return redirect('/authentication/login')
        
    uar = UserAccRepository()
    if(not uar.isAdmin(request.session.get('user_email'))):
        return redirect('/authentication/login')

    context = {'error_msg': message}
    return render(request, "buat_tarif.html", context)


def buat_tarif(request):

    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    
    uar = UserAccRepository()
    if(not uar.isAdmin(request.session.get('user_email'))):
        return redirect('/authentication/login')

    if request.method == "POST":

        province = request.POST["province"]
        motorfee = request.POST["motorfee"]
        carfee = request.POST["carfee"]

        if province == "" or motorfee == "" or carfee == "":
            return show_buat_tarif(request, "Data yang diisikan belum lengkap, silakan lengkapi data terlebih dahulu.")


        tarif_repo = TarifPengirimanRepository()
        queryResult = tarif_repo.createTarifPengiriman(province, motorfee, carfee)
        print(queryResult)

    
    if type(queryResult) == bool:
        return redirect('/tarifPengiriman/daftar_tarif/')
    else:
        return show_buat_tarif(request, queryResult)


def show_daftar_tarif(request, error_msg=False):

    if 'user_email' not in request.session:
        return redirect('/authentication/login')

    uar = UserAccRepository()
    if(not uar.isAdmin(request.session.get('user_email'))):
        return redirect('/authentication/login')

    tarif_repo = TarifPengirimanRepository()
    list_tarif_pengiriman = tarif_repo.getAllTarifPengiriman()
    

    context = {'list_tarif_pengiriman' : list_tarif_pengiriman,
    'error_msg' : error_msg}

    return render(request, "daftar_tarif.html", context)


def show_update_tarif(request, id, province, msg=False):


    if 'user_email' not in request.session:
        return redirect('/authentication/login')

    uar = UserAccRepository()
    if(not uar.isAdmin(request.session.get('user_email'))):
        return redirect('/authentication/login')

    context = { 'id' : id, 
                'province': province,
                'error_msg': msg
                }
    return render(request, "update_tarif.html", context)

def update_tarif(request, id, province):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')

    uar = UserAccRepository()
    if(not uar.isAdmin(request.session.get('user_email'))):
        return redirect('/authentication/login')


    if request.method == "POST":
        new_motorfee = request.POST["motorfee"]
        new_carfee = request.POST["carfee"]

        if new_motorfee == "" or new_carfee == "":
            return show_update_tarif(request, id, province, "Data yang diisikan belum lengkap, silakan lengkapi data terlebih dahulu.")

        tarif_repo = TarifPengirimanRepository()
        queryResult = tarif_repo.updateTarifPengiriman(id, int(new_motorfee), int(new_carfee))

    if type(queryResult) == bool:
        return redirect('/tarifPengiriman/daftar_tarif/')
    else:
        return show_update_tarif(request, id, province, queryResult)


def hapus_tarif(request, id):
    if 'user_email' not in request.session:
        return redirect('/authentication/login') 
    
    uar = UserAccRepository()
    
    if(not uar.isAdmin(request.session.get('user_email'))):
        return redirect('/authentication/login')

    if request.method == "POST":
        tarif_repo = TarifPengirimanRepository()
        
        queryResult = tarif_repo.hapusTarifPengiriman(id)

        return show_daftar_tarif(request, queryResult)
