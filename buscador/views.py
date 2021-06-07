from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import Recibo, Empleado
from .serializers import EmpleadoSerializer, ReciboSerializer


# Create your views here.

class ReciboRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new Recibo.
    """
    #permission_classes = [IsAdminUser]

    def get(self, request, control, periodo):
        recibo = Recibo.objects.filter(no_control=control, periodo=periodo)
        serializer = ReciboSerializer(recibo, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReciboSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, 
                            status= status.HTTP_201_CREATED)

        return Response(serializer.errors, 
                            status= status.HTTP_400_BAD_REQUEST)


class EmpleadoRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new Empleado.
    """
    #permission_classes = [IsAdminUser]

    def get(self, request, control):
        recibos = Empleado.objects.filter(no_control=control)

        serializer = EmpleadoSerializer(recibos, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpleadoSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, 
                            status= status.HTTP_201_CREATED)

        return Response(serializer.errors, 
                            status= status.HTTP_400_BAD_REQUEST)


class EmpleadoRecordNameView(APIView):

    def get(self, request, nombre, ape_p, ape_m):
        recibos = Empleado.objects.filter(nombre=nombre,  apellido_p=ape_p, apellido_m=ape_m)

        serializer = EmpleadoSerializer(recibos, many=True)

        return Response(serializer.data)
