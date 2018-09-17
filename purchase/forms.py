from django import forms

from purchase.models import Purchase


class PurchaseOrderFroms(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['pur_location_name', 'pur_cust_name', 'pur_modify_date', 'cust_id', 'pur_handle']
