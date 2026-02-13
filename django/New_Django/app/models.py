from django.db import models

# Create your models here.

class Student(models.Model):
    BRANCH_CHOICES = [
        ('CS', 'Computer Science'),
        ('ELEC', 'Electronics'),
        ('CIVIL', 'Civil Engineering'),    
    ]

    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)

    def __str__(self):
        return self.name