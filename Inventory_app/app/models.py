from django.db import models

# Create your models here.
class Item(models.Model):
    item_name=models.CharField(max_length=70)
    item_code=models.IntegerField()
    price=models.IntegerField()
    status=models.BooleanField(False)
    datetime=models.DateField()
    
    def __str__(r):
        return r.item_name
    
class Supplier(models.Model):
    supplier_name=models.CharField(max_length=70)
    mobile_no=models.CharField(max_length=12)
    address=models.CharField(max_length=100)
    datetime=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)
    
    def __str__(r):
        return r.supplier_name
class Purchase_Mstr(models.Model):
    
    invoice_no=models.CharField(max_length=50)
    invoice_date=models.DateField()
    supplier_id=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    total_amount=models.DecimalField(max_digits=10, decimal_places=2)
   
    def __str__(r):
        return r.supplier_id
class Purchase_Details(models.Model):
    # Purchase_Mstrs_id=models.ForeignKey(Purchase_Mstr, on_delete=models.CASCADE)
    purchase_mstr = models.ForeignKey(Purchase_Mstr, on_delete=models.CASCADE)
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    total=models.DecimalField(max_digits=10, decimal_places=2)
    #status=models.BooleanField(default=False)
    
    
    
class Temp_Table(models.Model):
    invoice_no=models.CharField(max_length=50)
    invoice_date=models.DateField()
    supplier_id=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    total=models.DecimalField(max_digits=10, decimal_places=2)
 
class Sale_Mstr(models.Model):
    customer_name=models.CharField(max_length=50)
    invoice_no=models.CharField(max_length=50)
    invoice_date=models.DateField()
    number=models.CharField(max_length=20)
    totoal=models.CharField(max_length=30)
    
    def __str__(r):
        return r.customer_name
    
class Sale_Details(models.Model):
    item_id=models.ForeignKey(Item, on_delete=models.CASCADE)
    sale_mstr = models.ForeignKey(Sale_Mstr, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(r):
        return r.item_id
    
    
    
class Temp_Table_Sales(models.Model):
    customer_name=models.CharField(max_length=50)
    invoice_no=models.CharField(max_length=50)
    invoice_date=models.DateField()
    number=models.CharField(max_length=20)
    item_id=models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    

    