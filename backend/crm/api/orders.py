from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from crm.models import Orders as Orders_model, ProductOrder
from crm.serializers.orders import SpecificOrdersSerializer, ProductOrderSerializer, SpecificStatusOrdersSerializer



class Orders(CreateAPIView, ListAPIView):
    queryset = Orders_model.objects.all()
    serializer_class = SpecificOrdersSerializer

class OneOrder(RetrieveAPIView):
    queryset = Orders_model.objects.all()
    serializer_class = SpecificStatusOrdersSerializer

class ProductOrderView(CreateAPIView):
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer