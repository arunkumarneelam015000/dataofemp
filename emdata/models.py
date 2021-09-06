from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length = 100, blank = False ) # name of the column
    father_name = models.CharField(max_length = 100, blank = False)
    customer_profile = models.CharField(max_length = 100, blank = False)
    loan_account_no = models.IntegerField()
    def __str__(self):
        return 'Customer_Name : {0} Loan_Account_No {1}'.format(self.customer_name, self.loan_account_no)

class BranchData(models.Model):
    zone_name = models.CharField(max_length=100, blank=False)
    region_name = models.CharField(max_length=100, blank=False)
    area_name = models.CharField(max_length=100, blank = False )
    branch_code = models.IntegerField()
    def __str__(self):
        return 'Zone_Name : {0} Branch_code {1}'.format(self.zone_name, self.branch_code)

class CustomerHomeAddress(models.Model):
    addressOne = models.CharField(max_length=100, blank=False)
    addressTwo = models.CharField(max_length=100, blank = False)
    pinCode = models.IntegerField()

    def __str__(self):
        return 'AddressOne : {0} PinCode : {1}'.format(self.addressOne, self.pinCode)
        

