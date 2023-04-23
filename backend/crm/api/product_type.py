from rest_framework.generics import RetrieveAPIView
from crm.models import ProductType
from crm.serializers.product_type import ProductTypeSerializer


class ProductType(RetrieveAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
