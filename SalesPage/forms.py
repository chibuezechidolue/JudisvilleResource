from collections.abc import Mapping
from typing import Any
from django import forms
from django.forms.utils import ErrorList

class SalesForm(forms.Form):
    first_name=forms.CharField(max_length=100,required=True)
    last_name=forms.CharField(max_length=100,required=True)
    phone_no=forms.CharField(widget=forms.NumberInput,required=True)
    alternative_phone_no=forms.CharField(widget=forms.NumberInput)
    address=forms.CharField(widget=forms.Textarea,required=True)
    qty_of_product=forms.ChoiceField(required=True,widget=forms.RadioSelect,choices={})

    def __init__(self,*args,**kwargs,) -> None:
        product_options = kwargs.pop('product_options', None)
        super(SalesForm, self).__init__(*args, **kwargs)
        self.fields['qty_of_product'].choices = product_options

    class Meta:
        fields=['first_name','last_name',"phone_no","alternative_phone_no","address",'qty_of_product']


