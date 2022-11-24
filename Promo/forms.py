from django import forms
from django.forms import widgets
from .models import *

class Form__PromoMT(forms.ModelForm) :
    class Meta :
        model = Model_Promo2
        fields = ('Nama', 'Jenis_promo','Diskon','Minimum_transaksi')
        widgets= {
            'Nama': forms.TextInput(attrs={'class':'form-control'}),
            'Jenis_promo': forms.HiddenInput(),
            'Diskon': forms.NumberInput(attrs={'class':'form-control'}),
            'Minimum_transaksi': forms.NumberInput(attrs={'class':'form-control'}),
            
        }
class MyDateInput(forms.widgets.DateInput):
    input_type = 'date'
class Form__PromoHS(forms.ModelForm) :
    class Meta :
        model = Model_Promo2
        fields = ('Nama','Jenis_promo','Diskon','Tanggal_berlangsung')
        widgets= {
            'Nama': forms.TextInput(attrs={'class':'form-control'}),
            'Jenis_promo': forms.HiddenInput(),
            'Diskon': forms.NumberInput(attrs={'class':'form-control'}),
            'Tanggal_berlangsung': forms.DateInput(attrs={'type': 'date'}),
            
        }