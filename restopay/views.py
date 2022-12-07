from django.shortcuts import render, redirect
from .models import TransactionActorRepository
# Create your views here.

def index(request, fail_tarik = False):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    email = request.session.get('user_email')
    tar = TransactionActorRepository()
    actor = tar.getByEmail(email)

    return render(request, 'restopay_index.html', {"actor": actor, "fail_tarik": fail_tarik})

def isi(request):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    email = request.session.get('user_email')
    tar = TransactionActorRepository()
    actor = tar.getByEmail(email)
    return render(request, 'restopay_isi.html', {"actor": actor})

def tarik(request):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    email = request.session.get('user_email')
    tar = TransactionActorRepository()
    actor = tar.getByEmail(email)
    return render(request, 'restopay_tarik.html', {"actor": actor})

def all_restopay(request):
    tar = TransactionActorRepository()
    actors = tar.getAll()
    return render(request, 'test_db_ta.html', {"actors": actors})

def tarik_op(request):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    email = request.session.get('user_email')
    if request.method == "POST":

        jumlahTarik = int(request.POST["nominalPenarikan"])
        tar = TransactionActorRepository()
        success = tar.reduceByEmail(email, jumlahTarik)

        if success:
            return redirect('/restopay/')
        else:
            return index(request, fail_tarik=True)

def isi_op(request):
    if 'user_email' not in request.session:
        return redirect('/authentication/login')
    email = request.session.get('user_email')
    if request.method == "POST":

        jumlahIsi = int(request.POST["nominalPengisian"])
        tar = TransactionActorRepository()
        tar.isiByEmail(email, jumlahIsi)

        return redirect('/restopay/')