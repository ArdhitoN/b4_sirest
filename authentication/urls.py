from django.urls import path

from .views import *

app_name = 'authentication'

urlpatterns = [
    path("register-admin/", show_register_admin, name="show_register_admin"),
    path("register-pelanggan/", show_register_pelanggan, name="show_register_pelanggan"),
]