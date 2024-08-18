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

@login_required
def serve_buyer(request):
    buy = Customers.objects.order_by('request_time').first()
    if buy:
        buy.delete()
    return redirect('customers:serve')

@login_required
def view_queue(request):
    buyer = Customers.objects.order_by('request_time')
    return render(request, 'queue.html', {'buyer':buyer})