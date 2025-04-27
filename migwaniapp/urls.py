from django.contrib import admin
from django.template.context_processors import static
from django.urls import path
from migwaniapp import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact')]
