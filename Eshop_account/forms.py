# from django import forms
# from django.contrib.auth.models import User
# from django.forms import CharField
#
#
# class LoginForms(forms.Form):
#     user_name = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': "لطفا نلم کاربری خود را وارد کنید "}),
#         label="نام کاربری "
#     )
#
#
#     password: CharField = forms.CharField(
#         widget=forms.PasswordInput(attrs={'placeholder': 'لطفا رمز خود را وارد کنید '}),
#         label="کلمه عبور "
#
# )
#     def clean_user_name(self):
#         user_name=self.cleaned_data.get("user_name")
#         is_existe_user= User.objects.filter(username=user_name).exists()
#         if not is_existe_user:
#             raise forms.ValidationError("کاربر با مشخصات زیر ثبت نام نکرده است ")
#         return user_name
#
#
# class Registerforms(forms.Form):
#     user_name = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': "لطفا نلم کاربری خود را وارد کنید "}),
#         label="نام کاربری "
#         )
#
#     email= forms.CharField(
#         widget=forms.EmailField(attrs={'placeholder': "لطفا ایمیل خود را وارد کنید "}),
#         label="ایمیل"
#         )
#
#     password: CharField = forms.CharField(
#         widget=forms.PasswordInput(attrs={'placeholder': 'لطفا رمز خود را وارد کنید '}),
#         label="کلمه عبور "
#
#         )
#    re_password: CharField = forms.CharField(
#         widget=forms.PasswordInput(attrs={'placeholder': 'لطفا رمز خود را وارد کنید '}),
#         label="کلمه عبور "
#
#     )
#
#
# def clean_pssword (self):
#      = self.cleaned_data.get("user_name")
#     is_existe_user = User.objects.filter(username=user_name).exists()
#     if not is_existe_user:
#         raise forms.ValidationError("کاربر با مشخصات زیر ثبت نام نکرده است ")
#     return user_name



from django import forms
from django.contrib.auth.models import User
from django.forms import CharField

class LoginForms(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "لطفا نام کاربری خود را وارد کنید "}),
        label="نام کاربری "
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا رمز خود را وارد کنید '}),
        label="کلمه عبور "
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        is_existe_user = User.objects.filter(username=user_name).exists()
        if not is_existe_user:
            raise forms.ValidationError("کاربر با مشخصات زیر ثبت نام نکرده است ")
        return user_name

class Registerforms(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "لطفا نام کاربری خود را وارد کنید "}),
        label="نام کاربری "
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': "لطفا ایمیل خود را وارد کنید "}),
        label="ایمیل"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا رمز خود را وارد کنید '}),
        label="کلمه عبور "
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا تکرار رمز خود را وارد کنید '}),
        label="تکرار کلمه عبور "
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        is_existe_user = User.objects.filter(username=user_name).exists()
        if not is_existe_user:
            raise forms.ValidationError("کاربر با مشخصات زیر ثبت نام نکرده است ")
        return user_name



    def clean_email(self):
        email=self.cleaned_data.get("email")
        is_exists_user_by_email=User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError("کاربر وارد شده تکراری است  ")

        if len(email)>20:
            raise forms.ValidationError("تعداد کاراکتر های ایمیل باید کمتر باشد ")
        return email



    def clean_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if password and re_password and password != re_password:
            raise forms.ValidationError("کلمه عبور و تکرار آن باید یکسان باشند")
        return password
