from django import forms

class AddressForm(forms.Form):
    address = forms.CharField(label='address', max_length=100)