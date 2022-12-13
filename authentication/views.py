# from django.shortcuts import render

# from urllib import request

# from django.shortcuts import redirect

# from django.contrib import messages

# from django.contrib import auth

# from django.contrib.auth.decorators import login_required

# import datetime

# from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
# from django.urls import reverse

# from django.core import serializers

# from django.utils.decorators import method_decorator



# def show_register(request):
#     current_user = auth.get_user(request)


#     # if(not current_user.is_admin):
#     #     return redirect('authentication:login')

#     context = {}
#     return render(request, "register.html", context)


# def show_register_admin(request):
#     return render(request, "register_admin.html")

# def show_register_pelanggan(request):
#     return render(request, "register_pelanggan.html")


# def show_login_register(request):
#     return render(request, 'Login&Register.html')

# def show_login(request):
#     return render(request, 'login.html')
from django.shortcuts import render, redirect
from .models import UserAccRepository, TransactionActorRepository, RestaurantRepository, CustomerRepository, Restaurant_Category_Repository, CourierRepository
from django.http import HttpResponse

def index(request):
    return render(request, 'Login&Register.html')

def register_all(request):
    return render(request, 'register.html')

def show_login(request, user_not_exist = False):
    return render(request, 'login.html', {"user_not_exist": user_not_exist})

def login_ua(request):

    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]
        uar = UserAccRepository()
        user_exist = uar.isUserExist(email, password)

        if user_exist:
            request.session['user_email'] = email
            if uar.isAdmin(email):
                # go to dashboard admin
                request.session['role'] = 'admin'
                print("from view = admin")
                return redirect('/authentication/logged_admin/')
            elif uar.isCustomer(email):
                request.session['role'] = 'customer'
                print("from view = cust")
                return redirect('/authentication/logged_customer/')
            elif uar.isRestaurant(email):
                request.session['role'] = 'restaurant'
                print("from view = restaurant")
                return redirect('/authentication/logged_restaurant/')
            else:
                return redirect('/authentication/login-after/')
        else:
            return show_login(request, user_not_exist=True)

def afterlogin(request):
    email = request.session.get('user_email')
    uar = UserAccRepository()
    user = uar.getByEmail(email)
    print(user)
    # test isi session
    # for key, value in request.session.items():
    #     print('{} => {}'.format(key, value))
    return render(request, 'test_page.html', {"user": user})

def after_login_admin(request):
    email = request.session.get('user_email')
    uar = UserAccRepository()
    user = uar.getByEmail(email)
    print(user)
    # test isi session
    # for key, value in request.session.items():
    #     print('{} => {}'.format(key, value))
    return render(request, "Dashboard_Admin.html", {"user": user})

def after_login_customer(request):
    email = request.session.get('user_email')
    uar = UserAccRepository()
    user = uar.getByEmail(email)

    tar = TransactionActorRepository()
    ta = tar.getByEmail(email)

    cr = CustomerRepository()
    customer = cr.getByEmail(email)
    # test isi session
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))
    return render(request, "dash_pelanggan.html", {"user": user, "actor": ta, "customer": customer})

def after_login_restaurant(request):
    email = request.session.get('user_email')
    uar = UserAccRepository()
    user = uar.getByEmail(email)

    tar = TransactionActorRepository()
    ta = tar.getByEmail(email)

    rr = RestaurantRepository()
    restaurant = rr.getByEmail(email)

    # test isi session
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))
    return render(request, "dash_restoran.html", {"user": user, "actor": ta, "restaurant": restaurant})

def logout(request):
    request.session.pop('user_email')
    request.session.pop('role')

    return redirect("/authentication/login")


def show_register_restoran(request, error_msg=False):
    kategori_restoran_repo = Restaurant_Category_Repository()
    list_kategori_restoran = kategori_restoran_repo.getAllRestaurantCategory()
    print(list_kategori_restoran)

    context = {
        'list_kategori_restoran' : list_kategori_restoran,
        'error_msg': error_msg
    }

    return render(request, "register_restoran.html", context)

def register_restoran(request):
    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]
        
        name = request.POST["name"]
        fname = name.split()[0]
        lname = name.split()[1] if len(name.split()) != 1 else " "

        phonenum = request.POST["phonenum"]
        nik = request.POST["nik"]
        bankname = request.POST["bankname"]
        accountno = request.POST["accountno"]

        rname = request.POST["rname"]
        rbranch = request.POST["rbranch"]
        rphonenum = request.POST["rphonenum"]
        street = request.POST["street"]
        district = request.POST["district"]
        city = request.POST["city"]
        province = request.POST["province"]
        rcategory = request.POST["rcategory"]


        user_repo = UserAccRepository()
        queryResult = user_repo.createUserAcc(email, password, phonenum, fname, lname)
 
        if type(queryResult) == bool:
            pass
        else:
            return show_register_restoran(request, queryResult)


        transactionActor_repo = TransactionActorRepository()
        queryResult = transactionActor_repo.createTransactionActor(email, nik, bankname, accountno)
       
        if type(queryResult) == bool:
            pass
        else:
            return show_register_restoran(request, queryResult)


        restoran_repo = RestaurantRepository() 
        queryResult = restoran_repo.createRestoran(rname, rbranch, email, rphonenum, street, district, city, province, rcategory)


        if type(queryResult) == bool:
            return login_ua(request)
        else:
            return show_register_restoran(request, queryResult)


def show_register_kurir(request):

    context = {}
    return render(request, "register_kurir.html", context)


def register_kurir(request):

    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]
        
        name = request.POST["name"]
        fname = name.split()[0]
        lname = name.split()[1] if len(name.split()) != 1 else " "

        phonenum = request.POST["phonenum"]
        nik = request.POST["nik"]
        bankname = request.POST["bankname"]
        accountno = request.POST["accountno"]

        platenum = request.POST["platenum"]
        drivinglicensenum = request.POST["drivinglicensenum"]
        vehicletype = request.POST["vehicletype"]
        vehiclebrand = request.POST["vehiclebrand"]


        user_repo = UserAccRepository()
        queryResult = user_repo.createUserAcc(email, password, phonenum, fname, lname)
 
        if type(queryResult) == bool:
            pass
        else:
            return show_register_restoran(request, queryResult)


        transactionActor_repo = TransactionActorRepository()
        queryResult = transactionActor_repo.createTransactionActor(email, nik, bankname, accountno)
       
        if type(queryResult) == bool:
            pass
        else:
            return show_register_restoran(request, queryResult)


        courier_repo = CourierRepository() 
        queryResult = courier_repo.createCourier(email, platenum, drivinglicensenum, vehicletype, vehiclebrand)


        if type(queryResult) == bool:
            return login_ua(request)
        else:
            return show_register_restoran(request, queryResult)