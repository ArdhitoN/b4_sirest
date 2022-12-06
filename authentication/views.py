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

# def show_register_restoran(request):
#     return render(request, "register_restoran.html")


# def show_register_kurir(request):
#     current_user = auth.get_user(request)


#     # if(not current_user.is_admin):
#     #     return redirect('authentication:login')

#     context = {}
#     return render(request, "register_kurir.html", context)

# def show_register_admin(request):
#     return render(request, "register_admin.html")

# def show_register_pelanggan(request):
#     return render(request, "register_pelanggan.html")


# def show_login_register(request):
#     return render(request, 'Login&Register.html')

# def show_login(request):
#     return render(request, 'login.html')
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

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
            request.session['user_password'] = password
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
    uar = UserAccRepository()
    user = uar.getByEmailPassword(request.session.get('user_email'), request.session.get('user_password'))
    print(user)
    # test isi session
    # for key, value in request.session.items():
    #     print('{} => {}'.format(key, value))
    return render(request, 'test_page.html', {"user": user})

def after_login_admin(request):
    uar = UserAccRepository()
    user = uar.getByEmailPassword(request.session.get('user_email'), request.session.get('user_password'))
    print(user)
    # test isi session
    # for key, value in request.session.items():
    #     print('{} => {}'.format(key, value))
    return render(request, "Dashboard_Admin.html", {"user": user})

def after_login_customer(request):
    email_session = request.session.get('user_email')
    password_session = request.session.get('user_password')

    uar = UserAccRepository()
    user = uar.getByEmailPassword(email_session, password_session)

    tar = TransactionActorRepository()
    ta = tar.getByEmail(email_session)

    cr = CustomerRepository()
    customer = cr.getByEmail(email_session)
    # test isi session
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))
    return render(request, "dash_pelanggan.html", {"user": user, "actor": ta, "customer": customer})

def after_login_restaurant(request):
    email_session = request.session.get('user_email')
    password_session = request.session.get('user_password')

    uar = UserAccRepository()
    user = uar.getByEmailPassword(email_session, password_session)

    tar = TransactionActorRepository()
    ta = tar.getByEmail(email_session)

    rr = RestaurantRepository()
    restaurant = rr.getByEmail(email_session)

    # test isi session
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))
    return render(request, "dash_restoran.html", {"user": user, "actor": ta, "restaurant": restaurant})
