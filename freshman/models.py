from django.db import models

# Create your models here.
class Visit(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    photo = models.ImageField(upload_to='img/visit_photos/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=[
        ('academic', 'Academic'),
        ('social', 'Social Spot'),
        ('food', 'Food Place'),
        ('admin', 'Admin Office'),
        ('other', 'Other'),
    ])
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
