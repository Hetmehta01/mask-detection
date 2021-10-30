from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mask_detection_app.urls')),
    path('', include('django.contrib.auth.urls')),
]