from crm.models import Orders
from rest_framework import serializers
from .clients import ClientsSerializer

class SpecificOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'



class OrdersSerializer(serializers.ModelSerializer):
    client = ClientsSerializer()
    order = SpecificOrdersSerializer()

    class Meta:
        model = Orders
        fields = ['client', 'order']

