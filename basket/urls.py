from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
]
