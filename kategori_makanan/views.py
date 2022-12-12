from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from kategori_makanan.models import *

def show_kategori_makanan(request):
    category_repo = FoodCategoryRepository()
    categories = category_repo.get_all()
    context = {"kategori_makanan" : categories}
    return render(request, 'kategori_makanan.html', context)
    
def show_tambah_kategori_makanan(request):
    if request.method == "POST":
        nama_kategori = request.POST.get("kategori")
        if (nama_kategori == ""):
            messages.info(request, "Data yang diisikan belum lengkap, silakan lengkapi data terlebih dahulu.")
        else:
            category_repo = FoodCategoryRepository()
            category_repo.add_category(nama_kategori)
            return redirect("kategori_makanan:show_kategori_makanan")
    return render(request, 'tambah_kategori_makanan.html')

def delete_kategori_makanan(request, id):
    category_repo = FoodCategoryRepository()
    category_repo.delete_category(id)
    return redirect('kategori_makanan:show_kategori_makanan')