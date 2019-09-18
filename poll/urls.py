from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('products/', views.product_view, name="products"),
    path('contact/', views.ContactView.as_view(), name="contact"),
]
