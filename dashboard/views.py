from django.shortcuts import render

# Create your views here.
def dash_pelanggan(response):
    return render(response, 'dash_pelanggan.html')

def dash_resto(response):
    return render(response, 'dash_restoran.html')