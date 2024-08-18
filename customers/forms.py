from django import forms
from .models import Customers

class BuyForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['name', 'meter_number', 'amount_to_buy']