from django.db import models
from django.contrib.auth.models import User
from commerce.models import *
# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(products,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    quantity = models.IntegerField()


class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20) 
    email = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField(max_length=20)

class Order(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE) 
    price = models.IntegerField(max_length=20)
    tid = models.CharField(max_length=200)
    tdate = models.DateField()   
 
