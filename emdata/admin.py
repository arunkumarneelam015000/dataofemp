
from django.contrib import admin
from .models import *

# Register your models here.
from import_export.admin import ImportExportActionModelAdmin

@admin.register(Customer, BranchData, CustomerHomeAddress)

class ViewAdmin(ImportExportActionModelAdmin):
    pass