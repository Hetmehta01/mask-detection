from django.urls import path
from .import views

urlpatterns = [
    path('', views.mainpage),
    path('mainpage', views.mainpage),
    path('camera', views.camera)
]