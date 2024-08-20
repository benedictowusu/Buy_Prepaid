from django.shortcuts import get_object_or_404, render,redirect
from customers.models import Customers
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        loginform = AuthenticationForm(data=request.POST)
        if loginform.is_valid():
            user = loginform.get_user()
            login(request, user)
            return redirect('seller:list')
    else:
        loginform = AuthenticationForm()
    return render(request, 'login.html', {'loginform': loginform})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('seller:login')

def add_customer(request):
    if request.method == 'POST':
        addcustomer = CustomerForm(request.POST)
        if addcustomer.is_valid():
            addcustomer.save()
            return redirect('view_queue')
    else:
        addcustomer = CustomerForm()
    return render(request, 'queue.html', {'addcustomer': addcustomer})

@login_required
def serve_buyer(request, customer_id):
    # Fetch the customer object by ID or return a 404 error if not found
    customer = get_object_or_404(Customers, id=customer_id)
    # Delete the customer object from the database when served
    customer.delete()
    return redirect('seller:list')

@login_required
def view_queue(request):
    # Get all customer objects ordered by the request time
    buyer = Customers.objects.order_by('request_time')
    return render(request, 'queue.html', {'buyer': buyer})