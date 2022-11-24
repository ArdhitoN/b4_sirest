from django.shortcuts import render
from kategori_makanan.models import FoodCategory
from django.shortcuts import redirect
from django.contrib import messages

def show_kategori_makanan(request):
    #context = {"kategori_makanan": FoodCategory.objects.all()}
    context = {}
    return render(request, 'kategori_makanan.html', context)
    
def show_tambah_kategori_makanan(request):
    if request.method == "POST":
        nama_kategori = request.POST.get("kategori")
        if (nama_kategori == ""):
            messages.info(request, "Data yang diisikan belum lengkap, silakan lengkapi data terlebih dahulu.")
        else:
            FoodCategory.objects.create(name = nama_kategori)
            return redirect("kategori_makanan:show_kategori_makanan")
    return render(request, 'tambah_kategori_makanan.html')

def delete_kategori_makanan(request):
    #FoodCategory.objects.get(pk = pk).delete()
    return redirect("kategori_makanan:show_kategori_makanan")