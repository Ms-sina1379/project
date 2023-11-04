from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Eshop_beta import settings
from .views import home_page, footer, header

urlpatterns = [

                  path('', home_page),
                  path('login/',include('Eshop_account.urls')),
                  path('header/', header, name="header"),
                  path('footer', footer, name="footer"),
                  path('admin/', admin.site.urls),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


