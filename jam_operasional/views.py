from django.shortcuts import render, redirect
from .models import RestaurantRepository

# Create your views here.
def jam_buat_op(request):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')

    email = request.session.get('user_email')
    if request.method == "POST":
        # get day
        day = request.POST["day"]
        print(day)
        # get starthour
        starthours = request.POST["starthours"]
        print(starthours)
        # get endhours
        endhours = request.POST["endhours"]
        print(endhours)
        rr = RestaurantRepository()
        success = rr.addOperatingHours(email, day, starthours, endhours)
        if success:
            return redirect('/jam_operasional/daftar/')
        else:
            return jam_buat(request, fail_add=True)

def jam_buat(request, fail_add = False):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')

    return render(request, 'jam_buat.html', {"fail_add": fail_add}) 

def jam_daftar(request, fail_delete = False):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')

    email = request.session.get('user_email')
    rr = RestaurantRepository()
    restaurant = rr.getByEmail(email)
    return render(request, 'jam_daftar.html', {"restaurant": restaurant, "fail_delete": fail_delete})

def jam_delete_op(request, day):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')

    print("masuk delete_op")
    email = request.session.get('user_email')
    rr = RestaurantRepository()
    success = rr.deleteOperatingHours(email, day)
    if success:
        return redirect('/jam_operasional/daftar/')
    else:
        print('fail delete at views')

def jam_ubah(request, day, fail_ubah = False):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')

    print("masuk jam_ubah")
    email = request.session.get('user_email')
    rr = RestaurantRepository()
    hour = rr.getHour(email, day)
    return render(request, 'jam_ubah.html', {"hour": hour, "fail_ubah": fail_ubah})

def jam_ubah_op(request, day):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
        
    print("masuk jam_ubah_op")
    email = request.session.get('user_email')
    if request.method == "POST":
        # get starthour
        starthours = request.POST["starthours"]
        print(starthours)
        # get endhours
        endhours = request.POST["endhours"]
        print(endhours)
        rr = RestaurantRepository()
        success = rr.updateOperatingHours(email, day, starthours, endhours)
        if success:
            return redirect('/jam_operasional/daftar/')
        else:
            return jam_ubah(request, day, fail_ubah=True)
    