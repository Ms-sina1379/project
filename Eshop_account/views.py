from django.shortcuts import render

def login_User(request):
    Login_Form=loginForm(request.post or None)
    context= {

    'login_form':login_form
    }
    return render(request, 'Eshop_account/login.html', context)
def register(request):

    context={}

    return  render(request,'Eshop_account/register.html',context)


