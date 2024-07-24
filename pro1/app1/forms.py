from django import forms
from django.contrib.auth.models import User

class UserCustomForm(forms.ModelForm):
    class Meta:
        model = User
        field = ['username','email','password']
        
    
        