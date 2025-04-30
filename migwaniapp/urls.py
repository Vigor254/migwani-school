from django.contrib import admin
from django.template.context_processors import static
from django.urls import path
from migwaniapp import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('about/', views.about_overview, name='about'),
    path('about/sports/', views.about_sports, name='about_sports'),
    path('about/policies/', views.about_policies, name='about_policies'),
    path('about/facilities/', views.about_facilities, name='about_facilities'),
    path('about/performance/', views.about_Performance, name='about_Performance'),
    path('news/', views.news, name='news'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact')]
