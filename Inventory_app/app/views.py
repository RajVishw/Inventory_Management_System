from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import *
from.models import *
from.models import Purchase_Details
from django.db import connections
from django.http import JsonResponse
from django.db.models import F
from django.db.models import Count
from django.db import connection
from django.db.models import Sum
from urllib.parse import urlencode

# Create your views here.
#--------Item_Operations------
def HomePage(request):
    return render(request,"homepage.html")

def InsertUpdate(request,action,pk):
    
    if action=="save":
        context ={}
        form = ItemForm(request.POST )
        
        if form.is_valid():
         name=form.cleaned_data['item_name']
         code=form.cleaned_data['item_code']
         price=form.cleaned_data['price']
         status=form.cleaned_data['status']
         date=form.cleaned_data['datetime']
        
         data=Item.objects.create(item_name=name,item_code=code,price=price,status=status,datetime=date)
         
         return redirect('/item/items')
        context['form']= form
        return render(request, "index.html",context)
      
    elif action=="update":
         data=Item.objects.get(pk=pk)
         form=ItemForm(instance=data)
         context={
             "form":form,
             'action':action
            }
         form = ItemForm(request.POST or None, request.FILES ,instance=data)
         if form.is_valid():
             
              name=form.cleaned_data['item_name']
              code=form.cleaned_data['item_code']
              price=form.cleaned_data['price']
              status=form.cleaned_data['status']
              date=form.cleaned_data['datetime']
              Item.objects.filter(pk=pk).update(item_name=name,item_code=code,price=price,status=status,datetime=date)
              return redirect('/item/items')
    
         form = ItemForm(request.POST or None, request.FILES ,instance=data)
        
         return render(request, 'update.html',context) 
 
    
    return HttpResponse("something is Wrong")

def AllItemsDeleteItem(request,action,pk):
    
    if action=="items":
        data=Item.objects.filter(status=True)
        return render(request,'allitems.html',{"key1":data})
    elif action=="delete":
        # ddta=Supplier.objects.get(pk=pk)
        # ddta.status=False
        Item.objects.filter(pk=pk).update(status=False)
        return redirect("/item/items") 
    
    return HttpResponse("Thing is wrong")

#--------Supplier Operation--------------------------------
def InsertUpdateSupplier(request,action,pk):
    
    if action=="save":
        context ={}
        form = SupplierForm(request.POST )
        
        if form.is_valid():
         name=form.cleaned_data['supplier_name']
         mobile=form.cleaned_data['mobile_no']
         address=form.cleaned_data['address']
         status=form.cleaned_data['status']
         
       
        
         data=Supplier.objects.create(supplier_name=name,mobile_no=mobile,address=address,status=status)
         
         return redirect("/suppliers/")
        context['form']= form
        return render(request, "addsupplier.html",context)
      
    elif action=="update":
         data=Supplier.objects.get(pk=pk)
         form=SupplierForm(instance=data)
         context={
             "form":form,
             'action':action
            }
         form = SupplierForm(request.POST )
         if form.is_valid():
             name=form.cleaned_data['supplier_name']
             mobile=form.cleaned_data['mobile_no']
             address=form.cleaned_data['address']
             status=form.cleaned_data['status']
    
             data=Supplier.objects.filter(pk=pk).update(supplier_name=name,mobile_no=mobile,address=address,status=status)
         
             return redirect("/suppliers/")
    
         form = SupplierForm(request.POST )
        
         return render(request, 'updateSupplier.html',context) 
 
    
    return HttpResponse("something is Wrong")

def AllItemsDeleteSupplier(request,action,pk):
    if action=="delete":
        # ddta=Supplier.objects.get(pk=pk)
        # ddta.status=False
        Supplier.objects.filter(pk=pk).update(status=False)
        return redirect("/suppliers/") 
    
    return HttpResponse("Thing is wrong")

def GetAllSuppliers(request):
     data=Supplier.objects.filter(status=True)
     return render(request,'allsuppliers.html',{"key1":data})
    
    
