from django.shortcuts import render, redirect
from .forms import LoginForms
from django.contrib.auth import login,get_user_model, authenticate


def login_user(request):
    if request.user.is_authenticated:
        return redirect("/")
    Login_Form = LoginForms(request.POST or None)
    if Login_Form.is_valid():
        user_name = Login_Form.cleaned_data.get("user_name")
        password = Login_Form.cleaned_data.get("password")
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            redirect("/")
        else:
            Login_Form.add_error('user_name', "کاربری با مشخصات زیر پیدا نشد ", )
        # print(Login_Form.cleaned_data)
    context = {

        'login_form': Login_Form
    }
    return render(request, 'Eshop_account/login.html', context)


def register(request):
    context = {}

    return render(request, 'Eshop_account/register.html', context)
