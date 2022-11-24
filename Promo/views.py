from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# from rest_framework.fields import JSONField
# from rest_framework.utils import json
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView,TemplateView,View
# Create your views here.
# Create your views here.
from itertools import chain
def Buat_Promo(request):
    # current_user = auth.get_user(request)

    
    # if(not current_user.is_admin):
    #     return redirect('authentication:login')

    context = {}
    return render(request, "Buat_Promo.html", context)

def Form_MinimumTransaksi_Promo(request):

    context = {}
    return render(request, "Form_MinimumTransaksi_Promo.html", context)

def Form_HariSpesial_Promo(request):

    context = {}
    return render(request, "Form_HariSpesial_Promo.html", context)

def Daftar_Promo(request):
    # current_user = auth.get_user(request)

    
    # if(not current_user.is_admin):
    #     return redirect('authentication:login')

    context = {}
    return render(request, "Daftar_Promo.html", context)

def Detail_MinimumTransaksi_Promo(request) :
    
    context = {}
    return render(request, "Detail_MinimumTransaksi_Promo.html")

def Detail_HariSpesial_Promo(request) :
    
    context = {}
    return render(request, "Detail_HariSpesial_Promo.html")

def Daftar_Promo_restoran(request) :
        
        context = {}
        return render(request, "Daftar_Promo_restoran.html")

def Form_Ubah_PromoMinTransaksi(request) :
        
        context = {}
        return render(request, "Form_Ubah_PromoMinTransaksi.html", context)

def Form_Ubah_PromoHS(request) :
    context = {}
    
    return render(request, "Form_Ubah_PromoHS.html", context)

def buat_promoMT(request) :
    submitted = False
    response ={}
    form = Form__PromoMT(request.POST, initial= {'Jenis_promo' : 'Minimum Transaksi'})

    if request.method == 'POST':
        if form.is_valid():
           form.save()
        
            # return HttpResponseRedirect('/Daftar_relawan/?submitted=True')
    else :
        form = Form__PromoMT(initial= {'Jenis_promo' : 'Minimum Transaksi Promo'})
        if 'submitted' in request.GET :
            submitted = True

        # return redirect('/Daftar_relawan/selesai')
    response['form']= form
    response['submitted'] = submitted
    return render(request,'Form_MinimumTransaksi_Promo.html',response)

def buat_promoHS(request) :
    submitted = False
    response ={}
    form = Form__PromoHS(request.POST, initial= {'Jenis_promo' : 'Special Day Promo', 'Tanggal_berlangsung' : '01/01/1875'})
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save()
            instance.Jenis_promo = 'Special Day Promo'
            # return HttpResponseRedirect('/Daftar_relawan/?submitted=True')
    else :
        form = Form__PromoHS(initial= {'Jenis_promo' : 'Special Day Promo'})
        if 'submitted' in request.GET :
            submitted = True

        # return redirect('/Daftar_relawan/selesai')
    response['form']= form
    response['submitted'] = submitted
    return render(request,'Form_HariSpesial_Promo.html',response)

class Daftar_Promo2(ListView):
   
    model=Model_Promo2
    template_name = "Daftar_Promo.html"


def DashboardKurir(request) :


    return render(request, 'Dashboard_kurir2.html')

def DashboardAdmin(request) :


    return render(request, 'Dashboard_Admin.html')