#--------End Supplier Op

# def purchase_form(request):
#     if request.method == 'POST':
#         mstr_form = PurchaseMstrForm(request.POST)
#         details_form = PurchaseDetailsForm(request.POST)
#         if mstr_form.is_valid() and details_form.is_valid():
#             # Save the PurchaseMstr instance first
#             purchase_mstr = mstr_form.save()
#             # Link the PurchaseDetails to the PurchaseMstr instance
#             purchase_details = details_form.save(commit=False)
#             purchase_details.purchase_mstr = purchase_mstr
#             purchase_details.save()
#             return HttpResponse("SucessFullyAdded")
#         # Redirect to a success page
#     else:
#         mstr_form = PurchaseMstrForm()
#         details_form = PurchaseDetailsForm()
#     return render(request, 'purchase.html', {'mstr_form': mstr_form, 'details_form': details_form})

def Purchase_Daetails(request):
   
     data=Purchase_Mstr.objects.all()
     return render(request,'purchaselist.html',{'data':data})
     
    
def Temp_Data(request):
    print('input')
  
    details_form = PurchaseDetailsForm()
    alldata = Temp_Table.objects.all()
    t_amount=0
    for am in alldata:
        t_amount+=am.total
        
    dt = Temp_Table.objects.last()
    print(dt)

        
    if request.method == 'POST':
        mstr_form = PurchaseMstrForm(request.POST)
        details_form = PurchaseDetailsForm(request.POST)
        if mstr_form.is_valid() and details_form.is_valid():
        
            number=mstr_form.cleaned_data['invoice_no']
            date=mstr_form.cleaned_data['invoice_date']
            supplier_id=mstr_form.cleaned_data['supplier_id']
            # id=supplier_id.id
            # total_amount=mstr_form.cleaned_data['total_amount']
            #--------------------------
            product_id=details_form.cleaned_data['item']
            quantity=details_form.cleaned_data['quantity']
            price=details_form.cleaned_data['price']
            total=details_form.cleaned_data['total']
            
        
            temp=Temp_Table.objects.create(invoice_no=number,
                                           invoice_date=date,
                                           supplier_id=supplier_id,
                                           product_id=product_id,
                                           quantity=quantity,
                                           price=price,
                                           total=total)
           
            return redirect('purchase_form')
      
    else:
         mstr_form = PurchaseMstrForm()
         details_form = PurchaseDetailsForm()
         
         if dt:
             
            dic = {
            'invoice_no': dt.invoice_no,
            'invoice_date': dt.invoice_date,
            'supplier_id': dt.supplier_id,
            
           
        }
            mstr_form = PurchaseMstrForm(initial=dic)
            print(dic)
            
    
       
        
    if 'create_purchase' in request.POST:
        if request.method == 'POST':
       
        # used default as we defined InventoryIMS db there
         with connections['default'].cursor() as cursor:
            # Insert data from TempPurchase into PurchaseMaster
            insert_purchase_master_sql = """
            INSERT INTO app_purchase_mstr (supplier_id_id, invoice_no, invoice_date, total_amount)
            
            SELECT supplier_id_id, invoice_no, invoice_date, SUM(total) FROM app_temp_table
            GROUP BY supplier_id_id, invoice_no, invoice_date
            """
            cursor.execute(insert_purchase_master_sql)
            
            # Retrieve the last inserted ID from purchase_master
            purchase_master=Purchase_Mstr.objects.latest('id')
            print(purchase_master.id)
            purchase_master_id=purchase_master.id

            # # # Insert data from TempPurchase into PurchaseDetails
            insert_purchase_details_sql = """
            INSERT INTO app_purchase_details (purchase_mstr_id, item_id, price, quantity, total)
            SELECT %s, product_id_id, price, quantity, total FROM app_temp_table
            """
            cursor.execute(insert_purchase_details_sql, [purchase_master_id])

            # # # Clear TempPurchase table
            clear_temp_purchase_sql = "DELETE FROM app_temp_table"
            cursor.execute(clear_temp_purchase_sql)



        return redirect('purchase')  
        
        
    return render(request, 'purchase.html', {'mstr_form': mstr_form, 'details_form': details_form,'key1':alldata,'amount':t_amount})


