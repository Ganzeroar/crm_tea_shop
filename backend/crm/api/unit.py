from rest_framework.generics import RetrieveAPIView
from crm.models import ProductUnit
from crm.serializers.unit import UnitSerializer


class UnitView(RetrieveAPIView):
    queryset = ProductUnit.objects.all()
    serializer_class = UnitSerializer
