from django import forms

from .models import Order

class OrderForm(forms.ModelForm):

	first_name = forms.CharField()
	last_name = forms.CharField()
	street_address = forms.CharField()
	phone_number = forms.CharField()
