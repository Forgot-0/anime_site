from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms




class CustomUserCreationsForm(UserCreationForm):
    
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    username = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'})
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        exclude = []
        fields = ('username', 'email')


class CusetomUserForm(forms.ModelForm):
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    phone = forms.CharField(required=False, label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'phone'}))
    avatarka = forms.ImageField(required=False, label='Автар', widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'avatarka'}))

    class Meta:
        model = CustomUser
        exclude = ['password']
        fields = ('email', 'phone', 'avatarka')

