from django.shortcuts import render, redirect
from .models import Staff
from .forms import StaffForm
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/staff/login')
def staff_view(request):
    # query_set = Staff.objects.all().values()
    query_set = Staff.objects.all().values()
    context ={
        "object": query_set 
    }
    now = datetime.datetime.now()
    print(now)
    return render(request, "staff/staff_view.html", context)

def staff_create(request):
    form = StaffForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StaffForm()
        return redirect('/')
    context = {
        'form': form
    }
    
    return render(request, "staff/staff_create.html", context)

def staff_update(request, id=id):
    obj = Staff.objects.get(id=id)
    form = StaffForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, "staff/staff_update.html", context)

def staff_delete(request, id):
    obj = Staff.objects.get(id=id)
    obj.delete()
    return redirect('/')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            #เช็คความถูกต้อง
            if user is not None: 
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')#loginเสร็จแล้วไปที่หน้า /admin แก้เป็นหน้าอื่นได้เช่น /home
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login/login.html",
                    context={"form":form})

def logout_view(request):
    logout(request)
    #แจ้งว่าlogoutแล้ว แก้ messageได้
    messages.info(request, "Logged out successfully!")
    return redirect("/staff/login") #logoutแล้วไปหน้าที่เรากำหนด แก้ได้                    

# def register_view(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             #เมื่อสมัครเสร็จแล้วจะให้เด้งไปหน้าไหน
#             return redirect("/admin")

#         #เพื่อแจ้งเตือน errorต่างๆ
#         else:
#             for msg in form.error_messages:
#                 print(form.error_messages[msg])

#             return render(request = request,
#                           template_name = "register.html",
#                           context={"form":form}) #นำ form ตรงนี้ไปใช้ใน register.htmlเพื่อrender

#     #เนื่อจากข้างบนเป็น if-elseเลยต้องมีเผื่อไว้
#     form = UserCreationForm
#     return render(request = request,
#                   template_name = "register.html",
#                   context={"form":form})