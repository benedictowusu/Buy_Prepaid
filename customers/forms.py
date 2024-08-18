from django.forms import ModelForm
from .models import Customers

class BuyForm(ModelForm):
    class Meta:
        model = Customers
        