from django.contrib import admin
from django.contrib import admin
from .models import News, Staff, Student, Event, Gallery
# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('title', 'content')
    ordering = ('-date_posted',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'department')
    list_filter = ('department', 'role')
    search_fields = ('name', 'email', 'role')
    ordering = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'admission_number', 'form', 'stream', 'house')
    list_filter = ('form', 'stream', 'house')
    search_fields = ('full_name', 'admission_number', 'email')
    ordering = ('form', 'stream', 'full_name')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('date', 'location')
    search_fields = ('title', 'description')
    ordering = ('-date',)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_taken')
    list_filter = ('date_taken',)
    search_fields = ('title',)
    ordering = ('-date_taken',)