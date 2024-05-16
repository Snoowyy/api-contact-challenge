from django.urls import path
from contacts.views import (getContacts, getContact,
                            addContact, updateContact, deleteContact)
urlpatterns = [
    path('', getContacts),
    path('create', addContact),
    path('detail/<str:pk>', getContact),
    path('update/<str:pk>', updateContact),
    path('delete/<str:pk>', deleteContact),
]
