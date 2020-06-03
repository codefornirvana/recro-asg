from django import forms

class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(max_length=10)
    password = forms.CharField(max_length=32)
