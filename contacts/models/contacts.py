from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    telephone = models.CharField(max_length=75)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
