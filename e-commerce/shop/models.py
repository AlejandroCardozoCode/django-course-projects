from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200) 
    description = models.TextField() 
    price = models.FloatField()
    category = models.CharField(max_length=200) 
    image = models.CharField(max_length=300) 

    def __str__(self) -> str:
        return self.name 