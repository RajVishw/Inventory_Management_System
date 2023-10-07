from django.contrib import admin
from django.urls import path,re_path
from app import views

urlpatterns = [
    re_path(r'^$',views.HomePage),
    
    #-------Item----------------
    re_path(r'^add/item/(?P<action>\w+)/(?P<pk>(.*)+|)$',views.InsertUpdate),
    re_path(r'^item/(?P<action>\w+)/(?P<pk>(.*)+|)$',views.AllItemsDeleteItem ),
    
    #--------Supplier-----------
    re_path(r'^add/supplier/(?P<action>\w+)/(?P<pk>(.*)+|)$',views.InsertUpdateSupplier),
    re_path(r'^supplier/(?P<action>\w+)/(?P<pk>(.*)+|)$',views.AllItemsDeleteSupplier ),
    path('suppliers/', views.GetAllSuppliers),
    
   
#    re_path(r'^add/item/(?P<action>\w+)/(?P<pk>(.*)+|)$',views.InsertUpdate),

  path('purchase/', views.Purchase_Daetails, name='purchase'),
  path('purchase/add/', views.Temp_Data, name='purchase_form'),
 
  path('getprice/', views.get_item_price,name='get_item_price'),
  
  path('getpricesale/', views.get_item_price_sale,name='get_item_price_sale'),
  
  path('purchase/<invoice>', views.viewPurchase),
  path('purchase_report/', views.purchase_report, name='purchase_report'),
  
 
   #--------------------
   path('sale/', views.AllSaleDetails, name='sale'),
   path('sale/add/', views.Temp_Data_sale, name='sale_form'),
   path('sale_report/', views.Sale_report, name='Sale_report'),
   
   
  
   #--------------------

   path('filter/', views.Purchase_Details),
#    path('dt/', views.Details),
   path("details/<int:invoice>",views.Sales,name="delete"),
   path('getpricesale/', views.get_item_price_sale, name='get_item_price'),
       #------------------Final Report............
   path('available/', views.Avialable_Report, name='get_item_price'),
   path('finalreport/', views.Final_availability),
#    path('chkquntity/', views.check_quantity_availability),
   path('check/', views.check_quantity_availability),
   
   path('purchase/x/', views.x,name="jadu")
   
   
   
     
]