from django.db import models
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    user = models.CharField(max_length=50)
    item = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateField(default=timezone.now)


    def __str__(self):
        return self.user