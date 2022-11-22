from django.shortcuts import render

def show_kategori_makanan(request):
    return render(request, 'kategori_makanan.html')