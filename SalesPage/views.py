from django.shortcuts import render,redirect
from . import forms
from . import models
from django.core.mail import send_mail
import os
from dotenv import load_dotenv

load_dotenv()

# Create your views here.


def sales_page(request,product_name):
    if request.method=="POST":
        content = request.POST
        first_name=content.get('first_name')
        last_name=content.get('last_name')
        phone_no= content.get('phone_no')
        alternate_phone_no=content.get('alternative_phone_no')
        address=content.get('address')
        product_qty=content.get("qty_of_product")
        custom_message=f"\n\nFirst Name: {first_name}  Last Name: {last_name}\nPhone num: {phone_no}\nAlternaive Phone num: {alternate_phone_no}\nAddress: {address}\nproduct qty: {product_qty}"
        send_mail(
                subject='Product Order from JudisVill Resources ',
                message=custom_message,
                from_email=None,
                recipient_list=[os.environ.get("EMAIL"),],
        )

        return redirect('thank-you-page',product_name=product_name.title())

    product_obj=models.SalesPage.objects.get(product_name=product_name)
    description_list=product_obj.product_description.split("|")
    price_list=product_obj.product_price.split("|")
    prod_options={}
    for n in range(len(price_list)):
        prod_options[f"{price_list[n]}"]=price_list[n]
    print(prod_options)
    form=forms.SalesForm(product_options=prod_options)
    arguments={'form':form,"product":product_obj,
               "descriptions":description_list,"prices":price_list}

    return render(request,f"sales/sales-page1.html",arguments)


def thank_you_page(request,product_name):
    product_obj=models.SalesPage.objects.get(product_name=product_name)
    return render(request,'sales/thank-you-page.html',{"product_obj":product_obj})



def home_page(request):
    return render(request,'sales/index.html')