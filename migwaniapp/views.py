from django.shortcuts import render
from .models import News, Staff, Event, Gallery, Partner
# Create your views here.
from django.shortcuts import render
from .models import News, Staff, Event, Gallery


def home(request):
    latest_news = News.objects.order_by('-date_posted')[:3]
    upcoming_events = Event.objects.order_by('date')[:3]
    aluminum_partner = Partner.objects.filter(name="Migwani Aluminum").first()

    # Add carousel images data
    carousel_images = [
        {
            'image': 'images/migwani.jpg',  # Path relative to static folder
            'alt': 'Migwani School Front View',
            'title': 'Welcome to Migwani Boys',
            'description': 'Quality Education forever'
        },
        # Add more images if needed
        {
            'image': 'images/school-building.jpg',
            'alt': 'School Building',
            'title': 'Migwani School with',
            'description': 'Modern Learning Facilities'
        }
    ]


    context = {
        'news': latest_news,
        'events': upcoming_events,
        'carousel_images': carousel_images,
        'aluminum_partner': aluminum_partner,
        'aluminum_quote': {
            'text': "Migwani Aluminum - Building Kenya's Future, One Quality Product at a Time",
            'author': "CEO, Migwani Aluminum Works",
            'year': "Since 2010"
        }
    }
    return render(request, 'school/index.html', context)
# def home(request):
#     latest_news = News.objects.order_by('-date_posted')[:3]
#     upcoming_events = Event.objects.order_by('date')[:3]
#     context = {
#         'news': latest_news,
#         'events': upcoming_events,
#     }
#     return render(request, 'school/index.html', context)
def about_sports(request):
    return render(request, 'school/about/sports.html')

def about_policies(request):
    return render(request, 'school/about/policies.html')

def about_facilities(request):
    return render(request, 'school/about/facilities.html')

def about_Performance(request):
    return render(request, 'school/about/performance.html')

def about_overview(request):
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