from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from store.models import Customer


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['number_phone', 'email']






