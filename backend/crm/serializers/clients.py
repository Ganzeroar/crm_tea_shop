from crm.models import Clients
from rest_framework import serializers


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'
