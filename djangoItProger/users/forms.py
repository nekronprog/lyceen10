from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField(
    label='Введите email',
    required=True,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'})
  )
  username = forms.CharField(
    label='Введите login', 
    required=True, 
    help_text='Нельзя вводить символы: @, /, _',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите login'})
  )
  password1 = forms.CharField(
    label='Введите пароль', 
    required=True, 
    help_text='Пароль не должен быть малинким и простым',
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
  )
  password2 = forms.CharField(
    label='Подтвердите пароль', 
    required=True, 
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
  )

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField(
    label='Введите email',
    required=False,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'})
  )
  username = forms.CharField(
    label='Введите login', 
    required=False, 
    help_text='Нельзя вводить символы: @, /, _',
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите login'})
  )

  class Meta:
    model = User
    fields = ['username', 'email']

class ProfileImageForn(forms.ModelForm):
  img = forms.ImageField(
    label='Загрузить фото',
    required=False,
    widget=forms.FileInput
  )
  class Meta:
    model = Profile
    fields = ['img']