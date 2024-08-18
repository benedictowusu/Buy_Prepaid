from django.shortcuts import render
from .models import Customers

# Create your views here.
def buy(request):
    customers = Customers.objects.all()
    return render(request, 'buy.html')