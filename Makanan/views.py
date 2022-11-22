from django.shortcuts import render

from urllib import request

from django.shortcuts import redirect

from django.contrib import messages

from django.contrib import auth

from django.contrib.auth.decorators import login_required

import datetime

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse

from django.core import serializers

from django.utils.decorators import method_decorator


# Create your views here.
def show_makanan(request):
    current_user = auth.get_user(request)

    
    # if(not current_user.is_admin):
    #     return redirect('authentication:login')

    context = {}
    return render(request, "Makanan.html", context)