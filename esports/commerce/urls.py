from django.urls import path
from . import views
urlpatterns = [
   
    path('admin_login/', views.adminlogin,name='adminlogin'),    
    path('admin_logout/', views.adminlogout,name='adminlogout'),
    path('adminpanel/', views.adminpanel,name='adminpanel'),

    path('adminpanel_user/', views.adminpanel_user,name='adminpaneluser'),
    path('create_user/', views.createuser,name='createuser'),
    path('edit_user/<int:id>', views.edituser,name='edituser'),
    path('update_user/<int:id>', views.updateuser,name='updateuser'),
    path('delete_user/<int:id>', views.deleteuser,name='deleteuser'),
    path('block_user/<int:id>', views.blockuser,name='blockuser'),

    
    path('adminpanel_category/', views.adminpanel_category,name='adminpanelcategory'),
    path('create_category/', views.createcategory,name='createcategory'),
    path('edit_category/<int:id>', views.editcategory,name='editcategory'),
    path('update_category/<int:id>', views.updatecategory,name='updatecategory'),
    path('delete_category/<int:id>', views.deletecategory,name='deletecategory'),

    path('adminpanel_products/', views.adminpanel_products,name='adminpanelproducts'),
    path('create_products/', views.createproducts,name='createproducts'),
    path('edit_products/<int:id>', views.editproducts,name='editproducts'),
    path('update_products/<int:id>', views.updateproducts,name='updateproducts'),
    path('delete_products/<int:id>', views.deleteproducts,name='deleteproducts'),

    path('adminpanel_orders/', views.adminpanel_orders,name='adminpanelorders'),
    path('adminpanel_suborders/<str:status>', views.adminpanel_suborders,name='adminpanelsuborders'),
    path('adminpanel_suborders/<str:status>', views.adminpanel_suborders,name='adminpanelsuborders'),
    path('confirm_order/<str:tid>', views.confirm_order,name='confirmorder'),
    path('cancel_order/<str:tid>', views.cancel_order,name='cancelorder'),

    path('adminpanel_reports/', views.adminpanel_reports,name='adminpanelreports'),
    path('adminpanel_subreports/<str:status>', views.adminpanel_subreports,name='adminpanelsubreports'),

 
]