def Temp_Data_sale(request):
    alldata = Temp_Table_Sales.objects.all()
    t_amount=0
    for am in alldata:
        t_amount+=am.amount
    
    
     
    dt = Temp_Table_Sales.objects.last() 
    details_form = SaleDetailsForm()
    
    if request.method == 'POST':
         mstr_form = SaleMstrForm(request.POST)
         details_form = SaleDetailsForm(request.POST)
         
         if mstr_form.is_valid() and details_form.is_valid():
            customer_name=mstr_form.cleaned_data['customer_name']
            invoice_no=mstr_form.cleaned_data['invoice_no']
            invoice_date=mstr_form.cleaned_data['invoice_date']
            number=mstr_form.cleaned_data['number']

            #----------------------------------
            item_id=details_form.cleaned_data['item_id']
            quantity=details_form.cleaned_data['quantity']
            price=details_form.cleaned_data['price']
            amount=details_form.cleaned_data['amount']
            
            
            #total_quantity = PurchaseDetail.objects.filter(item_id=productname)
            P_quantity = Purchase_Details.objects.filter(item=item_id).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
            
            S_quantity = Sale_Details.objects.filter(item_id=item_id).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
            
            T_total_quantity = Temp_Table_Sales.objects.filter(item_id=item_id).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0


            available_quantity = P_quantity - S_quantity 
            if available_quantity >= quantity + T_total_quantity:
         
                temp=Temp_Table_Sales.objects.create(customer_name=customer_name,
                                invoice_no=invoice_no,
                                invoice_date=invoice_date,
                                number=number,
                                item_id=item_id,
                                quantity=quantity,
                                price=price,
                                amount=amount
                                
                                )
                return redirect('sale_form')
            else:
                # Quantity not available, display an alert message and redirect back to the add_sale page
                
        
                return HttpResponse('<script>alert("Quantity is not available for this item."); window.location.href = window.location.href;</script>')
    
                
                
        
        
        
    else:
        mstr_form = SaleMstrForm()
        details_form = SaleDetailsForm()
        
         
        if dt:
            dic = {
            'customer_name': dt.customer_name,
                'invoice_no': dt.invoice_no,
                'invoice_date': dt.invoice_date,
                'number': dt.number,
        }
            mstr_form = SaleMstrForm(initial=dic)
       
        
        
    if 'create_sale' in request.POST:
        if request.method == 'POST':
       
        # used default as we defined InventoryIMS db there
         with connections['default'].cursor() as cursor:
            # Insert data from TempPurchase into PurchaseMaster
            insert_sale_master_sql = """
            INSERT INTO app_sale_mstr(customer_name, invoice_no, invoice_date, number, totoal)
            
           
            SELECT customer_name, invoice_no, invoice_date, number, SUM(amount)
            FROM app_temp_table_sales
            GROUP BY customer_name, invoice_no, invoice_date, number
            """
            cursor.execute(insert_sale_master_sql)

            # Retrieve the last inserted ID from purchase_master
            sale_master=Sale_Mstr.objects.latest('id')
            sale_master_id=sale_master.id
            print(sale_master_id)
            print("hello")
            

            # # Insert data from TempPurchase into PurchaseDetails
            insert_sale_details_sql = """
              INSERT INTO app_sale_details ( sale_mstr_id, quantity, price, amount, item_id_id)
            
            SELECT %s, quantity, price, amount, item_id_id FROM app_temp_table_sales
            """
            cursor.execute(insert_sale_details_sql, [sale_master_id])

            # # # Clear TempPurchase table
            clear_temp_sale_sql = "DELETE FROM app_temp_table_sales"
            cursor.execute(clear_temp_sale_sql)  
            
        return redirect('sale')       
        
    return render(request, 'sale.html', {'mstr_form': mstr_form, 'details_form': details_form,'key1':alldata,'amount':t_amount})   
            

