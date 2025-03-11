from django import forms
from .models import Product
from django.contrib.auth.models import User
   
class ProductForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(attrs={'readonly':True}))
    class Meta:
        model = Product
        fields = ['user','item','price','date']
        