from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from crm.models import Orders as Orders_model, ProductOrder
from crm.serializers.orders import SpecificOrdersSerializer, ProductOrderSerializer, SpecificStatusOrdersSerializer
from rest_framework import status
from rest_framework.response import Response


class Orders(CreateAPIView, ListAPIView):
    queryset = Orders_model.objects.all()
    serializer_class = SpecificOrdersSerializer

    # def create(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OneOrder(RetrieveAPIView):
    queryset = Orders_model.objects.all()
    serializer_class = SpecificStatusOrdersSerializer

class ProductOrderView(CreateAPIView):
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer