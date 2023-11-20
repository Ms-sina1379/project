from django.urls import path

from .views import login_User,register

urlpatterns = [
    path('login/',login_User),
    path('Register/',register),
]
