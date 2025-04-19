from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/')

    def __str__(self):
        return self.title


class Staff(models.Model):
    DEPARTMENT_CHOICES = [
        ('SCIENCE', 'Science'),
        ('HUMANITIES', 'Humanities'),
        ('TECHNICAL', 'Technical'),
        ('ADMIN', 'Administration'),
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='staff_photos/', blank=True)

    def __str__(self):
        return f"{self.name} ({self.role})"


class Student(models.Model):
    admission_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    form = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    stream = models.CharField(max_length=1)  # A, B, C, etc.
    house = models.CharField(max_length=50)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.full_name} (Form {self.form}{self.stream})"


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='event_posters/', blank=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    date_taken = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title