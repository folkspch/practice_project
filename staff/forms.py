# from enum import auto
from django import forms
from .models import Staff


class StaffForm(forms.ModelForm):
    inputStyle = 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md'
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': inputStyle}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': inputStyle}))
    email      = forms.CharField(widget=forms.TextInput(attrs={'class': inputStyle}))
    mobile_phone   = forms.CharField(widget=forms.TextInput(attrs={'class': inputStyle}))
    password  = forms.CharField(widget=forms.TextInput(attrs={'class': inputStyle}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': inputStyle}))
    dob = forms.DateField(widget=forms.TextInput(attrs={'class': inputStyle,"type":"date"}))
    role = forms.CharField(widget=forms.TextInput(attrs={'class': inputStyle}))
    code = forms.CharField(widget=forms.TextInput(attrs={'class': inputStyle}))

    class Meta:
        model = Staff
        fields = [
            'first_name',
            'last_name',
            'email',
            'mobile_phone',
            'password',
            'address',
            'dob',
            'role',
            'code',
        ]
       

    
#     class Meta:
#         model = Staff
#         fields = [
#             'first_name',
#             'last_name',
#             'email',
#             'mobile_phone',
#             'password',
#             'address',
#             'dob',
#             'role',
#             'code',
#             'created_at',
#             'updated_at',
#         ]
