from django.db import models

# Create your models here.
class products(models.Model):
    category = models.CharField(max_length=50)
    productname = models.CharField(max_length=20)
    productdesc = models.TextField(max_length=5000)
    price = models.IntegerField(max_length=10)
    Quantity = models.IntegerField(max_length=5)
    productimage = models.ImageField()
    