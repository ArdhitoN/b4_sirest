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


# Create your views here.
def show_buat_makanan(request):
    current_user = auth.get_user(request)

    
    # if(not current_user.is_admin):
    #     return redirect('authentication:login')

    context = {}
    return render(request, "buat_makanan.html", context)


def show_makanan_restoView(request):
    current_user = auth.get_user(request)

    
    # if(not current_user.is_admin):
    #     return redirect('authentication:login')

    context = {}
    return render(request, "daftarMakanan_restoView.html", context)


def show_makanan_nonRestoView(request):
    current_user = auth.get_user(request)

    
    # if(not current_user.is_admin):
    #     return redirect('authentication:login')

    context = {}
    return render(request, "daftarMakanan_nonRestoView.html", context)


def show_detail_resto(request):
    current_user = auth.get_user(request)

    
    # if(not current_user.is_admin):
    #     return redirect('authentication:login')

    context = {}
    return render(request, "detail_resto.html", context)



def show_detail_resto_NRView(request):
    current_user = auth.get_user(request)

    
    # if(not current_user.is_admin):
    #     return redirect('authentication:login')

    context = {}
    return render(request, "detail_resto_NRView.html", context)



def show_daftar_restoran(request):
    current_user = auth.get_user(request)

    
    # if(not current_user.is_admin):
    #     return redirect('authentication:login')

    context = {}
    return render(request, "daftar_restoran.html", context)


def show_daftar_restoran_NRView(request):
    current_user = auth.get_user(request)

    
    # if(not current_user.is_admin):
    #     return redirect('authentication:login')

    context = {}
    return render(request, "daftar_restoran_NRView.html", context)


def show_ubah_makanan(request):
    current_user = auth.get_user(request)

    
    # if(not current_user.is_admin):
    #     return redirect('authentication:login')

    context = {}
    return render(request, "ubah_makanan.html", context)

def hapus_makanan(request):
    current_user = auth.get_user(request)


    return

    