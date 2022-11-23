from django.shortcuts import render
from kategori_makanan.models import FoodCategory

def show_kategori_makanan(request):
    context = {"kategori_makanan": FoodCategory.objects.all()}
    return render(request, 'kategori_makanan.html', context)

def show_tambah_kategori_makanan(request):
    return render(request, 'tambah_kategori_makanan.html')