from django import forms
from captcha.fields import CaptchaField
from .models import *


class ReceptionForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'fullname', 'placeholder': 'Введите Ф.И.О. полностью'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Укажите электронный адрес'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'form-control', 'id': 'phone', 'placeholder': 'Введите номер Вашего телефона', 'pattern': '[+]{1}[0-9]{11,15}'}))
    question = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'question', 'placeholder': 'Введите свой вопрос', 'rows': 3}))
    captcha = CaptchaField()


class MessageForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'question',
                'placeholder': 'Суть проблемы или предложения',
                'rows': 3
    }))