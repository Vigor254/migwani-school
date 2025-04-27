from django.shortcuts import render
from .models import News, Staff, Event, Gallery
# Create your views here.
def home(request):
    latest_news = News.objects.order_by('-date_posted')[:3]
    upcoming_events = Event.objects.order_by('date')[:3]
    context = {
        'news': latest_news,
        'events': upcoming_events,
    }
    return render(request, 'school/index.html', context)

def about(request):
    staff = Staff.objects.all()
    return render(request, 'school/about.html', {'staff': staff})

def news(request):
    all_news = News.objects.order_by('-date_posted')
    return render(request, 'school/news.html', {'all_news': all_news})

def gallery(request):
    photos = Gallery.objects.all()
    return render(request, 'school/gallery.html', {'photos': photos})

def contact(request):
    return render(request, 'school/contact.html')