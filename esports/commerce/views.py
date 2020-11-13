from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import products,Category
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
            return render(request,'commerce/admin_login.html')        

def adminpanel(request):
    if request.session.has_key('password'):
        table = User.objects.all()
        product = products.objects.all()
        length_user =len(table)
        length_product =len(product)
        return render(request,'commerce/admin_panel.html',{'table_data':table,'length_user':length_user,'length_product':length_product})
    else:
        return redirect(adminlogin)

def adminpanel_user(request):
    if request.session.has_key('password'):
        table = User.objects.all()
        return render(request,'commerce/adminpanel_user.html',{'table_data': table})
    else:
        return redirect(adminlogin)     

def adminpanel_category(request):
    if request.session.has_key('password'):
        table = Category.objects.all()
        return render(request,'commerce/adminpanel_category.html',{'table_data': table})
    else:
        return redirect(adminlogin)    

def createcategory(request):
    if request.session.has_key('password'):
        if request.method == 'POST':
        
            categoryname = request.POST['categoryname']
            category = Category.objects.create(categoryname=categoryname)
            category.save();            
            return redirect(adminpanel_category)
        else:
            return render(request,'commerce/create_category.html')  
    else:
        return redirect(adminlogin)    

def editcategory(request,id):
    if request.session.has_key('password'):
        category = Category.objects.get(id=id) 
        return render(request,'commerce/edit_category.html',{'category_data':category})    
    else:
        return redirect(adminlogin)
def updatecategory(request,id):
    if request.session.has_key('password'):
        if request.method=="POST":
            categoryname = request.POST['categoryname']           
            category = Category.objects.get(id=id)
            category.categoryname = categoryname
            category.save()        
            return redirect(adminpanel_category)
        else:        
            return render(request,'commerce/edit_category.html')
    else:
        return redirect(adminlogin)           
                

def deletecategory(request,id):
    if request.session.has_key('password'):
        category = Category.objects.get(id=id) 
        category.delete()
        return redirect(adminpanel_category) 
    else:
       return redirect(adminlogin)              



def adminpanel_products(request):
    if request.session.has_key('password'):
        table = products.objects.all()
        return render(request,'commerce/adminpanel_products.html',{'table_data': table})
    else:
        return redirect(adminlogin)        

def createproducts(request):
    if request.session.has_key('password'):
        if request.method == 'POST':        
            category = Category.objects.get(id=request.POST['category'])
            productname = request.POST['productname']
            productdesc = request.POST['productdesc']
            price = request.POST['price']
            quantity = request.POST['quantity']
            unit = request.POST['unit']
            productimage = request.FILES.get('productimage')
            product = products.objects.create(category=category,productname=productname,productdesc=productdesc,price=price,Quantity= quantity,productimage=productimage,unit=unit)
            product.save();
            messages.info(request, "Product created successfully..")
            return redirect(createproducts)
        else:     
            category = Category.objects.all()      
            return render(request,'commerce/create_products.html',{'category_data':category})  
    else:
        return redirect(adminlogin)    

def editproducts(request,id):
    if request.session.has_key('password'):
        product = products.objects.get(id=id) 
        category = Category.objects.all()
        return render(request,'commerce/edit_products.html',{'category_data':category,'product_data':product})     
    else:
        return redirect(adminlogin)
def updateproducts(request,id):
    if request.session.has_key('password'):
        if request.method=="POST":
            category = Category.objects.get(id = request.POST['category'])
            productname = request.POST['productname']
            productdesc = request.POST['productdesc']
            price = request.POST['price']
            quantity = request.POST['quantity']
            unit = request.POST['unit']
            # productimage = request.POST['productimage']
            product = products.objects.get(id=id)
            product.productname = productname
            product.category.categoryname = category.categoryname
            product.productdesc = productdesc
            product.price = price
            product.Quantity = quantity
            product.unit = unit
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
        
            return render(request,'commerce/edit_products.html')
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
            return render(request,'commerce/create_user.html')        

def edituser(request,id):
    if request.session.has_key('password'):
        user = User.objects.get(id=id) 
        return render(request,'commerce/edit_user.html',{'user_data':user})    
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
        
            return render(request,'commerce/edit_user.html')
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
           
 