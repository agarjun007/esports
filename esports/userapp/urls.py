from django.urls import path
from . import views



urlpatterns = [
    path('', views.guesthome,name='guesthome'),
    path('home/', views.userhome,name='userhome'),  
    path('category/<int:id>', views.category,name='category'),  
    path('product_view/<int:id>', views.productview,name='productview'),
    path('user_cart/<int:id>', views.usercart,name='usercart'),
    path('user_payment/', views.userpayment,name='userpayment'),
    path('signup/', views.usersignup,name='usersignup'),
    path('signin/', views.usersignin,name='usersignin'),
    path('user_logout/', views.userlogout,name='userlogout'),
]