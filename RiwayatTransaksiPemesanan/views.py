from django.shortcuts import render

# Create your views here.
def Baca_RiwayatTransaksiPemesananPelanggan(request):
    # current_user = auth.get_user(request)

    
    # # if(not current_user.is_admin):
    # #     return redirect('authentication:login')

    context = {}
    return render(request, "Baca_RiwayatTransaksiPemesananP.html")

def Baca_RiwayatTransaksiPemesananRestoran(request):
    # current_user = auth.get_user(request)

    
    # # if(not current_user.is_admin):
    # #     return redirect('authentication:login')

    context = {}
    return render(request, "Baca_RiwayatTransaksiPemesananR.html")

def Baca_RiwayatTransaksiPemesananKurir(request):
    # current_user = auth.get_user(request)

    
    # # if(not current_user.is_admin):
    # #     return redirect('authentication:login')

    context = {}
    return render(request, "Baca_RiwayatTransaksiPemesananK.html")

def Form_Penilaian_Pemesanan(request):
    # current_user = auth.get_user(request)

    
    # # if(not current_user.is_admin):
    # #     return redirect('authentication:login')

    context = {}
    return render(request, "Form_Penilaian_Pemesanan.html", context)

def Detail_Pemesanan(request):
    # current_user = auth.get_user(request)

    
    # # if(not current_user.is_admin):
    # #     return redirect('authentication:login')

    context = {}
    return render(request, "Detail_Pemesanan.html")