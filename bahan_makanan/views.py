from django.shortcuts import render
from bahan_makanan.models import FoodMaterial
from django.shortcuts import redirect
from django.contrib import messages

def show_bahan_makanan(request):
    #context = {"bahan_makanan": FoodMaterial.objects.all()}
    context = {}
    return render(request, 'bahan_makanan.html', context)
    
def show_tambah_bahan_makanan(request):
    if request.method == "POST":
        nama_bahan = request.POST.get("bahan")
        if (nama_bahan == ""):
            messages.info(request, "Data yang diisikan belum lengkap, silakan lengkapi data terlebih dahulu.")
        else:
            FoodMaterial.objects.create(name=nama_bahan)
            return redirect("bahan_makanan:show_bahan_makanan")
    return render(request, 'tambah_bahan_makanan.html')

def delete_bahan_makanan(request):
    #FoodMaterial.objects.get(pk = pk).delete()
    return redirect("bahan_makanan:show_bahan_makanan")