#-----------------------------

def AllSaleDetails(request):
     data=Sale_Mstr.objects.all()
     return render(request,'saledetails.html',{'key1':data})
     

def get_item_price(request):
    print("updated")
    if  request.method == "GET":
        item_id = request.GET.get("item")
        item = Item.objects.get(id=item_id)
        price = item.price
        id = item.id
        print(price,id)
        print("working")
        data = {'price': price, }
        
        return JsonResponse(data)
    
    
    
    
def get_item_price_sale(request):
    print("updated")
    if request.method == "GET":
        item_id = request.GET.get("item")
        try:
            item = Item.objects.get(id=item_id.id)
        except Item.DoesNotExist:
            return HttpResponse("Item not found", status=404)
        
        price = item.price  # Assuming the price is stored in a field called 'price' in your Item model
        available_quantity = Purchase_Details.objects.filter(item=item).aggregate(total=models.Sum('quantity'))['total'] or 0
        
        data = {
            'price': price,
            'available_quantity': available_quantity 
        }
        
        print(data)
        
        return JsonResponse(data)  
    

      
def DeleteData(request,pk):
    ddta=Item.objects.get(id=pk)
    ddta.delete()
    return redirect("items")

def purchase_report(request):
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Query the database to fetch purchase records within the date range
            purchases = Purchase_Mstr.objects.filter(
                invoice_date__range=(start_date, end_date)
            )

            return render(request, 'purchasefinal.html', {'purchases': purchases})
    else:
        form = DateRangeForm()

    return render(request, 'purchasefinal.html', {'form': form})

def Purchase_Report_View(request,invoice_no):
    puchase=get_object_or_404(Purchase_Mstr,invoice_no=invoice_no)
    pur_detl=Purchase_Details.objects.filter(purchase_mstr=puchase)
    
    
    
    t_amount=0
    for am in pur_detl:
        t_amount+=am.total
    return render(request, 'viewpurchase_report.html',{'purchase':puchase, 'purchase_dt':pur_detl,'total':t_amount})



def get_item_price_sale(request):
    print("updated")
    if  request.method == "GET":
        item_id = request.GET.get("item")
        item = Item.objects.get(id=item_id)
        item_name=item.item_name
        price = item.price
        id = item.id
        print(price,id)
        print("working")
        

        try:
          item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
          return HttpResponse("Item not found", status=404)
        available_quantity = Purchase_Details.objects.filter(item=item).aggregate(total=models.Sum('quantity'))['total']
   
        
        data = {'price': price, 'id': id, 'avl': available_quantity}
        
        return JsonResponse(data)
    
def Sale_report(request):
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            sale = Sale_Mstr.objects.filter(
                invoice_date__range=(start_date, end_date)
            )
            print(sale)
            return render(request, 'salereport.html', {'sale': sale})
    else:
        form = DateRangeForm()

    return render(request, 'salereport.html', {'form': form})    

def Sales(request,invoice):
    sale=get_object_or_404(Sale_Mstr,invoice_no=invoice)
    sale_dt=Sale_Details.objects.filter(sale_mstr=sale)

    t_amount=0
    for am in sale_dt:
        t_amount+=am.amount
   
    return render(request, 'viewSaleReport.html',{'purchase':sale, 'purchase_dt':sale_dt,'total':t_amount})

def Avialable_Report(request):
    
    return HttpResponse("Working")

def viewPurchase(request,invoice):
     puchase=get_object_or_404(Purchase_Mstr,invoice_no=invoice)
     pur_detl=Purchase_Details.objects.filter(purchase_mstr=puchase)
     t_amount=0
     for am in pur_detl:
        t_amount+=am.total

     return render(request, 'purchaseView.html',{'purchase':puchase, 'purchase_dt':pur_detl,'total':t_amount})
 


