from django.urls import path
from . import views



urlpatterns = [
    path('', views.guesthome,name='guesthome'),
    path('home/', views.userhome,name='userhome'),  
    path('signup/', views.usersignup,name='usersignup'),
    path('signin/', views.usersignin,name='usersignin'),
    path('otplogin/', views.otplogin,name='otplogin'),
    path('verifyotp/', views.verifyotp,name='verifyotp'),

    path('category/<int:id>', views.category,name='category'),  
    path('product_view/<int:id>', views.productview,name='productview'),
    path('show_cart/', views.showcart,name='showcart'),   

    path('delete_item/<int:id>', views.deleteitem,name='deleteitem'),
    path('user_profile/', views.userprofile,name='userprofile'),
    path('user_cart/<int:id>', views.usercart,name='usercart'),
    path('cart_edit/', views.cartedit,name='cartedit'),
    path('show_address/', views.showaddress,name='showaddress'),
    path('create_address/', views.createaddress,name='createaddress'),
    path('edit_address/<int:id>', views.editaddress,name='editaddress'),
    path('user_order_history/', views.userorderhistory,name='userorderhistory'),
    path('user_payment/<int:id>', views.userpayment,name='userpayment'),
    path('paypal_payment/', views.payplpayment,name='paypalpayment'),
    path('razorpay_payment/', views.razorpaypayment,name='razorpaypayment'),
    path('user_logout/', views.userlogout,name='userlogout'),

]