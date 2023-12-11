from django.shortcuts import render
from django.views.generic import ListView
from.models import Product
# Create your views here.

def Products(request):
    Productsdetails= Product.objects.all()
    return render(request, "product/product_list.html", {'products':Productsdetails})

class ProductsList (ListView):

    template='product/product_list.html'

    def get_queryset(self):
        return Products.objects.all()

