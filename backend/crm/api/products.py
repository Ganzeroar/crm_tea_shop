from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from crm.models import Products, ProductType
from crm.serializers.products import ProductsSerializer


class OneProduct(CreateAPIView, ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class SpecificProduct(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsOfTypes(ListAPIView):
    serializer_class = ProductsSerializer

    # def get_queryset(self):
    #     print(self.kwargs)
    #     print(self)
    #     product_type_pk = self.kwargs['pk']
    #     product_type_obj = ProductType.objects.get(pk=product_type_pk)
    #     queryset = self.filter(product_type=product_type_obj)
    #     return queryset
    def get_queryset(self):
        product_type_pk = self.kwargs['pk']
        product_type_obj = ProductType.objects.get(pk=product_type_pk)
        return Products.objects.filter(product_type=product_type_obj)
