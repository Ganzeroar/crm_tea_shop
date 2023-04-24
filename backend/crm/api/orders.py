from rest_framework.generics import CreateAPIView, RetrieveAPIView
from crm.models import Orders as Orders_model
from crm.serializers.orders import SpecificOrdersSerializer


class Orders(CreateAPIView):
    queryset = Orders_model.objects.all()
    serializer_class = SpecificOrdersSerializer


class OneOrder(RetrieveAPIView):
    queryset = Orders_model.objects.all()
    serializer_class = SpecificOrdersSerializer
