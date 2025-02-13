from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about, name='about'),
    path('certifications/', views.certifications),
    path('projects/', views.projects),
]
