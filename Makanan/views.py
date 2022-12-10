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


def show_makanan_nonRestoView(request, rname, rbranch):
    food_repo = FoodRepository()
    list_makanan = food_repo.getAllRestaurantFood(rname, rbranch)


    #TODO: ambil kategori makanan 
    kategori_makanan_repo = Food_Category_Repository()
    #TODO: ambil bahan makanan
    food_ingredient_repo = Food_Ingredient_Repository()
    ingredient_repo = Ingredient_Repository()

    for makanan in list_makanan:
        makanan.FCategoryName = kategori_makanan_repo.getCategoryById(makanan.FCategory).name

        list_ingredientId = food_ingredient_repo.getIngredientId(rname, rbranch, makanan.FoodName)

        for ingredientId in list_ingredientId:    
            ingredient_name = ingredient_repo.getIngredientById(ingredientId).name
            makanan.IngredientName.append(ingredient_name)




    context = {'list_food': list_makanan}

    return render(request, "daftarMakanan_nonRestoView.html", context)


def show_detail_resto(request, rname, rbranch):
    restoran_repo = RestaurantRepository()
    restoran = restoran_repo.getByRnameAndRbranch(rname, rbranch)

    kategori_restoran_repo = Restaurant_Category_Repository()
    kategori_restoran = kategori_restoran_repo.getById(restoran.rcategory)

    restoran_opHours_repo = Restaurant_Op_Hours_Repository()
    list_restoran_opHours  = restoran_opHours_repo.getAllRestaurantOpHours(rname, rbranch)
    

    promo_restoran_repo = Restaurant_Promo_Repository()

    #TODO : FILTER BERDASARKAN WAKTU
    list_promo_restoran = promo_restoran_repo.getAllRestaurantPromo(rname, rbranch)

    # print(list_promo_restoran)

    context = {'restoran': restoran,
                'kategori_restoran': kategori_restoran,
                'list_restoran_opHours' : list_restoran_opHours,
                'list_promo_restoran': list_promo_restoran
                }
    return render(request, "detail_resto.html", context)



def show_daftar_restoran(request):
    restoran_repo = RestaurantRepository()
    
    list_restoran = restoran_repo.getAll()
    print(list_restoran)


    context = {'list_restoran': list_restoran, 
                'n': range(len(list_restoran))
                }
    

    return render(request, "daftar_restoran.html", context)


def show_ubah_makanan(request):
    current_user = auth.get_user(request)

    
    # if(not current_user.is_admin):
    #     return redirect('authentication:login')

    context = {}
    return render(request, "ubah_makanan.html", context)

def hapus_makanan(request):
    current_user = auth.get_user(request)


    return

    