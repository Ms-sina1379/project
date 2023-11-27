from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

def product(request):
    context = {}
    return render(request, "product/product_list.html", context)


class product_list(ListView):
    template='product/product_list.html'


def get_queryset(self):
        return product.objects.all()


