from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class products(models.Model):
    category = models.CharField(max_length=50)
    productname = models.CharField(max_length=20)
    productdesc = models.TextField(max_length=5000)
    price = models.IntegerField()
    Quantity = models.IntegerField()
    productimage = models.ImageField(null=True, blank=True)

    @property
    def ImageURL(self):
        try:
            url = self.productimage.url
        except:
            url = ''
        return url
        

class userdetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=50,null=True)
    address = models.TextField(max_length=5000,null=True)
    pincode = models.IntegerField(null=True)
