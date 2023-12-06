# forms.py

from django import forms


class DeliveryForm(forms.Form):
    km_location = forms.FloatField(label='Введите километр шоссе')
    medicine_name = forms.CharField(label='Введите название препарата')
