from django import forms
from django.forms import CharField


class LoginForms(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "لطفا نلم کاربری خود را وارد کنید "}),
        label="نام کاربری "
    )


    password: CharField = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا رمز خود را وارد کنید '}),
        label="کلمه عبور "

)
