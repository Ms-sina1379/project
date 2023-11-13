from django.shortcuts import render

def login(request):

    context= {}
    return render(request, 'Eshop_account/login.html', context)
def Rejister(request):

    context={}

    return  render(request,'Eshop_account/rejister.html',context)