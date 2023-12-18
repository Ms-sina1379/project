# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path, include
#
# from Eshop_beta import settings
# from Eshop_beta.views import home_page, footer, header
#
# urlpatterns = [
#
#                   path('', home_page),
#                   path('',include('Eshop_account.urls')),
#                   path('',include('Eshop_product.urls')),
#                   path('header/', header, name="header"),
#                   path('footer', footer, name="footer"),
#                   path('admin/', admin.site.urls),
#
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#
#
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Eshop_beta import settings
from Eshop_beta.views import home_page, footer, header

urlpatterns = [
    path('', home_page, name='home_page'),  # Add a unique name for the home page
    path('accounts/', include('Eshop_account.urls')),
    path('products/', include('Eshop_product.urls')),
    path('header/', header, name='header'),
    path('footer/', footer, name='footer'),
    path('admin/', admin.site.urls),
]

# Serving static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
