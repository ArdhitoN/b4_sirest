from django import forms
from tarifPengiriman.models import *

tarif_repo = TarifPengirimanRepository()
list_tarif_pengiriman = tarif_repo.getAllTarifPengiriman()

province_list = (
    (tarif_pengiriman.id, tarif_pengiriman.province) for tarif_pengiriman in list_tarif_pengiriman 
)

class FormAlamat(forms.Form):
    street = forms.CharField(max_length=30)
    district = forms.CharField(max_length=30)
    city = forms.CharField(max_length=25)
    province = forms.ChoiceField(choices= province_list, widget = forms.Select())