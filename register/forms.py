from django.core import validators
from django import forms
from .models import User

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','address','city','state','country','pincode','email']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'pincode':forms.TextInput(attrs={'class':'form-control'}),
        }