from rest_framework.generics import ListAPIView
from crm.models import City
from crm.serializers import CitySerializer


class Cities(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
