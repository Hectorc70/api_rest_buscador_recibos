from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Recibo, Empleado
from .serializers import EmpleadoSerializer, ReciboSerializer


# Create your views here.

class ReciboRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    #permission_classes = [IsAdminUser]

    def get(self, request, control, periodo):
        recibo = Recibo.objects.filter(no_control=control, periodo=periodo)
        serializer = ReciboSerializer(recibo, many=True)

        return Response(serializer.data)


class EmpleadoRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    #permission_classes = [IsAdminUser]

    def get(self, request, control):
        recibos = Empleado.objects.filter(name=control)

        serializer = EmpleadoSerializer(recibos, many=True)

        print(serializer)
        return Response(serializer.data)



