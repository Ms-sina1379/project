from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

def Products(request):
    context = {}
    return render(request, "product/product_list.html", context)


class ProductsList (ListView):

    template='product/product_list.html'

    def get_queryset(self):
        return Products.object.all()




