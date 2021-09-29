from django.urls import path
from .views import *

app_name = "hoody"

urlpatterns = [
    path('', hoody_list, name='hoody_list'),
    path('<int:pk>/', hoody_detail, name='hoody_detail'),
    path('<int:pk>/update', hoody_update, name='hoody_update'),
    path('<int:pk>/delete', hoody_delete, name='hoody_delete'),
    path('create/', hoody_create, name='hoody_create'),

    # profile_paths

    path('profile_list/', profile_list, name='profile_list'),
    path('profile_create/', profile_create, name='profile_create'),
    path('<int:pk>/update', profile_update, name='profile_update'),
    path('<int:pk>/delete', profile_delete, name='profile_delete'),

    # business_paths
    path('business_list/', business_list, name='business_list'),

]
