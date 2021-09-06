
from django import forms 
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_name','father_name','customer_profile','loan_account_no')
class BranchDataForm(forms.ModelForm):
    class Meta:
        model = BranchData
        fields = ('zone_name','region_name','area_name','branch_code')
class CustomerHomeAddressForm(forms.ModelForm):
    class Meta:
        model = CustomerHomeAddress
        fields = ('addressOne','addressTwo','pinCode')
    
