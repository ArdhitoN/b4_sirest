from django.urls import path
from . import views

urlpatterns = [
    path('buat/', views.jam_buat, name='restopay-index'),
]