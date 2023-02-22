from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket, name='basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
]