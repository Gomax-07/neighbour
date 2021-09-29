from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('accounts/', include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
]
