from rest_framework import serializers
from contacts.models import ContactsGroup

class ContactsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactsGroup
        fields = ['name', 'description', 'user']
        
