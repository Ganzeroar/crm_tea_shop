from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from crm.models import Products, ProductType
from crm.serializers.products import ProductsSerializer

from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class OneProduct(CreateAPIView, ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class SpecificProduct(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsOfTypes(ListAPIView):
    serializer_class = ProductsSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        product_type_pk = self.kwargs['pk']
        product_type_obj = ProductType.objects.get(pk=product_type_pk)
        return Products.objects.filter(product_type=product_type_obj).order_by('name')
