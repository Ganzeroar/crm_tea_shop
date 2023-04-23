from rest_framework.generics import CreateAPIView
from crm.models import Orders
from crm.serializers.orders import OrdersSerializer


class Orders(CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
