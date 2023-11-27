from django.urls import path

from .views import Product
urlpatterns = [
    path('products-fuction',Product),
    path('product/',ProducsList.as_viwe),
]