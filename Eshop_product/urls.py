
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import product_detail, ProductsList

urlpatterns = [
    path('products-class/', ProductsList.as_view(), name='products-class'),
    path('products/<int:id>/<str:title>', product_detail, name='product_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
