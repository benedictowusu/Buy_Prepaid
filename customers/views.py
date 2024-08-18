from django.shortcuts import render, redirect
from .forms import BuyForm
from .models import Customers
from django.contrib.auth.decorators import login_required

# Create your views here.
def buy(request):
    if request.method == "POST":
        customers = BuyForm(request.POST)
        if customers.is_valid():
            customers.save()
            return redirect('customers:buy')
    else:
        customers = BuyForm()
    return render(request, 'buy.html', {"customers": customers})