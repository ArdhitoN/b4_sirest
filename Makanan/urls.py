from django.urls import path

from .views import *


app_name = 'Makanan'

urlpatterns = [
    path('lihat_makanan/', show_makanan, name='show_makanan'),


]