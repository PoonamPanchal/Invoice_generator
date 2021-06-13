from django.shortcuts import render, HttpResponse, redirect
from .models import Invoices
from django.http import JsonResponse
from django.contrib import messages

import json

# Create your views here.
# Home Page
# add invoice


def add_invoice(request):
    if request.method == "POST":
        invoice_details = dict()
        invoice_id = request.POST['invoice_id']
        address = request.POST['address']
        total_items = request.POST.getlist('name')
        invoice_details['address'] = address
        invoice_details['total_amount'] = float(request.POST['grand_total'])
        invoice_details['items'] = []
        for i in range(0, len(total_items)):
            invoice_details['items'].append({'name': request.POST.getlist('name')[i],
                                            'quantity': int(request.POST.getlist('quantity')[i]), 
                                            'price': float(request.POST.getlist('price')[i]), 
                                            'amount': float(request.POST.getlist('amount')[i]), 
                                        'tax': float(request.POST.getlist('tax')[i]), 
                                        'total_amount': float(request.POST.getlist('total')[i])})
        insert_data = Invoices(invoice_id=invoice_id,
                               details=json.dumps(invoice_details, indent=4))
        insert_data.save()
        messages.success(request, "Invoice has been saved")

        return redirect('invoice_list')
    else:
        return render(request, 'main/home.html')


def Home(request):
    return render(request, 'main/home.html')
# Invoice Generate


def Invoice_list(request):
    Invoice_list = Invoices.objects.all().order_by('-id')[:10]

    return render(request, 'main/invoice_list.html', {'Invoice_list': Invoice_list})


def validate_invoice(request):
    if request.is_ajax and request.method == "GET":
        # get the invoice id from the client side.
        invoice_id = request.GET.get("invoice_id", None)

        # check for the invoice id in the database.
        if Invoices.objects.filter(invoice_id=invoice_id).exists():
            # if invoice_id found return not valid new invoice_id
            return JsonResponse({"valid": False}, status=200)
        else:
            # if invoice_id not found, then user can create a invoice_id.
            return JsonResponse({"valid": True}, status=200)

    return JsonResponse({}, status=400)
