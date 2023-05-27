from crm.serializers.clients import ClientPhoneSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PhoneValidator(APIView):

    def get(self, request, *args, **kwargs):
        phone = self.kwargs.get('phone') 

        phone_serializer = ClientPhoneSerializer(data={'phone': phone})
        if phone_serializer.is_valid():
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
