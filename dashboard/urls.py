from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('pelanggan/', dash_pelanggan, name='dash-pelanggan'),
    path('restoran/', dash_resto, name='dash-resto'),
]