from django.shortcuts import render
from . import forms
from . import models
from django.core.mail import send_mail

# Create your views here.


def sales_page(request,page_no):
    if request.method=="POST":
        pass
    product_obj=models.SalesPage.objects.get(id=page_no)
    description_list=product_obj.product_description.split("|")
    price_list=product_obj.product_price.split("|")
    prod_options={}
    for n in range(len(price_list)):
        prod_options[f"option_{n+1}"]=price_list[n]
    print(prod_options)
    form=forms.SalesForm(product_options=prod_options)
    arguments={'form':form,"product":product_obj,
               "descriptions":description_list,"prices":price_list}

    return render(request,f"sales/sales-page{page_no}.html",arguments)