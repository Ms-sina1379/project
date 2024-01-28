from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


def products(request):
    context = {"product": Product.objects.all()}
    return render(request, 'product/product_list.html', context)


class ProductsList(ListView):
    model = Product
    context_object_name = "products"
    # queryset = Product.objects.all()
    template_name = "product/product_list.html"
    # paginate_by = 3

    def get_queryset(self):
        return Product.objects.all()