def Final_availability(request):
    purchase_quantities = (
        Purchase_Details.objects.values('item_id__item_name')
        .annotate(purchase_quantity=Sum('quantity'))
    )

    sale_quantities = (
        Sale_Details.objects.values('item_id__item_name')
        .annotate(sale_quantity=Sum('quantity'))
    )

    merge = []
    for item_purchase in purchase_quantities:
        item_name = item_purchase['item_id__item_name']
        purchase_quantity = item_purchase['purchase_quantity']
        
        sale_quantity = 0
        for item in sale_quantities:
            if item['item_id__item_name'] == item_name:
                sale_quantity = item['sale_quantity']
                break

        available_quantity = purchase_quantity - sale_quantity

        merge.append({
            'item_name': item_name,
            'purchase_quantity': purchase_quantity,
            'sale_quantity': sale_quantity,
            'available_quantity': available_quantity,
        })

    return render(request, 'Available.html', {'data': merge})


def check_quantity_availability(request):
    print("hello")
    item_id = 31
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return HttpResponse("Item not found", status=404)

    available_quantity = Purchase_Details.objects.filter(item=item).aggregate(total=models.Sum('quantity'))['total']

    print(available_quantity)
    response_content = f"<h1>{available_quantity}</h1>"
   
    return HttpResponse(response_content)
 #---------------------------------------
def x(request):
      mstr_form = SaleMstrForm(request.POST)
      details_form = SaleDetailsForm(request.POST)
      
      if request.method == 'POST':
        # Get form data from request.POST dictionary
           invoice_number =mstr_form.request.POST.get('invoice_no')
         
        # ... other form fields ...

        # Process the form data as needed
        # ...

        # Return an appropriate response
           return JsonResponse({'message': invoice_number})
 
      return render(request, '.html', {'mstr_form': mstr_form})


#---------------------------------------------------

#--------------------------------------------------


# def Final_availability(request):
#     purchase_quantities = (
#         Purchase_Details.objects.values('item_id__item_name')
#         .annotate(purchase_quantity=Sum('quantity'))
#     )
#     print(purchase_quantities)

#     sale_quantities = (
#         Sale_Details.objects.values('item_id__item_name')
#         .annotate(sale_quantity=Sum('quantity'))
#     )
#     print(sale_quantities)

#     merge = []
#     for item_purchase in purchase_quantities:
#         item_name = item_purchase['item_id__item_name']
#         purchase_quantity = item_purchase['purchase_quantity']
#         sale_quantity = next(
#             (
#                 item['sale_quantity']
#              for item in sale_quantities
#              if item['item_id__item_name'] == item_name
#              ),
#             0
#         )
#         available_quantity = purchase_quantity - sale_quantity

#         merge.append({
#             'item_name': item_name,
#             'purchase_quantity': purchase_quantity,
#             'sale_quantity': sale_quantity,
#             'available_quantity': available_quantity,
#         })

#     return render(request, 'Available.html', {'data': merge})

# def Temp_Data_sale(request):
#     print("working")
    
#     alldata = Temp_Table_Sales.objects.all()  
#     mstr_form = SaleMstrForm()
#     details_form = SaleDetailsForm()
#     t_amount=0
#     for am in alldata:
#         t_amount+=am.amount
        
#     dt = Temp_Table_Sales.objects.last()

#     if request.method == 'POST':
#         mstr_form = SaleMstrForm(request.POST)
#         details_form = SaleDetailsForm(request.POST)
#         if mstr_form.is_valid() and details_form.is_valid():
#             customer_name=mstr_form.cleaned_data['customer_name']
#             invoice_no=mstr_form.cleaned_data['invoice_no']
#             invoice_date=mstr_form.cleaned_data['invoice_date']
#             number=mstr_form.cleaned_data['number']

#             #----------------------------------
#             item_id=details_form.cleaned_data['item_id']
#             quantity=details_form.cleaned_data['quantity']
#             price=details_form.cleaned_data['price']
#             amount=details_form.cleaned_data['amount']
           
#             temp=Temp_Table_Sales.objects.create(customer_name=customer_name,
#                             invoice_no=invoice_no,
#                             invoice_date=invoice_date,
#                             number=number,
#                             item_id=item_id,
#                             quantity=quantity,
#                             price=price,
#                             amount=amount
                            
