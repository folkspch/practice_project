from unittest import result
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .decorators import staff_only, allowed_users
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='/staff/login')
@staff_only
def product_view(request):
    session_key = request.session._session_key
    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)
    user_role = user.groups.all().get()
    user_role = str(user_role)
    print(type(user_role))
    query_set = Product.objects.all().values()
    context ={
        "object": query_set,
        "user": user_role
    }

    return render(request, "product/product_view.html", context)

@allowed_users(allowed_roles=['admin'])
def product_create(request):
    name = request.POST['name']
    desc = request.POST['desc']
    qty = request.POST['qty']
    price = request.POST['price']
    if 'is_avbl' in request.POST:
        is_avbl = True
    else:
        is_avbl = False
    product = Product(name = name, description = desc, quantity = qty, price = price,is_available = is_avbl)
    product.save()
    return redirect('/')
    # form = ProductForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     form = ProductForm()
    #     return redirect('/')
    # context = {
    #     'form': form
    # }
    # return render(request, "product_create.html", context)

@allowed_users(allowed_roles=['admin'])
def product_update(request, id):
    name = request.POST['name']
    desc = request.POST['desc']
    qty = request.POST['qty']
    price = request.POST['price']
    # is_avbl = request.POST.get['is_avbl',False]
    if 'is_avbl' in request.POST:
        is_avbl = True
    else:
        is_avbl = False
    product = Product.objects.get(id=id)
    product.name = name
    product.description = desc
    product.quantity = qty
    product.price = price
    product.is_available = is_avbl
    product.save()
    return redirect('/')
    # obj = Product.objects.get(id=id)
    # form = ProductForm(request.POST or None, instance=obj)
    # print(obj)
    # if form.is_valid():
    #     form.save()
    #     return redirect('/')
    # context = {
    #     'form': form
    # }
    # return render(request, "product_update.html", context)
@allowed_users(allowed_roles=['admin'])
def product_delete(request,id):
    print(id)
    obj = Product.objects.get(id=id)
    obj.delete()
    return redirect('/')

def product_get(request,id):
    obj = Product.objects.get(id=id)
    ctx = {
        'data': obj
    }
    print(id)
    return id

@allowed_users(allowed_roles=['admin'])
def product_sendEmail(request):
    # query_set = Product.objects.all().values()
    # context ={
    #     "object": query_set 
    # }
    # print(query_set)
    # print(type(context))
    return render(request, "product/product_sendEmail.html")

def send_email(request):
    subject = request.POST["subject"]
    message = request.POST["message"]
    from_email = "kmutnbcourtreservation@gmail.com"
    toEmail = request.POST["email"]
    listEmail = list(toEmail.split(','))
    recipient_list = listEmail
    print(recipient_list)
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, recipient_list )
        except:
            print('error')
        return HttpResponseRedirect('/sendEmail')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')
    

def search(request):
    search_key = request.POST['search']
    if request.method == 'POST':
        result = Product.objects.filter(name__contains=search_key)
        return render(request,'product/product_search.html',{'search_result':result})

    else:
        return render(request,'product/product_search.html',{})
    
