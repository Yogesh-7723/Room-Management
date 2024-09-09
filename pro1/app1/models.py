from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

DEPARTMENT_TYPES = (
    ('Bill','BILL MANAGER'),
    ('Rent','RENT MANAGER'),
    ('Clean','CLEANING MANAGER'),
    ('Grocery','GROCERY MANAGER')
)
# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,max_length=50,related_name='member')
    item = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateField(default=timezone.now)


    def __str__(self):
        return self.item

class Profile(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE,max_length=50)
    education = models.CharField(max_length=50,null=True)
    dept = models.CharField(choices=DEPARTMENT_TYPES,max_length=7,default='Member')
    gender = models.CharField(max_length=10,default=None)
    address = models.TextField(default=None)
    contact = models.IntegerField(default=None)
    profile = models.ImageField(upload_to='profile/',blank=True)


