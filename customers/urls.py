from django.urls import path
from .views import buy

app_name = 'customers'

urlpatterns = [
    path('', buy, name='buy')
]