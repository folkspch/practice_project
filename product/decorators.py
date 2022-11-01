from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]): #ระบุ role ว่าสามารถทำอะไรได้บ้าง
    def decorator(view_func):
        def wrapper_func1(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func1
    return decorator

def staff_only(view_func): #จำกัดว่า role นั้นๆเข้าหน้าไหน
    def wrapper_func2(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'admin'or 'viewer' :
            return view_func(request, *args, **kwargs)
        else:
                return HttpResponse('You are not authorized to view this page')
    return wrapper_func2
