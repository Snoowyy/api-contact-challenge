from django.db import models
from django.contrib.auth.models import User

from contacts.models import Contact


class ContactsGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    contacts = models.ManyToManyField(
        related_name='ContactsGroup', to=Contact,
    )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
