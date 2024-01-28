from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.shortcuts import render, get_object_or_404
from django.http import Http404



def products(request):
    context = {"product": Product.objects.all()}
    return render(request, 'product/product_list.html', context)


class ProductsList(ListView):
    model = Product
    context_object_name = "products"
    # queryset = Product.objects.all()
    template_name = "product/product_list.html"
    paginate_by = 3

    def get_queryset(self):
         return Product.objects.all()
#
#
# def product_detail(request, *args, **kwargs):
#     product_title = kwargs['title']
#
#     try:
#         product = Product.objects.get(title=product_title)
#     except Product.DoesNotExist:
#         raise Http404('محصول مورد نظر یافت نشد')
#
#     if not product.active:
#         raise Http404('محصول مورد نظر یافت نشد')
#
#     context = {
#         'product': product
#     }
#
#     return render(request, 'product/product_detail.html', context)



def product_detail(request, *args, **kwargs):
    product_title = kwargs.get('title')
    product_id = kwargs.get('id')

    if product_id:
        product = get_object_or_404(Product, id=product_id)
    elif product_title:
        product = get_object_or_404(Product, title=product_title)
    else:
        raise Http404('محصول مورد نظر یافت نشد')

    if not product.active:
        raise Http404('محصول مورد نظر یافت نشد')

    context = {
        'product': product
    }

    return render(request, 'product/product_detail.html', context)
