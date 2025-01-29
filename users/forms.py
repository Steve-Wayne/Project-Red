from django.forms import ModelForm
from .models import User
from django import forms

class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class UserUpdateform(forms.ModelForm):
    model=User
    # warning meta should always writen as Meta as it designs the core structure of the form
    class Meta:
        model = User
        fields = [ 'username', 'email']

class UserDeleteForm(forms.ModelForm):
    model=User
    class Meta:
        model = User
        fields = []