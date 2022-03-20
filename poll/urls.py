from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('events/', views.events_view, name="events"),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name="event"),
    path('gallery/', views.GalleryView.as_view(), name="gallery"),
    path('contact/', views.ContactView.as_view(), name="contact"),
]
