from django import forms
from django.forms import ModelForm
from .models import UserPayment


class UserPaymentForm(ModelForm):
    class Meta:
        model = UserPayment
        fields = ['card_number', 'expiration_date', 'cvv_2',
                  'username', 'phone_number', 'email']

        widgets = {
            'card_number': forms.TextInput(attrs={'class': 'all-length-input', 'placeholder': '**** **** **** ****', 'required': True}),
            'expiration_date': forms.TextInput(attrs={'class': 'left-length-input', 'placeholder': 'MM/YY', 'required': True}),
            'cvv_2': forms.TextInput(attrs={'class': 'right-length-input', 'placeholder': 'XXX', 'required': True}),
            'username': forms.TextInput(attrs={'class': 'all-length-input', 'required': True}),
            'phone_number': forms.TextInput(attrs={'class': 'left-length-input', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'right-length-input', 'placeholder': 'example@gmail.com', 'required': True}),
        }
