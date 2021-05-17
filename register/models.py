from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.CharField(max_length=200,unique=True,blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=200,blank=True,null=True)
    state = models.CharField(max_length=200,blank=True,null=True)
    country = models.CharField(max_length=200,blank=True,null=True)
    pincode =  models.CharField(max_length=10,blank=True,null=True)
    phone = models.CharField(max_length=10,blank=True,null=True)
    def __str__(self):
        return str(self.id)
