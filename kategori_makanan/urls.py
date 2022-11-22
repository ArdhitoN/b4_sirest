from django.urls import path
from .views import *

urlpatterns = [
    path('', show_kategori_makanan, name='show_kategori_makanan'),
]
