from crm.models import ProductType
from rest_framework import serializers


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'
