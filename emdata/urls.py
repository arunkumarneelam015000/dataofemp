from django.conf.urls import *
from django.urls import *
from .views import *

urlpatterns = [

   url(r'^$', index, name='index'),

    url(r'^$', arun, name='arun'),

    url(r'^display_customer$', display_customer, name='display_customer'),

    url(r'^display_branch_data$', display_branch_data, name='display_branch_data'),

    url(r'^display_customer_home_address$', display_customer_home_address, name='display_customer_home_address'),

    url(r'^aCustomer$', aCustomer, name='aCustomer'),
    url(r'^aBranchData$', aBranchData, name='aBranchData'),
    url(r'^aCustomerHomeAddress$', aCustomerHomeAddress, name='aCustomerHomeAddress'),

    #path('arun/', arun, name = 'arun'),
    #path('arunOne/', arunOne, name='arunOne')

     url(r'^edit_customer/(?P<pk>\d+)$', edit_customer , name='edit_customer'),

     url(r'^edit_branchdata/(?P<pk>\d+)$', edit_branchdata, name='edit_branchdata'),

     url(r'^edit_customerhomeaddress/(?P<pk>\d+)$', edit_customerhomeaddress, name='edit_customerhomeaddress'),






    url(r'^del_customer/(?P<pk>\d+)$', del_customer , name='del_customer'),

     url(r'^del_branchdata/(?P<pk>\d+)$', del_branchdata, name='del_branchdata'),

     url(r'^del_customerhomeaddress/(?P<pk>\d+)$', del_customerhomeaddress, name='del_customerhomeaddress')


]
