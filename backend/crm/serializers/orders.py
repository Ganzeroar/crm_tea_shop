from crm.models import Orders, OrderStatus, ProductOrder
from rest_framework import serializers
from .clients import ClientsSerializer
from .products import ProductsSerializer, SpecificProductsSerializer


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = '__all__'


class SpecificOrdersSerializer(serializers.ModelSerializer):
    product = ProductOrderSerializer(many=True)
    class Meta:
        model = Orders
        fields = ['id', 'product', 'client', 'destination_address']

    def create(self, validated_data):
        status = OrderStatus.objects.get(name='В работе')

        products = validated_data['product']

        destination_address = validated_data['destination_address']

        obj = Orders.objects.create(client=validated_data['client'], status=status, destination_address=destination_address)
        for product_r in products:
            product_order = ProductOrder.objects.create(**product_r)
            obj.product.add(product_order)
        return obj


class SpecificStatusOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'status', 'product', 'client']