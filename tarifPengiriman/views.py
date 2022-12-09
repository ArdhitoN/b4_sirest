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


from .models import *

# Create your views here.
def show_buat_tarif(request):

    context = {}
    return render(request, "buat_tarif.html", context)


def show_daftar_tarif(request):

    tarif_repo = TarifPengirimanRepository()
    list_tarif_pengiriman = tarif_repo.getAllTarifPengiriman()
    

    context = {'list_tarif_pengiriman' : list_tarif_pengiriman}

    return render(request, "daftar_tarif.html", context)


def show_update_tarif(request, id, province, msg=False):

    context = { 'id' : id, 
                'province': province,
                'error_msg': msg
                }
    return render(request, "update_tarif.html", context)

def update_tarif(request, id, province):

    if request.method == "POST":
        new_motorfee = int(request.POST["motorfee"])
        new_carfee = int(request.POST["carfee"])

        tarif_repo = TarifPengirimanRepository()
        queryResult = tarif_repo.updateTarifPengiriman(id, new_motorfee, new_carfee)

    if type(queryResult) == bool:
        return redirect('/tarifPengiriman/daftar_tarif/')
    else:
        return show_update_tarif(request, id, province, queryResult)


def hapus_tarif(request, id):
    if request.method == "POST":
        tarif_repo = TarifPengirimanRepository()
        
        tarif_repo.hapusTarifPengiriman(id)

        return redirect('/tarifPengiriman/daftar_tarif/')
