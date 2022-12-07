from django.shortcuts import render, redirect
from .models import RestaurantRepository

# Create your views here.
def jam_buat_op(request):
    print("test")
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
    return render(request, 'jam_buat.html', {"fail_add": fail_add}) 

def jam_daftar(request):
    email = request.session.get('user_email')
    rr = RestaurantRepository()
    restaurant = rr.getByEmail(email)
    return render(request, 'jam_daftar.html', {"restaurant": restaurant})

def jam_ubah(request):
    return render(request, 'jam_ubah.html')