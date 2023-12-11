from django.shortcuts import render
from django.views.generic import ListView
from.models import Product
# Create your views here.

def Products(request):
    Products= Product.objects.all()
    return render(request, "product/product_list.html", {'products':Product})

class ProductsList (ListView):

    template='product/product_list.html'

    def get_queryset(self):
        return Products.objects.all()

