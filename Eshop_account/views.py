from django.shortcuts import render

def login(request):

    context= {}
    return render(request, 'account/login.html', context)
def Rejister(request):

    context={}

    return  render(request,'account/rejister.html',context)