from django.forms import ModelForm
from Rent.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CarForm(ModelForm):
    
    class Meta:
        model = Car
        fields = ['brand','model', 'color', 'patent', 'picture',]
        
class EditCar(ModelForm):

    class Meta:
        model = Car
        fields = ['model', 'color', 'patent', 'picture',]
        
class ExecutiveForm(ModelForm):
    
    class Meta:
        model = Executive
        fields = ['name', 'birthday', 'age', 'email','picture','rut','dv']

class EditExecutive(ModelForm):
    
    class Meta:
        model = Executive
        fields = ['name', 'birthday', 'age', 'email','picture','rut','dv']

class ClientForm(ModelForm):
    
    class Meta:
        model = Client
        fields = ['name', 'birthday', 'age', 'email','rut','dv']

class EditClient(ModelForm):
    
    class Meta:
        model = Client
        fields = ['name', 'birthday', 'age', 'email','rut','dv']
        
class RentForm(ModelForm):
    
    class Meta:
        model = Rent
        fields = ['client','status','start_date','end_date']
        
class UserForm(ModelForm):
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','password1', 'password2', )