from django.urls import path
from . import views

urlpatterns = [
    path('', views.p_berlangsung, name='rpesanan-index'),
    path('detail/', views.p_detail, name='rpesanan-detail'),
]