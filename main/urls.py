from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('capturePage/', views.capturePage, name="capturePage"),
    path('uploadPage/', views.uploadPage, name="uploadPage"),
    path('translated/', views.translated, name="translated"),
]

