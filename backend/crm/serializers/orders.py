from crm.models import Orders, OrderStatus, ProductOrder
from rest_framework import serializers
from .clients import ClientsSerializer

class SpecificOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'product', 'client']

    def create(self, validated_data):
        status = OrderStatus.objects.get(name='В работе')
        # validated_data['status'] = status
        print(validated_data)
        product = validated_data['product']
        # products = ProductOrder.filter()
        obj = Orders.objects.create(client=validated_data['client'], status=status)
        obj.product.set(product)
        return obj

class SpecificStatusOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'status', 'product', 'client']


class OrdersSerializer(serializers.ModelSerializer):
    # deprecated
    client = ClientsSerializer()
    order = SpecificOrdersSerializer()

    class Meta:
        model = Orders
        fields = ['client', 'order']



class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = '__all__'