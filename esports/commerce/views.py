from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import products
from django.http import JsonResponse
from django.http import HttpResponse 

from django.core.files.storage import FileSystemStorage
from PIL import Image
from django.core.files import File

# Create your views here.
def adminlogin(request):
    if request.session.has_key('password'):
        return redirect(adminpanel)
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        if username == 'admin' and password == 'admin':
            request.session['password'] = password
            table = User.objects.all()
            return JsonResponse('valid', safe=False)
        
            # return render(request,'admin_panel.html',{'table_data':table})
        else: 
            return JsonResponse('invalid', safe=False)   
            # return redirect('/admin_login')
    else:    
            return render(request,'admin_login.html')        

def adminpanel(request):
    if request.session.has_key('password'):
        table = User.objects.all()
        return render(request,'admin_panel.html',{'table_data':table})
    else:
        return redirect(adminlogin)

def adminpanel_products(request):
    if request.session.has_key('password'):
        table = products.objects.all()
        return render(request,'adminpanel_products.html',{'table_data': table})
    else:
        return redirect(adminlogin)        

def createproducts(request):
    if request.session.has_key('password'):
         if request.method == 'POST':
        
            category = request.POST['category']
            productname = request.POST['productname']
            productdesc = request.POST['productdesc']
            price = request.POST['price']
            quantity = request.POST['quantity']
            productimage = request.FILES.get('productimage')
            product = products.objects.create(category=category,productname=productname,productdesc=productdesc,price=price,Quantity= quantity,productimage=productimage)
            product.save();
            messages.info(request, "User created successfully..")
            return render(request,'create_products.html')
         else:
              return render(request,'create_products.html')  
    else:
        return redirect(adminlogin)    

def editproducts(request,id):
    if request.session.has_key('password'):
        product = products.objects.get(id=id) 
        return render(request,'edit_products.html',{'product_data':product})    
    else:
        return redirect(adminlogin)
def updateproducts(request,id):
    if request.session.has_key('password'):
        if request.method=="POST":
            category = request.POST['category']
            productname = request.POST['productname']
            productdesc = request.POST['productdesc']
            price = request.POST['price']
            quantity = request.POST['quantity']
            # productimage = request.POST['productimage']
            product = products.objects.get(id=id)
            product.productname = productname
            product.category = category
            product.productdesc = productdesc
            product.price = price
            product.Quantity = quantity
            # product.productimage = productimage
            if 'productimage' not in request.POST:
                print('notinpost')
                productimage = request.FILES.get('productimage')
            else:
                print('inpost')
                productimage = product.productimage
            product.productimage = productimage
            product.save()
        
            return redirect(adminpanel_products)
        else:
        
            return render(request,'edit_products.html')
    else:
        return redirect(adminlogin)           
                

def deleteproducts(request,id):
    if request.session.has_key('password'):
        product = products.objects.get(id=id) 
        product.delete()
        return redirect(adminpanel_products) 
    else:
       return redirect(adminlogin)              

def createuser(request):
    if request.session.has_key('password'):
        if request.method == 'POST':
            name = request.POST['name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password']
            password2 = request.POST['confirmpassword']
            mobile = request.POST['mobile']
       
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                # return JsonResponse('usernamemismatch',safe=False)
                
                    return redirect('/create_user')
                else: 
                    user = User.objects.create_user(first_name=name,username=username,email=email,password = password1,last_name = mobile)
                    user.save();
                messages.info(request, "User created successfully..")  
                return redirect('/adminpanel')  
                # return JsonResponse('valid', safe=False)       
            else:
                # return JsonResponse('invalid', safe=False)
                # messages.info(request,"password not match")
                return redirect('/create_user')
        else:
            return render(request,'create_user.html')        

def edituser(request,id):
    if request.session.has_key('password'):
        user = User.objects.get(id=id) 
        return render(request,'edit_user.html',{'user_data':user})    
    else:
        return redirect(adminlogin)
def updateuser(request,id):
    if request.session.has_key('password'):
        if request.method=="POST":
            name = request.POST['name']
            username = request.POST['username']
            email = request.POST['email']
            mobile = request.POST['mobile']
            user = User.objects.get(id=id)
            user.first_name = name
            user.username = username
            user.email = email
            user.last_name = mobile
            
            user.save()
        
            return redirect(adminpanel)
        else:
        
            return render(request,'edit_user.html')
    else:
        return redirect(adminlogin)           
                

def deleteuser(request,id):
    if request.session.has_key('password'):
        user = User.objects.get(id=id) 
        user.delete()
        return redirect(adminpanel) 
    else:
       return redirect(adminlogin)              

def adminlogout(request):
    if request.session.has_key('password'):
        request.session.flush()
        return redirect(adminlogin)
           
    
def usersignup(request):
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
        return render(request,'signup.html')   

def usersignin(request):
    if request.user.is_authenticated:
        return redirect(home)
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
        return render(request,'user_signin.html')
   

def home(request):
    product = products.objects.all()
    
    if request.user.is_authenticated:
        return render(request,'home.html',{'product_data':product})
    else:
        return redirect(usersignin)      

def userlogout(request):
     if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request, "Logged out Successfully")
        return redirect(usersignin)             
