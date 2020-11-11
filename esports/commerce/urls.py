from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('product_view/', views.productview,name='productview'),
    path('admin_login/', views.adminlogin,name='adminlogin'),
    path('adminpanel/', views.adminpanel,name='adminpanel'),
    path('adminpanel_user/', views.adminpanel_user,name='adminpaneluser'),
    path('adminpanel_products/', views.adminpanel_products,name='adminpanelproducts'),
    path('create_products/', views.createproducts,name='createproducts'),
    path('edit_products/<int:id>', views.editproducts,name='editproducts'),
    path('update_products/<int:id>', views.updateproducts,name='updateproducts'),
    path('delete_products/<int:id>', views.deleteproducts,name='deleteproducts'),
    path('create_user/', views.createuser,name='createuser'),
    path('edit_user/<int:id>', views.edituser,name='edituser'),
    path('update_user/<int:id>', views.updateuser,name='updateuser'),
    path('delete_user/<int:id>', views.deleteuser,name='deleteuser'),
    path('admin_logout/', views.adminlogout,name='adminlogout'),
    path('signup/', views.usersignup,name='usersignup'),
    path('signin/', views.usersignin,name='usersignin'),
    path('user_logout/', views.userlogout,name='userlogout'),
]
