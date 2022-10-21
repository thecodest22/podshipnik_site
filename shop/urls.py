from django.urls import path, include
from . import views


app_name = 'shop'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('about/', views.about_us, name='about'),
]
