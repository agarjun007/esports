from django.shortcuts import render
from django.http import HttpResponse
from commerce.models import *


# Create your views here.

def gh(request):
    table = User.objects.all()
    product = products.objects.all()
    length_user =len(table)
    length_product =len(product)
    print(length_user,length_product)
    return HttpResponse('okkkk')