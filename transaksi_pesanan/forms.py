from django import forms

province_list = (
    ("Value1", "Provinsi1"),
    ("Value2", "Provinsi2"),
)

class FormAlamat(forms.Form):
    street = forms.CharField(max_length=30)
    district = forms.CharField(max_length=30)
    city = forms.CharField(max_length=25)
    province = forms.ChoiceField(choices= province_list,widget = forms.Select())