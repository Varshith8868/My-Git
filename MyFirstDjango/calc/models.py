from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=300, null=True)
    age=models.CharField(max_length=300, null=True)
    date=models.DateTimeField(max_length=300, null=True)
    
    def __str__(self):
        return self.name