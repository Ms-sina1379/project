from django.urls import path

from .views import login,Rejister

urlpatterns = [
    path('login/',login),
    path('rejister/',Rejister),
]
