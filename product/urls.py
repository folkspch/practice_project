from django.urls import path

from .views import (
    product_sendEmail,
    product_view,
    product_create,
    product_update,
    product_delete,
    product_get,
    product_sendEmail,
    send_email
    )

urlpatterns = [
    path('', product_view),
    path('view/', product_view),
    path('create/', product_create),
    path('get/<int:id>/', product_get), 
    path('update/<int:id>/', product_update), 
    path('delete/<int:id>/', product_delete),
    path('sendEmail/',product_sendEmail),
    path('send_email/',send_email)
]