from rest_framework.generics import CreateAPIView
from crm.models import Clients
from crm.serializers.clients import ClientsSerializer


class Clients(CreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
