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
def show_buat_makanan(request, error_msg=False, ingredient_input_counter = 1):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    
    uar = UserAccRepository()

    if(not uar.isRestaurant((request.session.get('user_email')))):
        return redirect('/authentication/login')
    
    #TODO: ambil kategori makanan 


    kategori_makanan_repo = Food_Category_Repository()
    list_kategori_makanan = kategori_makanan_repo.getAllFoodCategory()

    ingredient_repo = Ingredient_Repository()
    list_ingredient = ingredient_repo.getAllIngredient()



    context = {
        'list_kategori_makanan' : list_kategori_makanan,
        'list_ingredient' : list_ingredient,
        'error_msg' : error_msg,
        'ingredient_input_counter' : range(ingredient_input_counter), 
    }
    
    return render(request, "buat_makanan.html", context)


def buat_makanan(request):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    

    uar = UserAccRepository()

    if(not uar.isRestaurant((request.session.get('user_email')))):
        return redirect('/authentication/login')

    print("sadasda")
    if request.method == "POST":

        email = request.session.get('user_email')
        Restaurant_Repo = RestaurantRepository()


        restaurant = Restaurant_Repo.getByEmail(email)
        rname = restaurant.rname
        rbranch =  restaurant.rbranch


        foodname = request.POST["foodname"]
        description = request.POST["description"]
        stock = request.POST["stock"]
        price = request.POST["price"]
        fcategory = request.POST["fcategory"]

        food_repo = FoodRepository()
        queryResult = food_repo.createFood(rname, rbranch, foodname, description, stock, price, fcategory)


        ingredient = request.POST["ingredient"]
        print(ingredient)

        food_ingredient_repo = Food_Ingredient_Repository()
        queryResult = food_ingredient_repo.createFoodIngredient(rname, rbranch, foodname, ingredient)

        
        if type(queryResult) == bool:
            return redirect('/Makanan/daftarMakanan_restoView/')
        else:
            return show_buat_makanan(request, queryResult)

    return show_buat_makanan(request, queryResult)




def show_update_makanan(request, FoodName, error_msg=False):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    
    uar = UserAccRepository()

    if(not uar.isRestaurant((request.session.get('user_email')))):
        return redirect('/authentication/login')

    email = request.session.get('user_email')
    Restaurant_Repo = RestaurantRepository()


    restaurant = Restaurant_Repo.getByEmail(email)
    rname = restaurant.rname
    rbranch =  restaurant.rbranch


    food_repo = FoodRepository()
    food = food_repo.getFoodByName(rname, rbranch, FoodName)

    

    food_category_repo = Food_Category_Repository()
    food_category_name = food_category_repo.getCategoryById(food.FCategory)

    list_kategori_makanan = food_category_repo.getAllFoodCategory()

    ingredient_repo = Ingredient_Repository()
    list_ingredient = ingredient_repo.getAllIngredient()


    print(food)
    print(food_category_name)
    print(list_ingredient)

    context = {
        'food' : food,
        'food_category_name': food_category_name,
        'list_kategori_makanan' : list_kategori_makanan,
        'list_ingredient' : list_ingredient,
        'error_msg' : error_msg,
    }
    return render(request, "ubah_makanan.html", context)




def update_makanan(request, FoodName):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')

    uar = UserAccRepository()

    if(not uar.isRestaurant((request.session.get('user_email')))):
        return redirect('/authentication/login')

    if request.method == "POST":

        email = request.session.get('user_email')
        Restaurant_Repo = RestaurantRepository()


        restaurant = Restaurant_Repo.getByEmail(email)
        rname = restaurant.rname
        rbranch =  restaurant.rbranch

        description = request.POST["description"]
        stock = request.POST["stock"]
        price = request.POST["price"]
        fcategory = request.POST["fcategory"]

        food_repo = FoodRepository()
        queryResult = food_repo.updateFood(rname, rbranch, FoodName, description, stock, price, fcategory)

        print("======================")
        print(queryResult)
        print("======================")


        ingredient = request.POST["ingredient"]
        print(ingredient)

        food_ingredient_repo = Food_Ingredient_Repository()

        food_ingredient_repo.createFoodIngredient(rname, rbranch, FoodName, ingredient)

        # queryResult = food_ingredient_repo.createFoodIngredient()


        print(queryResult)


        
        if type(queryResult) == bool:
            return redirect('/Makanan/daftarMakanan_restoView/')
        else:
            return show_buat_makanan(request, queryResult)



    return show_buat_makanan(request, queryResult)


