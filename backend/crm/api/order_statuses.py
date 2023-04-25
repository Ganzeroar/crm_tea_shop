from rest_framework.generics import RetrieveAPIView
from crm.models import OrderStatus
from crm.serializers.order_statuses import OrderStatusSerializer


class OrderStatusesView(RetrieveAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer