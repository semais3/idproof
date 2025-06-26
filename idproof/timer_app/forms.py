# timer_app/forms.py

from django import forms
from captcha.fields import CaptchaField

class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите ваше имя'}),
        label="Ваше имя"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Введите ваш email'}),
        label="Email"
    )
    captcha = CaptchaField(label="Капча")
    privacy_policy = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'privacy-checkbox'}),
        label="Я согласен с политикой конфиденциальности"
    )
