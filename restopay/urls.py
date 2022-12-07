from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='restopay-index'),
    path('isi/', views.isi, name='restopay-isi'),
    path('tarik/', views.tarik, name='restopay-tarik'),
    path('all/', views.all_restopay, name='restopay-all'),
    path('tarik-request/', views.tarik_op, name='restopay-tarik-op'),
    path('isi-request/', views.isi_op, name='restopay-isi-op'),
]
