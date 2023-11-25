# from django.shortcuts import render, redirect
# from .forms import LoginForms
# from django.contrib.auth import login,get_user_model, authenticate
#
#
# def login_user(request):
#     # if request.user.is_authenticated:
#     #     return redirect("/")
#     Login_Form = LoginForms(request.POST or None)
#     if Login_Form.is_valid():
#         user_name = Login_Form.cleaned_data.get("user_name")
#         password = Login_Form.cleaned_data.get("password")
#         user = authenticate(username=user_name, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("/")
#         else:
#             Login_Form.add_error('user_name', "کاربری با مشخصات زیر پیدا نشد ", )
#         # print(Login_Form.cleaned_data)
#     context = {
#
#         'login_form': Login_Form
#     }
#     return render(request, 'Eshop_account/login.html', context)
#
#
# def register(request):
#     if request.user.is_authenticated:
#         return redirect("/")
#
#     Register_form = registerform(request.POST or None)
#
#     if register_form.is_valid():
#         user_name = register_form.cleaned_data.get("user_name")
#         password = register_form.cleaned_data.get("password")
#         email = register_form.cleaned_data.get("email")
#         # Create a new user
#         User.objects.create_user(username=user_name, password=password, email=email)
#         return redirect("/login")
#
#     context = {'register_form': register_form}
#     return render(request, 'Eshop_account/register.html', context)


from django.shortcuts import render, redirect
from .forms import LoginForms, Registerforms
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def login_user(request):
    # if request.user.is_authenticated:
    #     return redirect("/")
    login_form = LoginForms(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get("user_name")
        password = login_form.cleaned_data.get("password")
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            login_form.add_error('user_name', "کاربری با مشخصات زیر پیدا نشد")
        # print(login_form.cleaned_data)
    context = {'login_form': login_form}
    return render(request, 'Eshop_account/login.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect("/")

    register_form = Registerforms(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get("user_name")
        password = register_form.cleaned_data.get("password")
        email = register_form.cleaned_data.get("email")
        # Create a new user
        User.objects.create_user(username=user_name, password=password, email=email)
        return redirect("/login")

    context = {'register_form': register_form}
    return render(request, 'Eshop_account/register.html', context)
