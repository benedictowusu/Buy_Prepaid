from django.urls import path
from .views import view_queue, serve_buyer, login_view

app_name = "seller"
urlpatterns = [
    path('list/', view_queue, name='list'),
    path('serve/', serve_buyer, name='serve'),
    path('login/', login_view, name='login'),
]