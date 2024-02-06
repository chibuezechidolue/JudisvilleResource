from django.contrib import admin
from .models import SalesPage

# Register your models here.

class SalesPageAdmin(admin.ModelAdmin):
    list_display=["product_name", "product_price"]

admin.site.register(SalesPage,SalesPageAdmin)