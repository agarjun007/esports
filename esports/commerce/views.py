from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import products,Category
from django.http import JsonResponse
from django.http import HttpResponse 
from userapp.models import *
import base64
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from PIL import Image
from django.core.files import File
from datetime import date,datetime,timedelta

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
        order = Order.objects.all()
        dict = {}
        for order in order:
            if not order.tid in dict.keys():
                dict[order.tid]=order
                
        print(len(dict))
        length_order = len(dict)
        length_user =len(table)
        length_product =len(product)
        labels = []
        data = []
        data=[length_product,length_user,length_order]
        # print(label)
        print(data)    
        return render(request,'commerce/admin_panel.html',{'table_data':table,'length_user':length_user,'length_product':length_product,'length_order':length_order,'data': data})
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
        for category in table:
            totalitems =  products.objects.filter(category=category)
            category.productcount = totalitems.count()
            
            # dict[category] = productcount
       
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
            # productimage = request.FILES.get('productimage')
            image_data = request.POST['pro_img']
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
            product = products.objects.create(category=category,productname=productname,productdesc=productdesc,price=price,Quantity= quantity,productimage=data,unit=unit)
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
                
def blockuser(request,id):
    if request.session.has_key('password'):
        user = User.objects.get(id=id) 
        if user.is_active == True:
            user.is_active = False
            user.save()

        else:
            user.is_active = True   
            user.save()
        return redirect(adminpanel_user) 
    else:
       return redirect(adminlogin)   
def deleteuser(request,id):
    if request.session.has_key('password'):
        user = User.objects.get(id=id) 
        user.delete()
        return redirect(adminpanel) 
    else:
       return redirect(adminlogin)    

def adminpanel_orders(request):
    if request.session.has_key('password'):
        orders = Order.objects.all()
        grandtotal = 0
        dict = {}
        for order in orders:
            if not order.tid in dict.keys():
                dict[order.tid]=order
                dict[order.tid].orderprice = order.totalprice
            else:
                dict[order.tid].orderprice += order.totalprice
        print(len(dict))
        return render(request,'commerce/adminpanel_orders.html',{'table_data': dict})
    else:
        return redirect(adminlogin) 

def cancel_order(request,tid):
    if request.session.has_key('password'):
        order = Order.objects.filter(tid=tid)
        for items in order:
            items.order_status = 'Cancelled'
            items.save()  
        return redirect(adminpanel_orders)
    else:
        return redirect(adminlogin)

def confirm_order(request,tid):
    if request.session.has_key('password'):
        order = Order.objects.filter(tid=tid)
        for items in order:
            items.order_status = 'Confirmed'
            items.save()
        return redirect(adminpanel_orders)  
    else:
        return redirect(adminlogin)   

def adminpanel_reports(request):
    if request.session.has_key('password'):
        if request.method == 'POST':
            report_mode = 1
            if 'date_report' in request.POST:                
                from_date = request.POST['from']
                to_date = request.POST['to']
                orders = Order.objects.filter(tdate__range=[from_date, to_date])
                print(from_date,to_date)
                dict = {}           
                for order in orders:
                    if not order.tid in dict.keys():
                        dict[order.tid]=order
                        dict[order.tid].orderprice = order.totalprice
                    else:
                        dict[order.tid].orderprice += order.totalprice
                        
                return render(request,'commerce/adminpanel_reports.html',{'table_data': dict,'report_mode':report_mode})
            elif 'category_report' in request.POST:
                report_type = request.POST['report_type']
                if report_type == 'this_day':
                    print(report_type)
                    today_date = date.today()
                    orders = Order.objects.filter(tdate=today_date)
                    dict = {}           
                    for order in orders:
                        if not order.tid in dict.keys():
                            dict[order.tid]=order
                            dict[order.tid].orderprice = order.totalprice
                        else:
                            dict[order.tid].orderprice += order.totalprice
                            
                    return render(request,'commerce/adminpanel_reports.html',{'table_data': dict,'report_mode':report_mode,'heading':'Today'})

                elif report_type == 'last_7_days':
                    print(report_type) 
                    today = date.today()
                    lastweek_from = today - timedelta(days=7)
                    print(lastweek_from)
                    orders = Order.objects.filter(tdate__range=[lastweek_from, today])
                    print(lastweek_from,today)
                    dict = {}           
                    for order in orders:
                        if not order.tid in dict.keys():
                            dict[order.tid]=order
                            dict[order.tid].orderprice = order.totalprice
                        else:
                            dict[order.tid].orderprice += order.totalprice
                            
                    return render(request,'commerce/adminpanel_reports.html',{'table_data': dict,'report_mode':report_mode,'heading':'Previous Week'})

                elif report_type == 'this_month':
                    print(report_type)  
                    today_date = date.today()
                    # month = today_date.month
                    month = today_date.strftime('%B')
                    orders = Order.objects.filter(tdate__month=today_date.month)
                    dict = {}           
                    for order in orders:
                        if not order.tid in dict.keys():
                            dict[order.tid]=order
                            dict[order.tid].orderprice = order.totalprice
                        else:
                            dict[order.tid].orderprice += order.totalprice
                            
                    return render(request,'commerce/adminpanel_reports.html',{'table_data': dict,'report_mode':report_mode,'heading':month})

                elif report_type == 'annual':
                    print(report_type)     
                    today_date = date.today()
                    year =today_date.year
                    orders = Order.objects.filter(tdate__year=today_date.year)
                    dict = {}           
                    for order in orders:
                        if not order.tid in dict.keys():
                            dict[order.tid]=order
                            dict[order.tid].orderprice = order.totalprice
                        else:
                            dict[order.tid].orderprice += order.totalprice
                            
                    return render(request,'commerce/adminpanel_reports.html',{'table_data': dict,'report_mode':report_mode,'heading':year})

        else:
            return render(request,'commerce/adminpanel_reports.html')
    else:
        return redirect(adminlogin)

def adminpanel_subreports(request,status):
    if status == 'Confirmed':
        orders = Order.objects.filter(order_status=status)               
        dict = {}           
        for order in orders:
            if not order.tid in dict.keys():
                dict[order.tid]=order
                dict[order.tid].orderprice = order.totalprice
            else:
                dict[order.tid].orderprice += order.totalprice
        
        return render(request,'commerce/adminpanel_subreports.html',{'table_data': dict,'heading':status}) 

    elif status == 'Cancelled':
        orders = Order.objects.filter(order_status=status)               
        dict = {}           
        for order in orders:
            if not order.tid in dict.keys():
                dict[order.tid]=order
                dict[order.tid].orderprice = order.totalprice
            else:
                dict[order.tid].orderprice += order.totalprice        
        return render(request,'commerce/adminpanel_subreports.html',{'table_data': dict,'heading':status}) 
        
def adminlogout(request):
    if request.session.has_key('password'):
        request.session.flush()
        return redirect(adminlogin)
           
 