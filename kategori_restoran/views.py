from django.shortcuts import render
from kategori_restoran.models import RestaurantCategory
from django.shortcuts import redirect
from django.contrib import messages

def show_kategori_restoran(request):
    #context = {"kategori_restoran": RestaurantCategory.objects.all()}
    context = {}
    return render(request, 'kategori_restoran.html', context)
    
def show_tambah_kategori_restoran(request):
    if request.method == "POST":
        nama_kategori = request.POST.get("kategori")
        if (nama_kategori == ""):
            messages.info(request, "Data yang diisikan belum lengkap, silakan lengkapi data terlebih dahulu.")
        else:
            RestaurantCategory.objects.create(name = nama_kategori)
            return redirect("kategori_restoran:show_kategori_restoran")
    return render(request, 'tambah_kategori_restoran.html')

def delete_kategori_restoran(request):
    #RestaurantCategory.objects.get(pk = pk).delete()
    return redirect("kategori_restoran:show_kategori_restoran")