#                             )
            
#             return redirect('sale_form')
   
#     else:
#          mstr_form = SaleMstrForm()
#          details_form = SaleDetailsForm()
         
#          if dt:
#             dic = {
#             'customer_name': dt.customer_name,
#                 'invoice_no': dt.invoice_no,
#                 'invoice_date': dt.invoice_date,
#                 'number': dt.number,
#         }
#             print(dic)
#          mstr_form = SaleMstrForm(initial=dic)
#          print(dic)
#         # Redirect to a success page
        
       
    
        
#     if 'create_sale' in request.POST:
#         if request.method == 'POST':
       
#         # used default as we defined InventoryIMS db there
#          with connections['default'].cursor() as cursor:
#             # Insert data from TempPurchase into PurchaseMaster
#             insert_sale_master_sql = """
#             INSERT INTO app_sale_mstr(customer_name, invoice_no, invoice_date, number, totoal)
            
           
#             SELECT customer_name, invoice_no, invoice_date, number, SUM(amount)
#             FROM app_temp_table_sales
#             GROUP BY customer_name, invoice_no, invoice_date, number
#             """
#             cursor.execute(insert_sale_master_sql)

#             # Retrieve the last inserted ID from purchase_master
#             sale_master=Sale_Mstr.objects.latest('id')
#             sale_master_id=sale_master.id
#             print(sale_master_id)
#             print("hello")
            

#             # # Insert data from TempPurchase into PurchaseDetails
#             insert_sale_details_sql = """
#               INSERT INTO app_sale_details ( sale_mstr_id, quantity, price, amount, item_id_id)
            
#             SELECT %s, quantity, price, amount, item_id_id FROM app_temp_table_sales
#             """
#             cursor.execute(insert_sale_details_sql, [sale_master_id])

#             # # # Clear TempPurchase table
#             clear_temp_sale_sql = "DELETE FROM app_temp_table_sales"
#             cursor.execute(clear_temp_sale_sql)

#         return redirect('sale')  
        
        
#     return render(request, 'sale.html', {'mstr_form': SaleMstrForm, 'details_form': SaleDetailsForm,'key1':alldata,'amount':t_amount})


# def Final_availability(request):
#     with connection.cursor() as cursor:
#         cursor.execute("""
#             SELECT
#                 item_id AS item_name,
#                 COALESCE(SUM(quantity), 0) AS purchase_quantity
#             FROM
#                 app_purchase_details
#             GROUP BY
#                 item_id
#         """)
#         purchase_quantities = {row[0]: row[1] for row in cursor.fetchall()}

#         cursor.execute("""
#             SELECT
#                 item_id_id AS item_name,
#                 COALESCE(SUM(quantity), 0) AS sale_quantity
#             FROM
#                 app_sale_details
#             GROUP BY
#                 item_id_id
#         """)
#         sale_quantities = {row[0]: row[1] for row in cursor.fetchall()}

#         merge = []

#         for item_name in purchase_quantities:
#              purchase_quantity = purchase_quantities[item_name]
#              sale_quantity = sale_quantities.get(item_name, 0)
#              available_quantity = purchase_quantity - sale_quantity

#              merge.append({
#                 'item_name': item_name,
#                 'purchase_quantity': purchase_quantity,
#                 'sale_quantity': sale_quantity,
#                 'available_quantity': available_quantity,
#             })
#              print(merge)
    
#     return render(request, 'Available.html',{'data':merge})
#--------------------Another Trick to Calculate Total Stock----------------


# def Final_availability(request):
#     # Aggregate purchase quantities by item name
#     purchase_quantities = Purchase_Details.objects.values('item_id__item_name').annotate(purchase_quantity=Sum('quantity'))

#     # Aggregate sale quantities by item name and create a dictionary
#     sale_quantities_dict = {item['item_id__item_name']: item['sale_quantity'] for item in Sale_Details.objects.values('item_id__item_name').annotate(sale_quantity=Sum('quantity'))}

