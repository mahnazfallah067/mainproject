from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    family = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام و نام خانوادگی را وارد نمایید', 'class': 'form-control'}),
        label=' نام و نام خانوادگی',
        validators=[validators.MaxLengthValidator(120, 'نام و نام خانوادگی نمی تواند بیشتر از 150 کاراکتر باشد')]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل  را وارد نمایید', 'class': 'form-control'}),
        label='ایمیل ',
        validators=[validators.MaxLengthValidator(100, 'ایمیل شما نمی تواند بیشتر از 100 کاراکتر یاشد')]
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'لطفا متن پیام  را وارد نمایید', 'class': 'form-control'}),
        label='متن پیام '
    )

    number = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'لطفا شماره تلفن خود  را وارد نمایید', 'class': 'form-control'}),
        label=' شماره تلفن '
    )

