from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('invoices/',views.Invoice_list,name='invoice_list'),
    path('validation/',views.validate_invoice,name='validate_invoice'),
    path('add_invoice/',views.add_invoice,name='add_invoice'),
]
