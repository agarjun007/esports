from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse 
import datetime
from commerce.models import *
from .models import *
from django.core.files.storage import FileSystemStorage
from PIL import Image
from django.core.files import File
import razorpay

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
        user = request.user
        cart = Cart.objects.filter(user= user)
        item_count = cart.count()
        return render(request,'userapp/user_home.html',{'product_data':product,'category_data':category,'no':item_count})
    else:
        return redirect(usersignin)  

def userprofile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print('post')
            category = Category.objects.all()
            user = request.user
            cart = Cart.objects.filter(user= user)
            item_count = cart.count()  
            user.first_name = request.POST['name']
            user.last_name = request.POST['mobile']
            user.email = request.POST['email']
            user.save()
                        
            if Userprofile.objects.filter(user=user).exists():
                userdetails = Userprofile.objects.get(user=user)

                if 'profile-image-upload' not in request.POST:
                    print('notinpost')
                    profilepic = request.FILES.get('profile-image-upload')
                else:
                    print('inpost')
                    profilepic = userdetails.profilepic

                userdetails.profilepic = profilepic
                userdetails.save()    
            else: 
                profilepic = request.FILES.get('profile-image-upload')
                Userprofile.objects.create(user = user, profilepic = profilepic)
            
            return redirect(userhome)
        else:        
            category = Category.objects.all()
            user = request.user
            cart = Cart.objects.filter(user= user)
            item_count = cart.count() 
            if Userprofile.objects.filter(user=user).exists():
                userdetails = Userprofile.objects.get(user=user)
                    # for i in userdetails:
                    #     userdetail = i
                    #     break
                return render(request,'userapp/user_profile.html',{'category_data':category,'no':item_count,'userdetails':userdetails})
            else:
                
                return render(request,'userapp/user_profile.html',{'category_data':category,'no':item_count})

    else:
        return redirect(usersignin)      

def category(request,id):
    product= products.objects.filter(category=id)    
    category = Category.objects.all()
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user= user)
        item_count = cart.count()
        return render(request,'userapp/user_home.html',{'product_data':product,'category_data':category,'no':item_count})
    else:    
        return render(request,'userapp/guest_home.html',{'product_data':product,'category_data':category})          

def guesthome(request):
    if request.user.is_authenticated:
        return redirect(userhome)
    product = products.objects.all()
    category = Category.objects.all()

    return render(request,'userapp/guest_home.html',{'product_data':product,'category_data':category})
           
def productview(request,id):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user= user)
        item_count = cart.count()
        category = Category.objects.all()
        product = products.objects.get(id=id)
        return render(request,'userapp/user_product_view.html',{'product_data':product,'category_data':category,'no':item_count})
    else:
        return redirect(guesthome)

def showcart(request): 
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user= user)
        grandtotal = 0
        for item in cart:
            item.totalprice = item.quantity*item.product.price
            grandtotal = grandtotal + item.totalprice
        category= Category.objects.all()
        item_count = cart.count()
        if item_count == 0:
            return render(request,'userapp/user_cart.html',{'category_data':category,'no':item_count}) 
        else:
            return render(request,'userapp/user_cart.html',{'cart_data': cart,'category_data':category,'no':item_count,'grandtotal':grandtotal}) 
        
    else:
        return redirect(guesthome)

def deleteitem(request,id): 
    if request.user.is_authenticated:        
        cart = Cart.objects.filter(id=id)
        cart.delete()
        return redirect(showcart) 
    else:
        return redirect(guesthome)        
def usercart(request,id): 
    if request.user.is_authenticated:
            product =products.objects.get(id=id)
            user = request.user
            if Cart.objects.filter(product=product).exists():
                cart =  Cart.objects.get(product=product)
                if cart.quantity <= cart.product.Quantity:
                    cart.quantity = cart.quantity+1
                    cart.totalprice = cart.product.price * cart.quantity
                    cart.save()   
                    return redirect(userhome)
                else:
                    return redirect(guesthome)               
            else:   
                quantity = 1 
                
                cart =  Cart.objects.create(user=user,product=product,quantity = quantity)                   
                return redirect(userhome) 
    else:
        return redirect(guesthome)      