#     # Merge purchase and sale quantities and calculate available quantity
#     merge = []
#     for item_purchase in purchase_quantities:
#         item_name = item_purchase['item_id__item_name']
#         purchase_quantity = item_purchase['purchase_quantity']
#         sale_quantity = sale_quantities_dict.get(item_name, 0)
#         available_quantity = purchase_quantity - sale_quantity

#         merge.append({
#             'item_name': item_name,
#             'purchase_quantity': purchase_quantity,
#             'sale_quantity': sale_quantity,
#             'available_quantity': available_quantity,
#         })

#     # Return JSON response with merged data
#     return JsonResponse({'data': merge})

# def Final_availability(request):
#     purchase_quantities = (
#         Purchase_Details.objects.values('item_id__item_name')
#         .annotate(purchase_quantity=Sum('quantity'))
#     )

#     sale_quantities = (
#         Sale_Details.objects.values('item_id__item_name')
#         .annotate(sale_quantity=Sum('quantity'))
#     )

#     merge = []
#     for item_purchase in purchase_quantities:
#         item_name = item_purchase['item_id__item_name']
#         purchase_quantity = item_purchase['purchase_quantity']
#         sale_quantity = next(
#             (
#                 item['sale_quantity']
#              for item in sale_quantities
#              if item['item_id__item_name'] == item_name
#              ),
#             0
#         )
#         available_quantity = purchase_quantity - sale_quantity

#         merge.append({
#             'item_name': item_name,
#             'purchase_quantity': purchase_quantity,
#             'sale_quantity': sale_quantity,
#             'available_quantity': available_quantity,
#         })

#     return render(request, 'Available.html', {'data': merge})

    
# def Purchase_Details(request):
#     with connections['default'].cursor() as cursor:
#         purchase_mstr_id = 46
#         sql_query = """
# SELECT
#     pm.id AS purchase_id,
#     pm.invoice_date,
#     pm.total_amount AS invoice_total_amount,
# 	pm.invoice_no,
#     s.supplier_name,
#     pd.id AS item_id,
#     pd.quantity,
#     pd.price AS rate,
#     pd.total AS total_price,
#     i.item_name
# FROM
#     app_purchase_mstr AS pm
# INNER JOIN
#     app_purchase_details AS pd ON pm.id = pd.purchase_mstr_id
# INNER JOIN
#     app_supplier AS s ON pm.supplier_id_id = s.id
# INNER JOIN
#     app_item AS i ON pd.item_id = i.id
#      WHERE
#     pd.id = %s;
   
    
# """
#     # cursor.execute(sql_query)
#         cursor.execute(sql_query, [purchase_mstr_id])
#         results = cursor.fetchall()
       
#     print(results)
#     return render(request,'purchasereport.html',{'key1':results})

  
# def Final_availability(request):
#     # Retrieve purchase quantities
#     purchase_quantities = (
#         Purchase_Details.objects.values('item_id__item_name')
#         .annotate(purchase_quantity=Sum('quantity'))
#     )

#     # Retrieve sale quantities and store them in a dictionary
#     sale_quantities_dict = {
#         item['item_id__item_name']: item['sale_quantity']
#         for item in Sale_Details.objects.values('item_id__item_name')
#         .annotate(sale_quantity=Sum('quantity'))
#     }

#     merge = []
#     for item_purchase in purchase_quantities:
#         item_name = item_purchase['item_id__item_name']
#         purchase_quantity = item_purchase['purchase_quantity']
        
#         # Lookup sale quantity directly from the dictionary
#         sale_quantity = sale_quantities_dict.get(item_name, 0)
        
#         available_quantity = purchase_quantity - sale_quantity

#         merge.append({
#             'item_name': item_name,
#             'purchase_quantity': purchase_quantity,
#             'sale_quantity': sale_quantity,
#             'available_quantity': available_quantity,
#         })

#     return render(request, 'Available.html', {'data': merge})   



    
        
   
    
    

    

   


    
    
     
    
   