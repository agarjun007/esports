from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('admin_login/', views.adminlogin,name='adminlogin'),
    path('adminpanel/', views.adminpanel,name='adminpanel'),
    path('adminpanel_products/', views.adminpanel_products,name='adminpanel'),
    path('create_products/', views.createproducts,name='createproducts'),
    path('admin_logout/', views.adminlogout,name='adminlogout'),
    path('signup/', views.usersignup,name='usersignup'),
    path('signin/', views.usersignin,name='usersignin'),
]
