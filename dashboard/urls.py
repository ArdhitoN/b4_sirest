from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('pelanggan/', dash_pelanggan, name='dash-pelanggan'),
    path('pelanggan-v/', dash_pelanggan_verified, name='dash-pelanggan-v'),
    path('restoran/', dash_resto, name='dash-resto'),
]