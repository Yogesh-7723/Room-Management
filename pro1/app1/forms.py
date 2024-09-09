from django import forms
from .models import Product
from django.contrib.auth.models import User
   
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['user','item','price','date']
        