def cartedit(request):
    id = request.POST["id"]
    count =1
    grandtotal =0
    carts = Cart.objects.filter(user=request.user)
    item = Cart.objects.get(id=id)
    if request.POST["value"] == "add":       
        item.quantity = item.quantity + count
        item.save()
        price = item.product.price * item.quantity 

        for x in carts:
            grandtotal = grandtotal + x.product.price * x.quantity
    elif request.POST["value"]== "sub":
        item.quantity = item.quantity - count
        item.save()
        price = item.product.price * item.quantity 

        for x in carts:
            grandtotal = grandtotal + x.product.price * x.quantity
    return JsonResponse({'total':price,'grandtotal':grandtotal}, safe=False)

def showaddress(request): 
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user= user)       
        category= Category.objects.all()
        item_count = cart.count()
        address =Address.objects.filter(user=user)
        return render(request,'userapp/user_address.html',{'category_data':category,'no':item_count,'address':address}) 
    else:
        return redirect(guesthome)

def editaddress(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            name = request.POST['firstname']
            email = request.POST['email']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            pincode = request.POST['pincode']
            address_details = Address.objects.create(user=user,name=name,email=email,address=address,city=city,state=state,pincode=pincode) 
            return redirect(showaddress)
        else:
            return render(request,'userapp/edit_address.html')   
    else:
        return redirect(guesthome)             

def userorderhistory(request):
    if request.user.is_authenticated:
        user = request.user
        order = Order.objects.filter(user=user)
        category= Category.objects.all()
        cart = Cart.objects.filter(user= user)
        item_count = cart.count()        
        return render(request,'userapp/user_order_history.html',{'items_data': order,'category_data':category,'no':item_count})

def userpayment(request,id):
    if request.user.is_authenticated:
        print('Authentcated')
        if request.method == 'POST':
            print('insidepost')
            user = request.user 
            address = Address.objects.get(id=id)
            grandtotal = 0
            date = datetime.datetime.now()
            trans_id = datetime.datetime.now().timestamp()
            mode =  request.POST['mode']
            print(mode)
            cart = Cart.objects.filter(user= user)
            status= 'pending'
            for item in cart:
                item.totalprice = item.quantity*item.product.price
                grandtotal = grandtotal + item.totalprice
            
            for item in cart:
                order_details = Order.objects.create(user=user, address=address, product=item.product, quantity=item.quantity, totalprice=item.product.price*item.quantity,tdate=date,tid=trans_id,payment_mode=mode,order_status = 'pending',payment_status=status)
                item.product.Quantity = item.product.Quantity - item.quantity
                item.product.save()
            cart.delete()
            if mode == 'COD':
                mode = 'COD'
                messages.info(request,"Order placed Succesfully")
                return JsonResponse({'mode':mode,'tid':trans_id},safe=False)    

            elif mode == 'Paypal':
                mode ='Paypal'
                return JsonResponse({'mode':mode,'tid':trans_id},safe=False)    

            elif mode == 'Razorpay':
                order_amount = grandtotal*100
                order_currency = 'INR'
                client = razorpay.Client(auth = ('rzp_test_EJQneGlqu2SpAQ', 'oCisVDcytFHu60u7EGuzrinD'))
                payment = client.order.create({'amount':order_amount, 'currency':order_currency, 'payment_capture': '1'})
                print(payment)
                mode = 'Razorpay'
                return JsonResponse({'mode':mode,'tid':trans_id},safe=False)    

            
            # return redirect(showcart)
        else:   
            user = request.user 
            address = Address.objects.filter(id=id)        
            cart = Cart.objects.filter(user= user)
            item_count = cart.count()
            grandtotal = 0
            for item in cart:
                item.totalprice = item.quantity*item.product.price
                grandtotal = grandtotal + item.totalprice
            razorpay_total = grandtotal*100
            return render(request,'userapp/user_payment.html',{'cart_data': cart,'no':item_count,'grandtotal':grandtotal,'address':address,'razorpay_total':razorpay_total})     
    else:
        return redirect(guesthome)

def payplpayment(request):
    tid = request.POST['tid']
    print(tid)
    orders = Order.objects.filter(tid=tid)
    for order in orders:
        order.payment_status ='SUCCESS'
        order.save()
    return JsonResponse('success',safe=False)    

def userlogout(request):
     if request.user.is_authenticated:
        auth.logout(request)
        return redirect(usersignin)             


   