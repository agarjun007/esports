from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import products
from django.http import JsonResponse
from django.http import HttpResponse 

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
        return render(request,'admin_panel.html')
    else:
        return redirect(adminlogin)

def adminpanel_products(request):
    if request.session.has_key('password'):
        table = products.objects.all()
        return render(request,'adminpanel_products.html')
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
            productimage = request.POST['productimage']

            product = products.objects.create(category=category,productname=productname,productdesc=productdesc,price=price,Quantity= quantity,productimage=productimage)
            product.save();
            messages.info(request, "User created successfully..")
            return render(request,'create_products.html')
         else:
              return render(request,'create_products.html')  
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
        password1 = request.POST['password']
        password2 = request.POST['confirmpassword']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
       
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                # return JsonResponse('usernamemismatch',safe=False)
                
                return redirect('/')
            else: 
                user = User.objects.create_user(first_name=name,username=username,email=email,password = password1,address = address,city = city,state = state,pincode = pincode)
                user.save();
            messages.info(request, "User created successfully..")  
            return redirect(usersignin)  
            # return JsonResponse('valid', safe=False)       
        else:
            # return JsonResponse('invalid', safe=False)
            # messages.info(request,"password not match")
            return redirect('/')

    else:    
        return render(request,'signup.html')   

def usersignin(request):
    return render(request,'user_signin.html')

def home(request):
    return render(request,'home.html')             
