from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='restopay-index'),
    path('isi/', views.isi, name='restopay-isi'),
    path('tarik/', views.tarik, name='restopay-tarik'),
]
