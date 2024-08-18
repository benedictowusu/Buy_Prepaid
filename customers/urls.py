from django.urls import path
from .views import buy, view_queue, serve_buyer

app_name = 'customers'

urlpatterns = [
    path('', buy, name='buy'),
    path('list/', view_queue, name='requests'),
    path('serve/', serve_buyer, name='serve'),
]