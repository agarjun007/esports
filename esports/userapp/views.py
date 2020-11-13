from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse 
from commerce.models import *


# Create your views here.

   
def usersignup(request):
    if request.user.is_authenticated:
        return redirect(userhome)
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        mobile = request.POST['mobile']
       
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return JsonResponse('usernamemismatch',safe=False)
                
                # return redirect('/signin')
            else: 
                user = User.objects.create_user(first_name=name,username=username,email=email,password = password1,last_name = mobile)
                user.save();
            messages.info(request, "User created successfully..")  
            # return redirect(usersignin)  
            return JsonResponse('valid', safe=False)       
        else:
            return JsonResponse('invalid', safe=False)
            messages.info(request,"password not match")
            # return redirect('/signin')

    else:    
        return render(request,'userapp/signup.html')   

def usersignin(request):
    if request.user.is_authenticated:
        return redirect(userhome)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username , password=password)

        if user is not None:
            auth.login(request,user)
            return JsonResponse('valid', safe=False)
        else:
            return JsonResponse('invalid', safe=False)
    else:
        return render(request,'userapp/user_signin.html')
   

def userhome(request):   
    if request.user.is_authenticated:
        product = products.objects.all()
        category = Category.objects.all()
        return render(request,'userapp/user_home.html',{'product_data':product,'category_data':category})
    else:
        return redirect(usersignin)  

def category(request,id):
    product= products.objects.filter(category=id)    
    category = Category.objects.all()
    if request.user.is_authenticated:
        return render(request,'userapp/user_home.html',{'product_data':product,'category_data':category})
    else:    
        return render(request,'userapp/guest_home.html',{'product_data':product,'category_data':category})          

def guesthome(request):
    if request.user.is_authenticated:
        return redirect(userhome)
    product = products.objects.all()
    category = Category.objects.all()
    return render(request,'userapp/guest_home.html',{'product_data':product,'category_data':category})
           
def productview(request,id):
    category = Category.objects.all()
    product = products.objects.get(id=id)
    return render(request,'userapp/user_product_view.html',{'product_data':product,'category_data':category})
    
def usercart(request,id):
    product = products.objects.filter(id=id)
    user = User.objects.get()
    
    return render(request,'userapp/user_cart.html') 


def userpayment(request):
    
    return render(request,'userapp/user_payment.html')     

def userlogout(request):
     if request.user.is_authenticated:
        auth.logout(request)
        return redirect(usersignin)             


   