from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    category = models.CharField(max_length=50, choices=[
        ('Festival', 'Festival'),
        ('dance', 'Dance'),
        ('food', 'Food Place'),
        ('Night Event', 'Night Event'),
        ('other', 'Other'),
    ])
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='img/clubs/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=[
        ('Web', 'Web'),
        ('social', 'Social Spot'),
        ('food', 'Food Place'),
        ('Movie', 'Movie'),
        ('other', 'Other'),
    ])
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title