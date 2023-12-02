from django.urls import path

from .views import Product,Productlist
urlpatterns = [
    path('product-fuction',Product),
    path('product/',Productlist.as_view),
]