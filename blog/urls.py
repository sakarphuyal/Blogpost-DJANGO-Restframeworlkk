from django.urls import path
from django.views.generic import TemplateView\
    
from . import views

app_name="blog"

urlpatterns = [
    path('', views.home, name="home"),
    path('single/<slug:slug>', views.single, name="single"),
    path('about_us', views.aboutus, name="aboutus"),
]
