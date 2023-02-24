from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'town_or_city', 'street_address1', 'postcode', 'country', 'email', 'phone_number', 'county']
