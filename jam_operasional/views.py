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

def jam_daftar(request, fail_delete = False):
    email = request.session.get('user_email')
    rr = RestaurantRepository()
    restaurant = rr.getByEmail(email)
    return render(request, 'jam_daftar.html', {"restaurant": restaurant, "fail_delete": fail_delete})

def jam_delete_op(request, day):
    print("masuk delete_op")
    email = request.session.get('user_email')
    rr = RestaurantRepository()
    success = rr.deleteOperatingHours(email, day)
    if success:
        return redirect('/jam_operasional/daftar/')
    else:
        print('fail delete at views')

def jam_ubah(request):
    return render(request, 'jam_ubah.html')