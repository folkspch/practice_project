from email.policy import default
from tkinter import Widget
from django import forms
from .models import Product


# class RawProductForm(forms.Form):
#     name      = forms.CharField()
#     description = forms.CharField()
#     quantity      = forms.DecimalField()
#     price     = forms.DecimalField()
#     is_available     = forms.BooleanField(required=False)

class ProductForm(forms.ModelForm):
    inputStyle = 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
    name      = forms.CharField(widget=forms.TextInput(attrs={'class': inputStyle}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': inputStyle}))
    quantity      = forms.DecimalField(widget=forms.TextInput(attrs={'class': inputStyle}))
    price     = forms.DecimalField(widget=forms.TextInput(attrs={'class': inputStyle}))
    is_available     = forms.BooleanField(required=False)

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'quantity',
            'price',
            'is_available'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }