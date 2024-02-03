from rest_framework import serializers
from .models.entities import *
from .models.components import *


class PersonSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'

    def get_age(self, obj):
        if hasattr(self, 'context') and 'age' in self.context:
            return obj.age
        return None


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'


class OwnershipFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnershipForm
        fields = '__all__'


class LegalEntitySerializer(serializers.ModelSerializer):
    details = DetailsSerializer()
    ownershipForm = OwnershipFormSerializer()
    address = AddressSerializer()

    class Meta:
        model = LegalEntity
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    company = LegalEntitySerializer()  # Используем LegalEntitySerializer для company

    class Meta:
        model = Employee
        fields = '__all__'

    def get_age(self, obj):
        if hasattr(self, 'context') and 'age' in self.context:
            return obj.age
        return None
