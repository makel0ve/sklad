from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('update/', views.productupdate, name='productupdate'),
]