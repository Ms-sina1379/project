

from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class ProductsList (ListView):

    template='Product/product_list.html'


def Products(request):
     Productsdetails= Product.objects.all()
     return render(request, "Product/product_list.html", {'Products':Productsdetails})


def get_queryset(self):
  return Products.objects.all()
