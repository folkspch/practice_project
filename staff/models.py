from unittest.util import _MAX_LENGTH
from django.db import models
import datetime
# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    mobile_phone = models.CharField(max_length=16)
    password = models.CharField(max_length=128)
    address = models.TextField()
    dob = models.DateField(null=True, blank=True, default=None, max_length=10)
    role = models.CharField(max_length=4)
    code = models.CharField(max_length=16, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(null=True, auto_now=True )

    def get_absolute_url(self):
        return 