def hapus_makanan(request, FoodName):

    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    
    uar = UserAccRepository()

    if(not uar.isRestaurant((request.session.get('user_email')))):
        return redirect('/authentication/login')

    if request.method == "GET":
        email = request.session.get('user_email')
        Restaurant_Repo = RestaurantRepository()


        restaurant = Restaurant_Repo.getByEmail(email)
        rname = restaurant.rname
        rbranch =  restaurant.rbranch

        food_repo = FoodRepository()
        
        food_ingredient_repo = Food_Ingredient_Repository()

        ingredientId = food_ingredient_repo.getIngredientId(rname, rbranch, FoodName)

        for i in range(len(ingredientId)):
            queryResult =  food_ingredient_repo.deleteFoodIngredient(rname, rbranch, FoodName, ingredientId[i])

                
        if type(queryResult) == bool:
            pass
        else:
            return show_makanan_restoView(request, queryResult)

        queryResult = food_repo.deleteFood(rname, rbranch, FoodName)

        if type(queryResult) == bool:
            return redirect('/Makanan/daftarMakanan_restoView/')
        else:
            return show_makanan_restoView(request, queryResult)





def show_makanan_restoView(request, error_msg = False):

    if 'user_email' not in request.session:
        return redirect('/authentication/login')

    
    uar = UserAccRepository()

    if(not uar.isRestaurant((request.session.get('user_email')))):
        return redirect('/authentication/login')

    email = request.session.get('user_email')

    Restaurant_Repo = RestaurantRepository()
    
    
    restaurant = Restaurant_Repo.getByEmail(email)
    rname = restaurant.rname
    rbranch =  restaurant.rbranch

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


    context = {'list_food': list_makanan, 
                'error_msg' : error_msg}

    return render(request, "daftarMakanan_restoView.html", context)


def show_makanan_nonRestoView(request, rname, rbranch):

    if 'user_email' not in request.session:
        return redirect('/authentication/login')

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

    if 'user_email' not in request.session:
        return redirect('/authentication/login')

    restoran_repo = RestaurantRepository()
    restoran = restoran_repo.getByRnameAndRbranch(rname, rbranch)

    kategori_restoran_repo = Restaurant_Category_Repository()
    kategori_restoran = kategori_restoran_repo.getById(restoran.rcategory)

    restoran_opHours_repo = Restaurant_Op_Hours_Repository()
    list_restoran_opHours  = restoran_opHours_repo.getAllRestaurantOpHours(rname, rbranch)
    

    promo_restoran_repo = Restaurant_Promo_Repository()

    #TODO : FILTER BERDASARKAN WAKTU
    list_promo_restoran = promo_restoran_repo.getAllRestaurantPromo(rname, rbranch)
    
    list_promo_restoran_fix = []

    time = datetime.datetime.now()

    for promo in list_promo_restoran:
        if(promo.start < time and promo.promoend > time) :
            list_promo_restoran_fix.append(promo)

    # print(list_promo_restoran)

    context = {'restoran': restoran,
                'kategori_restoran': kategori_restoran,
                'list_restoran_opHours' : list_restoran_opHours,
                'list_promo_restoran': list_promo_restoran_fix
                }
    return render(request, "detail_resto.html", context)



def show_daftar_restoran(request):

    if 'user_email' not in request.session:
        return redirect('/authentication/login')

    restoran_repo = RestaurantRepository()
    
    list_restoran = restoran_repo.getAll()
    print(list_restoran)


    context = {'list_restoran': list_restoran, 
                'n': range(len(list_restoran))
                }
    

    return render(request, "daftar_restoran.html", context)

    