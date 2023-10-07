from django import forms
from .models import *
from django.forms import DateInput

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        widgets = {
            'datetime': DateInput(attrs={'type': 'date'}),
        }
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"        
        
        
class PurchaseMstrForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(PurchaseMstrForm, self).__init__(*args, **kwargs)
            self.fields['supplier_id'].empty_label="Select Supplier" 
            
    class Meta:
        model = Purchase_Mstr
        fields = ['invoice_no','invoice_date','supplier_id']# 'total_amount'
        widgets = {
            'invoice_date': DateInput(attrs={'type': 'date'}),
        }
   
class PurchaseDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(PurchaseDetailsForm, self).__init__(*args, **kwargs)
            self.fields['item'].empty_label="Select Items" 
            
    class Meta:
        model = Purchase_Details
        fields = ['item', 'quantity', 'price', 'total']   
        # widgets = {
        #     'purchase_id': forms.HiddenInput(),
        # }   
        widgets = {
            'price': forms.TextInput(attrs={'readonly': 'readonly'}),
            'total': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
        
         
        
class SaleMstrForm(forms.ModelForm):
    class Meta:
        model = Sale_Mstr
        fields = ['customer_name','invoice_no','invoice_date','number']# 'total_amount'
        widgets = {
            'invoice_date': DateInput(attrs={'type': 'date'}),
            'invoice_no': forms.TextInput(attrs={'readonly': 'invoice_no'}),
        }
        
        
   

class SaleDetailsForm(forms.ModelForm):
    class Meta:
        model = Sale_Details
        fields = ['item_id', 'quantity', 'price', 'amount']   
        # widgets = {
        #     'purchase_id': forms.HiddenInput(),
        # }          
class DateRangeForm(forms.Form):
    start_date = forms.DateField(label='Start Date',widget=forms.DateInput(attrs={'type': 'date'}))
    
    end_date = forms.DateField(label='End Date',widget=forms.DateInput(attrs={'type': 'date'}))   
    
    
    