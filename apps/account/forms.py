from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UsernameField,
)
from .models import CustomerUser
from captcha.fields import ReCaptchaField
import re


class SignUpForm(UserCreationForm):
    captcha = ReCaptchaField(label="", )
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Nazwa użytkownika'}))
    email = forms.EmailField(label="", max_length=150, widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Ponownie wpisz hasło'}))

    class Meta:
        model = CustomerUser
        fields = ("username", "email", "address", "phone_number", "captcha")
        field_classes = {"username": UsernameField}

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tylko litery lub cyfry.")
        if len(username) < 8:
            raise forms.ValidationError("Nazwa użytkownika musi mieć 8 lub więcej znaków.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomerUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Taki email jest już zarejestrowany.')
        return email


class UpdateProfileForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "address", "phone_number", "photo", "captcha")

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not re.search(r'^\w+$', first_name):
            raise forms.ValidationError("Tylko litery lub cyfry.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not re.search(r'^\w+$', last_name):
            raise forms.ValidationError("Tylko litery lub cyfry.")
        return last_name

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].disabled = True


class ChangePasswordForm:
    pass
