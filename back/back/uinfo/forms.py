from .models import *
from back.wtenant.models import *
from django import forms
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm




class UserInfoForm(ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    surname = forms.CharField(label='Surname', widget=forms.TextInput(attrs={'class': 'form-input'}))
    passport = forms.CharField(label='Passport', widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone_number = forms.CharField(label='Phone number', widget=forms.TextInput(attrs={'class': 'form-input'}))
    #user_id=forms.CharField(initial=request.user)

    class Meta:
        model = TenantUser
        fields = ['name', 'surname', 'passport', 'phone_number']


class AppointmentForm(ModelForm):
    time = forms.DateTimeField(label='time')

    class Meta:
        model = Appointment
        fields = ['medicalcard_id', 'time', 'doctor_id']


class RegisterUserForm(UserCreationForm):

    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = TenantUser

        fields = ( 'email', 'password1', 'password2', 'name')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


