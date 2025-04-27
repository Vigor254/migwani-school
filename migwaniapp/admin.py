from django.contrib import admin
from .models import News, Staff, Student, Event, Gallery

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    search_fields = ('title', 'content')
    list_filter = ('date_posted',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'department')
    search_fields = ('name', 'role', 'department')
    list_filter = ('department',)
    ordering = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'admission_number', 'form', 'stream', 'house')
    search_fields = ('full_name', 'admission_number')
    list_filter = ('form', 'stream', 'house')
    ordering = ('form', 'stream', 'full_name')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    search_fields = ('title', 'description', 'location')
    list_filter = ('date',)
    date_hierarchy = 'date'

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_taken')
    search_fields = ('title',)
    list_filter = ('date_taken',)
    date_hierarchy = 'date_taken'