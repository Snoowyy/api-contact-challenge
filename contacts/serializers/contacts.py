from rest_framework import serializers
from contacts.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'mail', 'telephone', 'user',  'created_at']

    def validate_mail(self, value: str):
        if not value.find('@'):
            raise serializers.ValidationError("El correo electrónico no es valido")
        return value

    def validate_telephone(self, value):
        if not value.isdigit() or len(value) < 7:
            raise serializers.ValidationError("El número de teléfono debe contener solo dígitos y tener al menos 7 caracteres")
        return value
