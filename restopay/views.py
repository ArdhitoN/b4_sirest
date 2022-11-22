from django.shortcuts import render

# Create your views here.


def index(response):
    return render(response, 'restopay_index.html')

def isi(response):
    return render(response, 'restopay_isi.html')

def tarik(response):
    return render(response, 'restopay_tarik.html')
