from django.shortcuts import render

# Create your views here.
def jam_buat(response):
    return render(response, 'jam_buat.html')