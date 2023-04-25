from crm.models import Orders, OrderStatus
from rest_framework import serializers
from .clients import ClientsSerializer

class SpecificOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'quantity', 'product', 'client']

    def create(self, validated_data):
        status = OrderStatus.objects.get(name='В работе')
        validated_data['status'] =  status
        obj = Orders.objects.create(**validated_data)
        obj.save()
        return obj


class OrdersSerializer(serializers.ModelSerializer):
    # deprecated
    client = ClientsSerializer()
    order = SpecificOrdersSerializer()

    class Meta:
        model = Orders
        fields = ['client', 'order']

