from django.db import models

# Create your models here.

CATEGORY_CHOICE = (
    ('M','member only'),
    ('PM','PaymentManage'),
    ('BM','BillManage'),
    ('RM','RentManage'),
    ('FM','FoodManage'),
    ('WM','WorkManage')
)

class User(models.Model):
    u_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    post = models.CharField(choices=CATEGORY_CHOICE,max_length=2)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    pro_img = models.ImageField(upload_to='profile',blank=True)
    
    def __str__(self):
        return self.u_name 
    
class Purches(models.Model):
    ref_user = models.ForeignKey(User , on_delete=models.CASCADE)
    pro_name = models.CharField(max_length=100)
    pro_price = models.PositiveIntegerField()
    buy_date = models.DateField()
    
    def __str__(self):
        return self.pro_name
    

MEMORY_CHOICE = (
    ('G','GROUP'),
    ('S','MYSELF')
)
class Memory(models.Model):
    title = models.CharField(choices=MEMORY_CHOICE,max_length=1)
    image = models.ImageField(upload_to='memory',blank=True)
    discribe = models.TextField()
    upload_by = models.ForeignKey(User,on_delete=models.CASCADE)
    upload_date = models.DateTimeField()
    
    def __str__(self):
        return self.discribe
    
    