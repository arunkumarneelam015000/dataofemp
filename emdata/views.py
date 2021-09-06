from employee_data import *
from django.shortcuts import *
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def display_customer(request):
    items = Customer.objects.all()

    context = {
        'items' : items,
        'header' : 'Customers',
        'arun'   : 'Customer Name',
         'arunOne' : 'Father Name',
         'arunTwo' : 'Customer Profile',
         'arunThree' : 'Loan Account No.'
    }

    return render(request, 'index.html', context) # 3 arguments

def display_branch_data(request):
    items = BranchData.objects.all()

    context = {
        'items' : items,
        'header' : 'Branch Data',
        'arun'   : 'Zone Name',
        'arunOne' : 'Region Name',
        'arunTwo' : 'Area Name',
        'arunThree' : 'Branch Code'

       
    }

    return render(request, 'arunOne.html', context) # 3 arguments

def display_customer_home_address(request):
    items = CustomerHomeAddress.objects.all()

    context = {
        'items' : items,
        'header' : 'Customer Home Address Data',
        'arun'   : 'Address 1',
        'arunOne' : 'Address 2',
        'arunTwo' : 'Pin Code'
    }

    return render(request, 'arun.html', context) # 3 arguments


def add_device(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
        

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls()
        return render(request, 'add_new.html', {'form' : form})

def aCustomer(request):
    return add_device(request, CustomerForm)

def aBranchData(request):
    return add_device(request, BranchDataForm)

def aCustomerHomeAddress(request):
    return add_device(request, CustomerHomeAddressForm)
    
def arun(request):
    return render(request, 'arun.html')
def arunOne(request):
    return render(request, 'arunOne.html')

def editpage(request):
    return render(request, 'edit_item.html')
def editpageone(request):
    return render(request, 'edit.html')




def edit_customer(request, pk):
    item = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomerForm(instance=item)
        return render(request, 'edit_item.html', {'form': form})

def edit_branchdata(request, pk):
    item = get_object_or_404(BranchData, pk=pk)

    if request.method == "POST":
        form = BranchDataForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BranchDataForm(instance=item)
        return render(request, 'edit_item.html', {'form': form})


def edit_customerhomeaddress(request, pk):
    item = get_object_or_404(CustomerHomeAddress, pk=pk)

    if request.method == "POST":
        form = CustomerHomeAddressForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomerHomeAddressForm(instance=item)
        return render(request, 'edit_item.html', {'form': form})


def del_customer(request, pk):
    Customer.objects.filter(id=pk).delete()
    items = Customer.objects.all()

    context = {
        'items' : items
    }

    return render(request, 'index.html', context)


def del_branchdata(request, pk):
    BranchData.objects.filter(id=pk).delete()
    items = BranchData.objects.all()

    context = {
        'items' : items
    }

    return render(request, 'arunOne.html', context)


def del_customerhomeaddress(request, pk):
    CustomerHomeAddress.objects.filter(id=pk).delete()
    items = CustomerHomeAddress.objects.all()

    context = {
        'items' : items
    }

    return render(request, 'arun.html', context)




