from django.shortcuts import render
from .models import TransactionActorRepository
# Create your views here.

def index(request):
    return render(request, 'restopay_index.html')

def isi(request):
    return render(request, 'restopay_isi.html')

def tarik(request):
    return render(request, 'restopay_tarik.html')

def all_restopay(request):

    tar = TransactionActorRepository()
    actors = tar.getAll()
    return render(request, 'test_db_ta.html', {"actors": actors})
