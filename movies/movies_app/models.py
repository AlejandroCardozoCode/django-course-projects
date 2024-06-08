from django.db import models

# Create your models here.
class MovieData(models.Model):
    name = models.CharField(max_length = 200)
    duration_seconds = models.FloatField()
    rating = models.FloatField()
    genre = models.CharField(max_length = 200, default='action')
    image = models.ImageField(upload_to='images/movies_images/', default='images/movies_images/default.jpg')

    def __str__(self):
        return self.name
    
    