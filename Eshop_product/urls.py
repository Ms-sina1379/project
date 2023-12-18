
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Products, ProductsList

urlpatterns = [
    path('products/', Products),
    path('products-class/', ProductsList.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
