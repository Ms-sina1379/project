from django.shortcuts import render

def login(request):

    context= {}
    return render(request, 'Eshop_account/login.html', context)
def register(request):

    context={}

    return  render(request,'Eshop_account/register.html',context)


