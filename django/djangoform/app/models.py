from django.db import models

# Create your models here.

class UserDetails(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    postel= models.IntegerField()

    def __str__(self):
        return self.name
    
