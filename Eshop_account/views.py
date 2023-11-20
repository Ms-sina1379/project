from django.contrib.auth import login,get_user_model,authenticate
from django.shortcuts import render
from .forms import LoginForms
def login_User(request):
    Login_Form=LoginForms(request.POST or None)
    if Login_Form.is_valid():
        user_name=Login_Form.cleaned_data.get("user_name" )
        password=Login_Form.cleaned_data.get("  password" )
        User=authenticate(username="user_name",password="password")
        print(Login_Form.cleaned_data)
    context= {

    'login_form':Login_Form
    }
    return render(request, 'Eshop_account/login.html', context)
def register(request):

    context={}

    return  render(request,'Eshop_account/register.html',context)


