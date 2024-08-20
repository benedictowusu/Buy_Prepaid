from django.urls import path
from .views import view_queue, serve_buyer, login_view

app_name = "seller"
urlpatterns = [
    path('list/', view_queue, name='list'),
    path('login/', login_view, name='login'),
    path('serve_buyer/<int:customer_id>/', serve_buyer, name='serve'),
]