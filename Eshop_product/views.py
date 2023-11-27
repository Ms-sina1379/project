from django.shortcuts import render

# Create your views here.

def products(request):
    context = {}
    return render(request, "product/product_list.html", context)