from django.shortcuts import render

# Create your views here.
def jam_buat(response):
    return render(response, 'jam_buat.html')

def jam_daftar(response):
    return render(response, 'jam_daftar.html')

def jam_ubah(response):
    return render(response, 'jam_ubah.html')