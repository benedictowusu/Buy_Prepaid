from django.shortcuts import render,redirect
from customers.models import Customers
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        loginform = AuthenticationForm(data=request.POST)
        if loginform.is_valid():
            #login by retrieving user
            user = loginform.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('seller:list')
    else:
        loginform = AuthenticationForm()
    return render(request, 'login.html', {'loginform': loginform})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('seller:login')

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