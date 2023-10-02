
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import Home_page

from Eshop_beta import settings

urlpatterns = [
    path('', Home_page),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
