from django.urls import path
from . import views

urlpatterns = [
    path('<slug>/', views.product_detail, name='product_detail'),
    path('', views.home, name='home'),
    path('booked_tables', views.booked, name='booked_tables')
]