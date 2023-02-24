from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'town_or_city', 'street_address1', 'postcode', 'country', 'email', 'phone_number', 'county']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'postcode': 'Postal Code',
            'country': 'Country',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'county': 'County'
        }
        
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
