from django.shortcuts import render
from .views import *
# Create your views here.
def Baca_PromoRestoran(request):
    # current_user = auth.get_user(request)

    
    # # if(not current_user.is_admin):
    # #     return redirect('authentication:login')

    context = {}
    return render(request, "Baca_PromoRestoran.html")

def Buat_PromoRestoran(request):
    # current_user = auth.get_user(request)

    
    # # if(not current_user.is_admin):
    # #     return redirect('authentication:login')

    context = {}
    return render(request, "Buat_PromoRestoran.html")

def Ubah_PromoRestoran(request):
    # current_user = auth.get_user(request)

    
    # # if(not current_user.is_admin):
    # #     return redirect('authentication:login')

    context = {}
    return render(request, "Ubah_PromoRestoran.html")

def Detail_PromoRestoran(request):
    # current_user = auth.get_user(request)

    
    # # if(not current_user.is_admin):
    # #     return redirect('authentication:login')

    context = {}
    return render(request, "Detail_PromoRestoran.html")