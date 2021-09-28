from django.urls import path
from .views import *

app_name = "hoody"

urlpatterns = [
    path('', hoody_list, name='hoody_list'),
    path('<int:pk>/', hoody_detail, name='hoody_detail'),
    path('create/', hoody_create, name='hoody_create'),

]