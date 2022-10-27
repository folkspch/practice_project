
from django.urls import path
from .views import (
    staff_view,
    staff_create,
    staff_update,
    staff_delete,
    login_view,
    logout_view,
    )
urlpatterns = [
    path('', staff_view),
    path('create/', staff_create),
    path('update/<int:id>/', staff_update),
    path('delete/<int:id>/', staff_delete),
    path('login/', login_view),
    path('logout/', logout_view),
]
