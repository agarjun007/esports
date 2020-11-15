from django.urls import path
from . import views



urlpatterns = [
    path('', views.guesthome,name='guesthome'),
    path('home/', views.userhome,name='userhome'),  
    path('signup/', views.usersignup,name='usersignup'),
    path('signin/', views.usersignin,name='usersignin'),

    path('category/<int:id>', views.category,name='category'),  
    path('product_view/<int:id>', views.productview,name='productview'),
    path('show_cart/', views.showcart,name='showcart'),
    path('delete_item/<int:id>', views.deleteitem,name='deleteitem'),
    path('user_cart/<int:id>', views.usercart,name='usercart'),
    path('user_order_history/', views.userorderhistory,name='userorderhistory'),
    path('user_payment/', views.userpayment,name='userpayment'),
    path('user_logout/', views.userlogout,name='userlogout'),
]