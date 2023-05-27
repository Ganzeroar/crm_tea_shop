from crm.models import Products
from rest_framework import serializers


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class SpecificProductsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Products
        fields = ['id']
