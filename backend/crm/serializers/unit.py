from crm.models import ProductUnit
from rest_framework import serializers


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUnit
        fields = '__all__'
