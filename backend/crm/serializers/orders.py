from crm.models import Orders, OrderStatus, ProductOrder, NotificationInfo
from rest_framework import serializers
import requests


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

        obj = Orders.objects.create(
            client=validated_data['client'],
            status=status,
            destination_address=destination_address,
        )
        for product_order_info in products:
            product_order = ProductOrder.objects.create(**product_order_info)
            obj.product.add(product_order)

            product_obj = product_order_info.get('product')
            order_quantity = product_order_info.get('quantity')
            product_obj.quantity = product_obj.quantity - order_quantity
            product_obj.save()

        url = 'http://127.0.0.1:8888/new_order'
        tg_user_ids_for_notify = NotificationInfo.objects.all()
        print(obj)
        print(validated_data)
        for telegram_user_id_obj in tg_user_ids_for_notify:
            order_id = obj.id
            client_info = obj.client
            client_city = obj.client.city
            products_info = ''
            print(validated_data['product'])
            for product in validated_data['product']:
                product_name = product['product']
                product_unit = product['product'].unit
                product_quantity = product['quantity']
                product_info = f'{product_name} {product_quantity} {product_unit}, '
                products_info += product_info
            print(f'1{products_info}1')
            print(f'1{products_info[:-2]}1')
            products_info = products_info[:-2]
            print(products_info)
            order_url = f'http://127.0.0.1:8000/admin/crm/orders/{order_id}/change/'
            notification_message = f"""Только что поступил новый заказ № {order_id}.

Клиент: {client_info}
Список продуктов: {products_info}
город: {client_city}
адрес: {destination_address}

{order_url} перейдите по ссылке или откройте панель администрирования, чтобы узнать подробнее о заказе."""
            data = {
                'notification_message': notification_message,
                'telegram_user_id': telegram_user_id_obj.telegram_user_id,
            }
            print(data)
            requests.post(url=url, json=data)

        return obj


class SpecificStatusOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'status', 'product', 'client']
