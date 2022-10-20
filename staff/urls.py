
from django.urls import path
from .views import (
    staff_view,
    staff_create,
    staff_update,
    staff_delete,
    )
urlpatterns = [
    path('', staff_view),
    path('create/', staff_create),
    path('update/<int:id>/', staff_update),
    path('delete/<int:id>/', staff_delete),
]
