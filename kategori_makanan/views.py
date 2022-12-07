from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

def show_kategori_makanan(request):
    context = {}
    return render(request, 'kategori_makanan.html', context)
    
def show_tambah_kategori_makanan(request):
    if request.method == "POST":
        nama_kategori = request.POST.get("kategori")
        if (nama_kategori == ""):
            messages.info(request, "Data yang diisikan belum lengkap, silakan lengkapi data terlebih dahulu.")
        else:
            return redirect("kategori_makanan:show_kategori_makanan")
    return render(request, 'tambah_kategori_makanan.html')
