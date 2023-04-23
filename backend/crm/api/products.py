from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from crm.models import Products
from crm.serializers.products import ProductsSerializer


class OneProduct(CreateAPIView, ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class SpecificProduct(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
