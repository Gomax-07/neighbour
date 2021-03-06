from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from hoody.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("landing/", landing_page, name='landing_page'),
    path('hoody/', include('hoody.urls', namespace='hoody')),
    path("blog/", include("blog.urls", namespace='blog')),
    path("", include("users.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root='settings.STATIC_ROOT')
