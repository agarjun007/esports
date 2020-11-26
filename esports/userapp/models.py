from django.db import models
from django.contrib.auth.models import User
from commerce.models import *
# Create your models here.

class Userprofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    profilepic = models.ImageField(null=True, blank=True)
    status = models.CharField(max_length=20,null=True, blank=True)

    @property
    def ImageURL(self):
        try:
            url = self.profilepic.url
        except:
            url = ''
        return url

class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20) 
    email = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField() 

class Order(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank =True)    
    address = models.ForeignKey(Address,on_delete=models.CASCADE,null = True,blank =True) 
    product = models.ForeignKey(products,on_delete=models.CASCADE,null = True,blank =True)
    quantity = models.IntegerField(null = True,blank =True)
    totalprice = models.IntegerField(null = True,blank =True)
    tid = models.CharField(max_length=200,null = True,blank =True)
    tdate = models.DateField(null = True,blank =True) 
    payment_status = models.CharField(max_length=50,null = True,blank =True)
    order_status = models.CharField(max_length=50,null = True,blank =True)
    payment_mode = models.CharField(max_length=50,null = True,blank =True)
   

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank =True)
    product = models.ForeignKey(products,on_delete=models.CASCADE,null = True,blank =True)
    quantity = models.IntegerField(null = True,blank =True)
    


 
 
