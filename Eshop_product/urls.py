from django.urls import path

from .views import Products,ProductsList

urlpatterns = [
    path('products/', Products),
    path('products-fuction/', ProductsList.as_view),
]