from rest_framework.generics import RetrieveAPIView, ListAPIView
from crm.models import ProductType
from crm.serializers.product_type import ProductTypeSerializer


class ProductTypeView(RetrieveAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductTypesView(ListAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
